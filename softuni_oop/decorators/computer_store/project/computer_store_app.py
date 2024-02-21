from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop


class ComputerStoreApp:
    valid_types = ["Desktop Computer", "Laptop"]

    def __init__(self):
        self.warehouse = []
        self.profits = 0

    def build_computer(self, type_computer, manufacturer, model, processor, ram):
        if type_computer not in self.valid_types:
            raise ValueError(f"{type_computer} is not a valid type computer!")
        if type_computer == "Laptop":
            next_comp = Laptop(manufacturer, model)
        else:
            next_comp = DesktopComputer(manufacturer, ram)
        self.warehouse.append(next_comp)
        return next_comp.configure_computer(processor, ram)

    def sell_computer(self, client_budget, wanted_processor, wanted_ram):
        current_stock = self.warehouse
        item_found = False
        item_for_sale = ''
        for item in current_stock:
            if item.processor == wanted_processor and item.ram >= wanted_ram and item.price <= client_budget:
                item_found = True
                item_for_sale = item
                diff = client_budget - item.price
                if diff > 0:
                    self.profits += diff
                self.warehouse.remove(item)

        if not item_found:
            raise Exception("Sorry, we don't have a computer for you.")
        return f"{item_for_sale} sold for {client_budget}$."
