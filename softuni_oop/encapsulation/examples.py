from project.beverage.beverage import Beverage
from project.beverage.coffee import Coffee
from project.food.cake import Cake
from project.food.soup import Soup
from project.product import Product

product = Product("coffee", 2.5)
print(product.__class__.__name__)
print(product.name)
print(product.price)
beverage = Beverage("coffee", 2.5, 50)
print(beverage.__class__.__name__)
print(beverage.__class__.__bases__[0].__name__)
print(beverage.name)
print(beverage.price)
print(beverage.milliliters)
coffee = Coffee("fish soup", 5)
print(coffee.__class__.__name__)
print(coffee.__class__.__bases__[0].__name__)
print(coffee.name)
print(coffee.price)
print(coffee.milliliters)
