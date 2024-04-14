from main import Product
from Smartphone import Smartphone
from LawnGrass import LawnGrass

product1 = Product("Phone", 500, "Electronics")
product2 = Smartphone("iPhone", 1000, "Apple", "X", 64, "Black", "High")
product3 = LawnGrass("Grass", 20, "USA", "2 weeks", "Green")

# Вызовет ошибку
total_price = product1 + product2