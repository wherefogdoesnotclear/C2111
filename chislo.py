import random
secret_number = random.randint(1, 10)
attempts = 3
print("Я загадав число від 1 до 10. Спробуй вгадати його!")
for attempt in range(1, attempts + 1):
    guess = input(f"Спроба {attempt}: Введи своє число: ")
    guess = int(guess)

    if guess == secret_number:
        print("Вітаю! Ти вгадав число!")
        break
    elif guess < secret_number:
        print("Більше.")
    else:
        print("Менше.")

else:
    print(f"На жаль, ти не вгадав. Загадане число було {secret_number}.")
