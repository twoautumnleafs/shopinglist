def parse_product_quantity(text: str):
    """Parses input like 'milk 2l' or 'bread 1.5'."""
    parts = text.lower().strip().split()
    if not parts:
        return None, 1.0

    name = parts[0]
    try:
        qty = float(parts[1].replace(',', '.')) if len(parts) > 1 else 1.0
    except ValueError:
        qty = 1.0

    return name, qty