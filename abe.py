a = input("Введи перше число : ")
b = input("Введи друге число : ")
a = float(a)
b = float(b)
operation = input("Введи дію (+, -, *, /): ")
if operation == "+":
    result = a + b
    print(f"Результат: {result}")
elif operation == "-":
    result = a - b
    print(f"Результат: {result}")
elif operation == "*":
    result = a * b
    print(f"Результат: {result}")
elif operation == "/":
    if b == 0:
        print("Помилка: ділення на нуль!")
    else:
        result = a / b
        print(f"Результат: {result}")
else:
    print("Невідома операція. Використовуй тільки +, -, *, /.")
