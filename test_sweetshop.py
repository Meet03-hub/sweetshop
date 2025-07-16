from sweetshop import SweetShop

def test_add_sweet():
    shop = SweetShop()
    shop.add_sweet(1001, "Kaju Katli", "Nut-Based", 50, 20)

    assert len(shop.sweets) == 1
    assert shop.sweets[0]["name"] == "Kaju Katli"
