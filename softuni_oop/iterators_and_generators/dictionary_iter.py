class dictionary_iter:
    def __init__(self, dict_obj):
        self.dict_obj = dict_obj
        self.list_obj = [(k, v) for k, v in self.dict_obj.items()]
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.counter < len(self.list_obj):
            curr = self.counter
            self.counter += 1
            return self.list_obj[curr]
        else:
            raise StopIteration()


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

