class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def display_info(self):
        print(f"Name: {self.name}, Price: {self.price}, Category: {self.category}")
    def __add__(self, other):
        if type(self) != type(other):
            raise TypeError("Можно добавлять только товары одного типа")
        return self.price + other.price

class Category:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        if isinstance(product, Product):
            self.products.append(product)
        else:
            raise TypeError("В категорию можно добавлять только экземпляры класса Product или его подклассов.")
