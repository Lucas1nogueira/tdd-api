from datetime import datetime


def product_data():
    return {
        "name": "Iphone 14 Pro Max",
        "quantity": 10,
        "price": 8500,
        "status": True,
        "updated_at": str(datetime.now()),
    }


def products_data():
    return [
        {"name": "Iphone 11 Pro Max", "quantity": 15, "price": 4500, "status": True},
        {"name": "Iphone 12 Pro Max", "quantity": 20, "price": 6000, "status": True},
        {"name": "Iphone 13 Pro Max", "quantity": 17, "price": 7500, "status": True},
        {"name": "Iphone 15 Pro Max", "quantity": 5, "price": 11000, "status": False},
    ]
