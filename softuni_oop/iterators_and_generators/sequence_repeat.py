from collections import deque


class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.store = []
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.number > 0:
            curr = self.start
            self.store.append(self.sequence[curr])
            self.start += 1
            if self.start == len(self.sequence):
                self.start = 0
            self.number -= 1
            return self.store.pop()
        else:
            raise StopIteration()




result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')
