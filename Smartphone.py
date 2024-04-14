from main import Product
class Smartphone(Product):
    def __init__(self, name, price, manufacturer, model, storage_capacity, color, performance):
        super().__init__(name, price, "Smartphone")
        self.manufacturer = manufacturer
        self.model = model
        self.storage_capacity = storage_capacity
        self.color = color
        self.performance = performance
