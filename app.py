from flask import Flask, request, render_template
from services.parser import parse_product_quantity
from services.pricing import get_base_price, get_price_from_tesco, calculate_total, get_unit
from dotenv import load_dotenv
from extensions import db  # подключаем SQLAlchemy
from models.product import Product  # модель Product
from utils.units import BASE_PRICES, units
import os

load_dotenv()

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", "default-secret")
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route("/", methods=["GET", "POST"])
def index():
    city = "Kosice"
    total = None
    prices_real = {}
    selected_items = []

    if request.method == "POST":
        for raw in request.form.getlist("items"):
            name, qty = parse_product_quantity(raw)
            if not name:
                continue
            selected_items.append(name)

            db_product = Product.query.filter_by(name=name).first()
            price = db_product.base_price if db_product else get_price_from_tesco(name) or get_base_price(name) or 0

            prices_real[name] = (price * qty, qty, get_unit(name))

        total = calculate_total(prices_real)

    # Получаем все продукты из базы для боковой панели
    all_products = Product.query.all()

    return render_template("index.html",
                           city=city,
                           total=total,
                           selected_items=selected_items,
                           prices_real=prices_real,
                           prices=BASE_PRICES,
                           units=units,
                           all_products=all_products)


with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(
        debug=True,
        host=os.getenv("HOST", "127.0.0.1"),
        port=int(os.getenv("PORT", 5000))
    )
