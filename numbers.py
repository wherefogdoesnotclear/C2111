start = input("Введи початкове число (з): ")
end = input("Введи кінцеве число (по): ")
start = int(start)
end = int(end)

print(f"Числа від {start} до {end}:")
for number in range(start, end + 1):
    print(number)
