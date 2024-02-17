from project.computer_types.computer import Computer


class DesktopComputer(Computer):
    available_processors = {
        'AMD Ryzen 7 5700G': 500,
        'Intel Core i5-12600K': 600,
        'Apple M1 Max': 1800,
    }
    max_ram = 128

    def __init__(self, manufacturer, model):
        super().__init__(manufacturer, model)
        self.manufacturer = manufacturer
        self.model = model

    def configure_computer(self, processor, ram):
        if processor not in self.available_processors:
            raise ValueError(f"{self.processor} is not compatible with desktop computer {self.manufacturer} {self.model}!")
        if ram % 2 != 0 or ram > self.max_ram:
            raise ValueError(f"{ram}GB RAM is not compatible with desktop computer {self.manufacturer} {self.model}!")
        self.processor = processor
        self.ram = ram
        self.price = ram / 2 * 100
        return f"Created {self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM for {self.price}$."