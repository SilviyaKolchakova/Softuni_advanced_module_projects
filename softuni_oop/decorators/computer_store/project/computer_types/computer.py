from abc import ABC


class Computer(ABC):
    def __init__(self, manufacturer, model):
        self.manufacturer = manufacturer
        self.model = model
        self.processor = None
        self.ram = None
        self.price = 0

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        if value == '' or value.isspace():
            raise ValueError("Manufacturer name cannot be empty.")
        self.__manufacturer = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if value == '' or value.isspace():
            raise ValueError("Model name cannot be empty.")
        self.__model = value

    def configure_computer(self, processor, ram):
        self.processor = processor
        self.ram = ram

    @staticmethod
    def find_product_price(processor_price, ram):
        pass

    def __repr__(self):
        return f"{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM"

