class House:
    def __init__(self, name, num_of_floor):
        self.name = name
        while True:
            if 1 > num_of_floor or num_of_floor > 100:
                print('\033[33mГде вы такой дом нашли? Давайте будем реалистами)))\033[0m')
                num_of_floor = int(input('Введите нужную этажность (\033[31mНЕ БОЛЬШЕ 100 ЭТАЖЕЙ\033[0m): '))
                continue
            else:
                self.num_of_flor = int(num_of_floor)
                break


    # Функция для поиска этажа
    def go_to(self, new_floor):
        draw_list = []
        floor_list = []
        pointer = str(' ')

        # Логика для отрисовки указателя в консоли
        for p in range(1, new_floor + 1):
            if 10 > p == new_floor:
                pointer += str(f'^ - Искомый этаж в здании "{self.name}"')
                break
            elif 100 <= p == new_floor:
                pointer += str(f'^^^ - Искомый этаж в здании "{self.name}"')
                break
            elif 10 <= p == new_floor:
                pointer += str(f'^^ - Искомый этаж в здании "{self.name}"')
                break
            elif p < 10:
                pointer += str('   ')
            elif 10 <= p < 100:
                pointer += str('    ')

        # Логика для отрисовки списка этажей
        for floor in range(1, self.num_of_flor + 1):
            if floor <= new_floor:
                draw_list.append(floor)
            if floor > new_floor:
                floor_list.append(floor)

        # Проверка на поиск несуществующего этажа
        if new_floor > self.num_of_flor:
            print(
                f'\033[31mТакого этажа не существует в здании \033[35m{self.name}\033[31m!!! \nВы не можете подняться на этаж \033[34m{new_floor} \033[31mпри этажности \033[33m{self.num_of_flor}')
        else:
            print('\033[32m', draw_list, '\033[33m', floor_list, '\033[0m', sep='')
            print(pointer)


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
