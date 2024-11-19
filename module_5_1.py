class House:

    def __init__(self, name, number_of_floors): # инициализатор
        self.name = name # переменная, указывающая на объект
        self.number_of_floors = number_of_floors # переменная, указывающая на объект

    def go_to(self, new_floor):
        if 0 < new_floor <= self.number_of_floors: # проверяем этаж
            for floor in range(1, new_floor + 1): # последовательность чисел от 1 до new_floor
                print(floor)
        else:
            print("Такого этаже не существует")

House('ЖК Эльбрус', 30)
h1 = House('ЖК Горский, дом',  18)
h2 = House('Домик в деревне, дом', 2)
#print(h1.name, h1.number_of_floors)
#print(h2.name, h2.number_of_floors)
h1.go_to(5)
h2.go_to(10)
