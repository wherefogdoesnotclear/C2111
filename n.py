n = input("Введи число n: ")
n = int(n)
even_numbers = [str(i) for i in range(n, 0, -1) if i % 2 == 0]
print(" ".join(even_numbers))
