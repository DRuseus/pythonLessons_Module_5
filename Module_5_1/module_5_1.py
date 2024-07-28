class House:
    def __init__(self, name, num_of_floor):
        self.name = name
        while True:
            if 1 > num_of_floor or num_of_floor > 999:
                print('\033[31mТакой этажности быть не может!!!\033[0m')
                num_of_floor = int(input('Введите нужную этажность: '))
                continue
            else:
                self.num_of_flor = int(num_of_floor)
                break

    def go_to(self, new_floor):
        draw_list = []
        pointer = str(' ')

        for p in range(1, new_floor + 1):
            if 10 > p == new_floor:
                pointer += str('^ - Искомый этаж')
                break
            elif 100 <= p == new_floor:
                pointer += str('^^^ - Искомый этаж')
                break
            elif 10 <= p == new_floor:
                pointer += str('^^ - Искомый этаж')
                break
            elif p < 10:
                pointer += str('   ')
            elif 10 <= p < 100:
                pointer += str('    ')

        for floor in range(1, new_floor + 1):
            draw_list.append(floor)

        if new_floor > self.num_of_flor:
            print(
                f'\033[31mТакого этажа не существует!!! \nВы не можете подняться на этаж \033[34m{new_floor} \033[31mпри этажности \033[33m{self.num_of_flor}')
        else:
            print(draw_list)
            print(pointer)
        return new_floor


elb = House('Elbrus', 30)
elb.go_to(9)
