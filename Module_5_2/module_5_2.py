class House:
    def __init__(self, name='НЕТ ДАННЫХ', abs_floor=1):
        self.name = name
        self.abs_floor = abs_floor

    def __str__(self):
        return f'Название: {self.name}, Количество этажей: {self.abs_floor}'

    def __len__(self):
        return self.abs_floor


h1 = House('ЖК Эльбрус', 50)
h2 = House('ЖК Акация', 20)
h3 = House('Домик в деревне')
h4 = House(abs_floor=5)

# __str__
print(h1)
print(h2)
print(h3)
print(h4)

# __len__
print(len(h1))
print(len(h2))
print(len(h3))
print(len(h4))
