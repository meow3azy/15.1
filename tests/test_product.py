import pytest
from Products.Product import Product
from Products.Smartphone import Smartphone
from Products.Grass import Grass


def test_add_to_category():
    p = Product("Test Product", 10, "TestCategory")
    p.add_to_category(Product)
    assert p.category == "Product"

    s = Smartphone("iPhone", 1000, "Apple", "iPhone 12", 128, "Black")
    s.add_to_category(Smartphone)
    assert s.category == "Smartphone"

    g = Grass("Green Grass", 5, "USA", "2 weeks", "Green")
    g.add_to_category(Grass)
    assert g.category == "Grass"


def test_add_invalid_category():
    p = Product("Test Product", 10, "TestCategory")
    with pytest.raises(TypeError):
        p.add_to_category(str)


def test_add_different_types():
    p1 = Product("Test Product 1", 10, "TestCategory")
    s1 = Smartphone("Test Smartphone 1", 100, "Samsung", "Model1", "64GB", "Black")
    with pytest.raises(TypeError) as e:
        result = p1 + s1
    assert str(e.value) == "Can only add Product objects"

    s = Smartphone("iPhone", 1000, "Apple", "iPhone 12", 128, "Black")
    p = Product("Charger", 20, "Accessory")
    with pytest.raises(TypeError):
        result = s + p
