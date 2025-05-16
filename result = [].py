result = []
def divider(a, b):
    if a < b:
        raise ValueError("a is less than b")
    if b > 100:
        raise IndexError("b is too large")
    return a / b
data = {10: 2, 2: 5, "123": 4, 18: 0, "empty": 15, 8: 4}

for key in data:
    try:
        if not isinstance(key, (int, float)):
            raise TypeError(f"Invalid key type: {key}")
        res = divider(key, data[key])
        result.append(res)
    except Exception as e:
        print(f"Error with key={key}, value={data[key]}: {e}")
print(result)