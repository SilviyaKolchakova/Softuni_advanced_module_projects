from softuni_oop.classes_and_objects.shop.project.product import Product


class Drink(Product):
    def __init__(self, name):
        super().__init__(self, name)
        self.quantity = 10

