class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        return f"{self.name} - ${self.price}"

    def add_to_category(self, category):
        if isinstance(self, Product) and issubclass(category, Product):
            self.category = category.__name__
        else:
            raise TypeError("Can only add instances of Product or its subclasses to a category")

    def __add__(self, other):
        if not isinstance(other, Product):
            raise TypeError("Can only add Product objects")
        if type(self) != type(other):
            raise TypeError("Cannot add products of different types")
        return self.price + other.price
