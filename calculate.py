def safe_calculator(func):
    def wrapper(expression):
        try:
            result = func(expression)
            return result
        except Exception as e:
            return f"Помилка при обчисленні: {e}"
    return wrapper
def calculate(expression):
    return eval(expression)
