import time
def measure_time(func, *args, **kwargs):
    start = time.time()
    result = func(*args, **kwargs)
    end = time.time()
    elapsed = end - start
    return result, elapsed

def slow_function(n):
    """Імітація повільної операції"""
    total = 0
    for i in range(n):
        total += i ** 2
    return total

def fast_function():
    """Швидка функція"""
    return sum(range(10))

if __name__ == "__main__":
    result, t = measure_time(slow_function, 1_000_000)
    print(f"Результат slow_function: {result}, час: {t:.4f} с")
    result, t = measure_time(fast_function)
    print(f"Результат fast_function: {result}, час: {t:.6f} с")

    _, t_small = measure_time(slow_function, 100_000)
    _, t_big = measure_time(slow_function, 1_000_000)
    print("Перевірка часу:", "✅" if t_big > t_small else "❌", f"({t_small:.4f}s < {t_big:.4f}s)")
