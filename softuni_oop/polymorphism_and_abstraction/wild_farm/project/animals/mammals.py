from project.animals.animal import Mammal


class Mouse(Mammal):
    ALLOWED_FOODS = ['Vegetable', 'Fruit']
    FOOD_INDEX = 0.10

    def make_sound(self):
        return "Squeak"

    def feed(self, food):
        if food.__class__.__name__ not in self.ALLOWED_FOODS:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.food_eaten += food.quantity
        self.weight += food.quantity * self.FOOD_INDEX


class Dog(Mammal):
    ALLOWED_FOODS = ['Meat']
    FOOD_INDEX = 0.40

    def make_sound(self):
        return "Woof!"

    def feed(self, food):
        if food.__class__.__name__ not in self.ALLOWED_FOODS:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.food_eaten += food.quantity
        self.weight += food.quantity * self.FOOD_INDEX


class Cat(Mammal):
    ALLOWED_FOODS = ['Vegetable', 'Meat']
    FOOD_INDEX = 0.30

    def make_sound(self):
        return "Meow"

    def feed(self, food):
        if food.__class__.__name__ not in self.ALLOWED_FOODS:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.food_eaten += food.quantity
        self.weight += food.quantity * self.FOOD_INDEX


class Tiger(Mammal):
    ALLOWED_FOODS = ['Meat']
    FOOD_INDEX = 1.00

    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food):
        if food.__class__.__name__ not in self.ALLOWED_FOODS:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.food_eaten += food.quantity
        self.weight += food.quantity * self.FOOD_INDEX