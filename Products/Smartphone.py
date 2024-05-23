from Product import Product


class Smartphone(Product):
    def __init__(self, name, price, manufacturer, model, memory, color):
        super().__init__(name, price, "Smartphone")
        self.manufacturer = manufacturer
        self.model = model
        self.memory = memory
        self.color = color
