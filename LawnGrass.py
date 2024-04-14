from main import Product
class LawnGrass(Product):
    def __init__(self, name, price, country_of_origin, germination_period, color):
        super().__init__(name, price, "Lawn Grass")
        self.country_of_origin = country_of_origin
        self.germination_period = germination_period
        self.color = color
