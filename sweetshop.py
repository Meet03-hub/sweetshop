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

    def delete_sweet(self, sweet_id):
        self.sweets = [sweet for sweet in self.sweets if sweet["id"] != sweet_id]

    def view_sweets(self):
        return self.sweets

    def search_sweets(self, name=None, category=None, min_price=None, max_price=None):
        result = self.sweets
        if name:
            result = [s for s in result if s["name"].lower() == name.lower()]
        if category:
            result = [s for s in result if s["category"].lower() == category.lower()]
        if min_price is not None:
            result = [s for s in result if s["price"] >= min_price]
        if max_price is not None:
            result = [s for s in result if s["price"] <= max_price]
        return result

    def purchase_sweet(self, sweet_id, quantity):
        for sweet in self.sweets:
            if sweet["id"] == sweet_id:
                if sweet["quantity"] >= quantity:
                    sweet["quantity"] -= quantity
                    return
                else:
                    raise ValueError("Not enough stock available.")
        raise ValueError("Sweet not found.")

    def restock_sweet(self, sweet_id, quantity):
        for sweet in self.sweets:
            if sweet["id"] == sweet_id:
                sweet["quantity"] += quantity
                return
        raise ValueError("Sweet not found.")
