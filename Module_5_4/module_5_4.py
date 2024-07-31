class House:
    houses_history = []

    def __new__(cls, *args):
        cls.houses_history.append(args[0])
        return super().__new__(cls)

    def __init__(self, name, abs_floor):
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

    def __del__(self):
        return print(f'{self.name} снесён, но он останется в истории')


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
