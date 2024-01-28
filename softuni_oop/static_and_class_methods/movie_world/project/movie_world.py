class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):
        target_customer = [c for c in self.customers if c.id == customer_id][0]
        dvd = [d for d in self.dvds if d.id == dvd_id][0]
        already_rented = [d for d in target_customer.rented_dvds if d.id == dvd_id]
        if len(already_rented) > 0:
            return f"{target_customer.name} has already rented {dvd.name}"
        if dvd.is_rented:
            return "DVD is already rented"

        if target_customer.age < dvd.age_restriction:
            return f"{target_customer.name} should be at least {dvd.age_restriction} to rent this movie"

        else:
            target_customer.rented_dvds.append(dvd)
            dvd.is_rented = True
            return f"{target_customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        target_customer = [c for c in self.customers if c.id == customer_id][0]
        dvd = [d for d in self.dvds if d.id == dvd_id][0]
        already_rented = [d for d in target_customer.rented_dvds if d.id == dvd_id]
        if len(already_rented) > 0:
            target_customer.rented_dvds.remove(dvd)
            dvd.is_rented = False
            return f"{target_customer.name} has successfully returned {dvd.name}"

        return f"{target_customer.name} does not have that DVD"

    def __repr__(self):
        result = ''
        for customer in self.customers:
            result += f"{customer}" '\n'
            # result += '\n'

        for dvd in self.dvds:
            result += f"{dvd}" '\n'

        return result


