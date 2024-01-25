class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget < price:
            return "Not enough budget"
        if len(self.animals) == self.__animal_capacity:
            return "Not enough space for animal"

        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):
        if len(self.workers) == self.__workers_capacity:
            return "Not enough space for worker"

        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        salaries_count = sum([worker.salary for worker in self.workers])
        if salaries_count <= self.__budget:
            self.__budget -= salaries_count
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        care_count = sum([animal.money_for_care for animal in self.animals])
        if care_count <= self.__budget:
            self.__budget -= care_count
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals" + '\n'
        lions = [animal for animal in self.animals if animal.__class__.__name__ == 'Lion']
        tigers = [animal for animal in self.animals if animal.__class__.__name__ == 'Tiger']
        cheetahs = [animal for animal in self.animals if animal.__class__.__name__ == 'Cheetah']

        result += f"----- {len(lions)} Lions:" + '\n'
        for lion in lions:
            result += lion.__repr__()  + '\n'

        result += f"----- {len(tigers)} Tigers:" + '\n'
        for tiger in tigers:
            result += tiger.__repr__()  + '\n'

        result += f"----- {len(cheetahs)} Cheetahs:" + '\n'
        for cheetah in cheetahs:
            result += cheetah.__repr__()  + '\n'

        return result.strip()

    def workers_status(self):
        result = f"You have {len(self.workers)} workers" + '\n'
        keepers = [worker for worker in self.workers if worker.__class__.__name__ == 'Keeper']
        caretakers = [worker for worker in self.workers if worker.__class__.__name__ == 'Caretaker']
        vets = [worker for worker in self.workers if worker.__class__.__name__ == 'Vet']

        result += f"----- {len(keepers)} Keepers:" + '\n'
        for keeper in keepers:
            result += keeper.__repr__() + '\n'

        result += f"----- {len(caretakers)} Caretakers:" + '\n'
        for caretaker in caretakers:
            result += caretaker.__repr__() + '\n'

        result += f"----- {len(vets)} Vets:" + '\n'
        for vet in vets:
            result += vet.__repr__() + '\n'

        return result.strip()


