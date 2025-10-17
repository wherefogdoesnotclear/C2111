import random

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.energy = 100
        self.hunger = 0
        self.mood = 100
        self.health = 100
        self.cleanliness = 100
        self.alive = True

    def _check_alive(self):
        if self.health <= 0 or self.energy <= 0:
            self.alive = False
            print(f"😿 {self.name} дуже ослаб і більше не може рухатися...")
        return self.alive

    def meow(self):
        if not self._check_alive(): return
        print(f"{self.name} каже: Мяу! 😺")
        self.energy -= 5
        self.hunger += 5
        self.mood += 5

    def eat(self):
        if not self._check_alive(): return
        print(f"{self.name} їсть рибку 🍣")
        self.hunger = max(0, self.hunger - 30)
        self.energy = min(100, self.energy + 15)
        self.mood += 10
        self.cleanliness -= 5

    def sleep(self):
        if not self._check_alive(): return
        print(f"{self.name} спить... 😴")
        self.energy = min(100, self.energy + 40)
        self.hunger += 10
        self.mood += 5

    def play(self):
        if not self._check_alive(): return
        print(f"{self.name} грається з клубком ниток 🧶")
        self.energy -= 15
        self.hunger += 10
        self.mood = min(100, self.mood + 20)
        self.cleanliness -= 10

    def wash(self):
        if not self._check_alive(): return
        print(f"{self.name} вилизує себе 🧼")
        self.cleanliness = 100
        self.energy -= 10
        self.mood += 5

    def visit_vet(self):
        if not self._check_alive(): return
        print(f"{self.name} відвідує ветеринара 🩺")
        self.health = min(100, self.health + 40)
        self.mood -= 10
        self.energy -= 10

    def hunt(self):
        if not self._check_alive(): return
        print(f"{self.name} полює на мишку 🐭...")
        success = random.choice([True, False])
        self.energy -= 20
        self.hunger += 15
        if success:
            print(f"{self.name} впіймав мишку! 😼")
            self.hunger = max(0, self.hunger - 40)
            self.mood += 15
        else:
            print(f"{self.name} не зміг нічого зловити 😿")
            self.mood -= 10

    def purr(self):
        if not self._check_alive(): return
        print(f"{self.name} муркоче 💕")
        self.mood = min(100, self.mood + 10)
        self.energy -= 5

    def get_sick(self):
        if not self._check_alive(): return
        print(f"{self.name} захворів 🤒")
        self.health -= 30
        self.mood -= 20

    def status(self):
        print(f"\n--- Стан котика {self.name} ---")
        print(f"Вік: {self.age} років")
        print(f"Енергія: {self.energy}")
        print(f"Голод: {self.hunger}")
        print(f"Настрій: {self.mood}")
        print(f"Здоров’я: {self.health}")
        print(f"Чистота: {self.cleanliness}")
        print(f"Стан: {'живий 🐱' if self.alive else '😿 неактивний'}")
        print("-----------------------------\n")
murko = Cat("Мурко", 3)

murko.status()
murko.play()
murko.eat()
murko.hunt()
murko.wash()
murko.sleep()
murko.purr()
murko.get_sick()
murko.visit_vet()

murko.status()
