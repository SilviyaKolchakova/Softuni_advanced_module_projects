from abc import ABC


class Animal(ABC):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def make_sound(self):
        pass

    def __repr__(self):
        pass