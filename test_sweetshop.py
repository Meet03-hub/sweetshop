from sweetshop import SweetShop
import pytest

def test_add_sweet():
    shop = SweetShop()
    shop.add_sweet(1001, "Kaju Katli", "Nut-Based", 50, 20)
    assert len(shop.sweets) == 1
    assert shop.sweets[0]["name"] == "Kaju Katli"

def test_delete_sweet():
    shop = SweetShop()
    shop.add_sweet(1001, "Kaju Katli", "Nut-Based", 50, 20)
    shop.delete_sweet(1001)
    assert len(shop.sweets) == 0

def test_view_sweets():
    shop = SweetShop()
    shop.add_sweet(1001, "Kaju Katli", "Nut-Based", 50, 20)
    shop.add_sweet(1002, "Gajar Halwa", "Vegetable-Based", 30, 15)
    all_sweets = shop.view_sweets()
    assert len(all_sweets) == 2
    assert all_sweets[0]["name"] == "Kaju Katli"
    assert all_sweets[1]["name"] == "Gajar Halwa"

def test_search_sweets():
    shop = SweetShop()
    shop.add_sweet(1001, "Kaju Katli", "Nut-Based", 50, 20)
    shop.add_sweet(1002, "Gulab Jamun", "Milk-Based", 10, 50)
    shop.add_sweet(1003, "Gajar Halwa", "Vegetable-Based", 30, 15)

    # Search by name
    result_name = shop.search_sweets(name="Kaju Katli")
    assert len(result_name) == 1
    assert result_name[0]["name"] == "Kaju Katli"

    # Search by category
    result_category = shop.search_sweets(category="Milk-Based")
    assert len(result_category) == 1
    assert result_category[0]["name"] == "Gulab Jamun"

    # Search by price range
    result_price = shop.search_sweets(min_price=10, max_price=35)
    assert len(result_price) == 2  # Gulab Jamun and Gajar Halwa

def test_purchase_sweets():
    shop = SweetShop()
    shop.add_sweet(1001, "Kaju Katli", "Nut-Based", 50, 10)

    # Successful purchase
    shop.purchase_sweet(1001, 3)
    assert shop.sweets[0]["quantity"] == 7

    # Unsuccessful purchase (not enough stock)
    with pytest.raises(ValueError) as e:
        shop.purchase_sweet(1001, 15)

    assert str(e.value) == "Not enough stock available."

def test_restock_sweet():
    shop = SweetShop()
    shop.add_sweet(1001, "Kaju Katli", "Nut-Based", 50, 5)

    shop.restock_sweet(1001, 10)
    assert shop.sweets[0]["quantity"] == 15

    with pytest.raises(ValueError) as e:
        shop.restock_sweet(9999, 5)  # Non-existent ID

    assert str(e.value) == "Sweet not found."
