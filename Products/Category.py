from Products.Product import Product

class Category:
    def __init__(self, name):
        self.__name = name
        self.__products = []

    def add_product(self, product):
        if not isinstance(product, Product):
            raise ValueError("Товар должен быть экземпляром класса Product")
        self.__products.append(product)

    @property
    def products(self):
        return [f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт." for product in self.__products]

    def __str__(self):
        return f"{self.__name}, количество продуктов: {len(self.__products)} шт."