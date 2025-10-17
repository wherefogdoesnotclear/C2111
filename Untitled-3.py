class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.energy = 100
        self.hunger = 0
        self.mood = 100

    def meow(self):
        print(f"{self.name} каже: Мяу!")
        self.energy -= 5
        self.hunger += 5
        self.mood += 5

    def eat(self):
        print(f"{self.name} їсть смачну рибку 🍣")
        self.hunger = max(0, self.hunger - 20)
        self.energy += 10

    def sleep(self):
        print(f"{self.name} спить... 😴")
        self.energy = min(100, self.energy + 30)
        self.hunger += 10

    def play(self):
        print(f"{self.name} грається з клубком ниток 🧶")
        self.mood = min(100, self.mood + 10)
        self.energy -= 10
        self.hunger += 5

    def status(self):
        print(f"--- Стан котика {self.name} ---")
        print(f"Вік: {self.age}")
        print(f"Енергія: {self.energy}")
        print(f"Голод: {self.hunger}")
        print(f"Настрій: {self.mood}")
        print("-----------------------------")
murko = Cat("Мурко", 2)
murko.status()
murko.play()
murko.eat()
murko.sleep()
murko.status()