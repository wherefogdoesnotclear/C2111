class Product:
    def __init__(self, name: str, price: float, in_stock: int):
        self.name = name.lower()
        self.price = price
        self.in_stock = in_stock

    def __str__(self):
        return f"{self.name.capitalize()} - {self.price:.2f} грн (в наявності: {self.in_stock})"

class Cart:
    def __init__(self):
        self.items = {}

    def add_product(self, product: 'Product', quantity: int = 1):
        if product.in_stock < quantity:
            print(f"Недостатньо товару '{product.name}' на складі ({product.in_stock} шт).")
            return

        if product in self.items:
            self.items[product] += quantity
        else:
            self.items[product] = quantity
        product.in_stock -= quantity
        print(f"Додано {quantity} × '{product.name}' до кошика.")

    def remove_product(self, product: 'Product', quantity: int = 1):
        if product not in self.items:
            print(f"Товар '{product.name}' відсутній у кошику.")
            return

        if quantity >= self.items[product]:
            removed = self.items.pop(product)
            product.in_stock += removed
            print(f"Усі {removed} × '{product.name}' видалено з кошика.")
        else:
            self.items[product] -= quantity
            product.in_stock += quantity
            print(f"Видалено {quantity} × '{product.name}' з кошика.")

    def total_price(self):
        return sum(product.price * qty for product, qty in self.items.items())

    def show_cart(self):
        if not self.items:
            print("Кошик порожній.")
            return
        print("Вміст кошика:")
        for product, qty in self.items.items():
            print(f"  {product.name.capitalize()} × {qty} = {product.price * qty:.2f} грн")
        print(f"Загальна сума: {self.total_price():.2f} грн")
if __name__ == "__main__":

    products = {
        "яблуко": Product("Яблуко", 12.5, 50),
        "молоко": Product("Молоко", 40.0, 10),
        "хліб": Product("Хліб", 25.0, 20)
    }

    cart = Cart()

    print("=== Онлайн-магазин ===")
    print("Доступні товари:")
    for p in products.values():
        print(" •", p)
    print("\nВведіть команди:")
    print("  додати <назва> <кількість>")
    print("  видалити <назва> <кількість>")
    print("  показати — переглянути кошик")
    print("  вийти — завершити програму")

    while True:
        command = input("\n> ").strip().lower()
        if not command:
            continue

        if command.startswith("додати"):
            parts = command.split()
            if len(parts) != 3:
                print("Формат: додати <назва> <кількість>")
                continue
            name, qty = parts[1], parts[2]
            if name not in products:
                print(f"Товар '{name}' не знайдено.")
                continue
            try:
                qty = int(qty)
            except ValueError:
                print("Кількість має бути числом.")
                continue
            cart.add_product(products[name], qty)

        elif command.startswith("видалити"):
            parts = command.split()
            if len(parts) != 3:
                print("Формат: видалити <назва> <кількість>")
                continue
            name, qty = parts[1], parts[2]
            if name not in products:
                print(f"Товар '{name}' не знайдено.")
                continue
            try:
                qty = int(qty)
            except ValueError:
                print("Кількість має бути числом.")
                continue
            cart.remove_product(products[name], qty)

        elif command == "показати":
            cart.show_cart()

        elif command == "вийти":
            print("Дякуємо за покупки! Гарного дня!")
            break

        else:
            print("Невідома команда. Спробуйте ще раз.")