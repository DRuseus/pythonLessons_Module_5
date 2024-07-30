class House:
    def __init__(self, name='НЕТ ДАННЫХ', abs_floor=1):
        self.name = name
        self.abs_floor = abs_floor

    def __len__(self):
        return self.abs_floor

    def __str__(self):
        return f'Название: {self.name}, Количество этажей: {self.abs_floor}'

    def __eq__(self, other):
        return self.abs_floor == other.abs_floor

    def __lt__(self, other):
        return self.abs_floor < other.abs_floor

    def __le__(self, other):
        return self.abs_floor <= other.abs_floor

    def __gt__(self, other):
        return self.abs_floor > other.abs_floor

    def __ge__(self, other):
        return self.abs_floor >= other.abs_floor

    def __add__(self, other):
        if isinstance(other, int):
            self.abs_floor = self.abs_floor + other
        return self

    def __iadd__(self, other):
        if isinstance(other, int):
            self.abs_floor += other
        return self

    def __radd__(self, other):
        if isinstance(other, int):
            self.abs_floor = other + self.abs_floor
        return self


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
h3 = House('Домик в деревне')

print(h1)
print(h2)

#print(h1 == h2)  # __eq__

h1 = h1 + 10  # __add__
print(h1)
print(h1 == h2)

h1 += 10  # __iadd__
print(h1)

h2 = 10 + h2  # __radd__
print(h2)

print(h1 > h2)  # __gt__
print(h1 >= h2)  # __ge__
print(h1 < h2)  # __lt__
print(h1 <= h2)  # __le__
print(h1 != h2)  # __ne__"""
