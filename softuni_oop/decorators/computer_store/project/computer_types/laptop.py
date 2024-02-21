from project.computer_types.computer import Computer


class Laptop(Computer):
    available_processors = {
        'AMD Ryzen 9 5950X': 900,
        'Intel Core i9-11900H': 1050,
        'Apple M1 Pro': 1200,
    }
    max_ram = 64

    def __init__(self, manufacturer, model):
        super().__init__(manufacturer, model)
        self.manufacturer = manufacturer
        self.model = model

    def configure_computer(self, processor, ram):

        if processor not in self.available_processors:
            raise ValueError(f"{processor} is not compatible with laptop  {self.manufacturer} {self.model}!")

        if ram % 2 != 0 or ram > self.max_ram:
            raise ValueError(f"{ram}GB RAM is not compatible with laptop  {self.manufacturer} {self.model}!")

        self.processor = processor
        self.ram = ram
        self.price = self.find_product_price(self.available_processors[self.processor], ram)

        return f"Created {self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM for {self.price}$."

    @staticmethod
    def find_product_price(processor_price, ram):
        counter = 0
        while ram > 1:
            ram = ram // 2
            counter += 1
        price = processor_price + counter * 100
        return price

