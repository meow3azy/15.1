from Product import Product


class Grass(Product):
    def __init__(self, name, price, country, sprouting_period, color):
        super().__init__(name, price, "Grass")
        self.country = country
        self.sprouting_period = sprouting_period
        self.color = color
