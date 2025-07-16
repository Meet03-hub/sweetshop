class SweetShop:
    def __init__(self):
        self.sweets = []

    def add_sweet(self, sweet_id, name, category, price, quantity):
        self.sweets.append({
            "id": sweet_id,
            "name": name,
            "category": category,
            "price": price,
            "quantity": quantity
        })
