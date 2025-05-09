class Тварина:
    def __init__(self, name, age, лапи=4, має_хвіст=True, має_вуха=True):
        self.name = name
        self.age = age
        self.лапи = лапи
        self.має_хвіст = має_хвіст
        self.має_вуха = має_вуха

    def подай_звук(self):
        print("Тварина видає звук")

    def інформація(self):
        print(f"Ім'я: {self.name}, Вік: {self.age}, Лапи: {self.лапи}, Хвіст: {self.має_хвіст}, Вуха: {self.має_вуха}")
class Собака(Тварина):
    def __init__(self, name, age):
        super().__init__(name, age, лапи=4, має_хвіст=True, має_вуха=True)

    def подай_звук(self):
        print("Гав-гав!")
class Кіт(Тварина):
    def __init__(self, name, age):
        super().__init__(name, age, лапи=4, має_хвіст=True, має_вуха=True)

    def подай_звук(self):
        print("Мяу!")
тварина1 = Собака("Барсик", 4)
тварина2 = Кіт("Сніжок", 2)

тварина1.інформація()
тварина1.подай_звук()

тварина2.інформація()
тварина2.подай_звук()

