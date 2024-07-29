class House:
    def __init__(self, name, abs_floor):
        self.name = name
        self.abs_floor = abs_floor

    def __str__(self):
        return f'Название: {self.name}, Количество этажей: {self.abs_floor}'

    def __len__(self):
        return self.abs_floor


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))
