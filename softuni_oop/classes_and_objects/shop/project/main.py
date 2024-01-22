from softuni_oop.classes_and_objects.shop.project.drink import Drink
from softuni_oop.classes_and_objects.shop.project.food import Food
from softuni_oop.classes_and_objects.shop.project.product_repository import ProductRepository

food = Food("apple")
drink = Drink("water")
repo = ProductRepository()
repo.add(food)
repo.add(drink)
# print(repo.products)
print(repo.find("water"))
repo.find("apple").decrease(5)
print(repo)
