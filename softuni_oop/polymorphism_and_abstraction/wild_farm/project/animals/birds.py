from project.animals.animal import Bird

class Owl(Bird):
    ALLOWED_FOODS = ['Meat']
    FOOD_INDEX = 0.25

    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, food):
        if food.__class__.__name__ not in self.ALLOWED_FOODS:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.food_eaten += food.quantity
        self.weight += food.quantity * self.FOOD_INDEX


class Hen(Bird):
    FOOD_INDEX = 0.35

    def make_sound(self):
        return "Cluck"

    def feed(self, food):
        # if food not in self.ALLOWED_FOODS:
        #     return f"{self.__class__.__name__} does not eat {food}!"

        self.food_eaten += food.quantity
        self.weight += food.quantity * self.FOOD_INDEX
