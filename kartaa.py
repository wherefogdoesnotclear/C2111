class Особа:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        def отримати_вік(self):
            return self._вік

    def інформація(self):
        print(f"Ім'я: {self.name}, Вік: {self.age}")
class Водій(Особа):
    def __init__(self, name, age, номер_посвідчення):
        super().__init__(name, age)
        self.номер_посвідчення = номер_посвідчення

    def інформація(self):
        super().інформація()
        print(f"Номер водійського посвідчення: {self.номер_посвідчення}")
особа1 = Особа("Іван", 30)
водій1 = Водій("Олег", 45, "AB123456")

особа1.інформація()
print()
водій1.інформація()
