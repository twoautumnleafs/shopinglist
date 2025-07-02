from extensions import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    unit = db.Column(db.String(10))
    base_price = db.Column(db.Float)

    def __repr__(self):
        return f"<Product {self.name}>"