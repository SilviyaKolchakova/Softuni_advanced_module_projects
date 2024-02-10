class countdown_iterator:
    def __init__(self,count):
        self.count = count
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.count > -1:
            curr = self.count
            self.start += 1
            self.count -= 1
            return curr
        else:
            raise StopIteration()


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")

