def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

result_add = add(10, 5)
print(f"Addition Result: {result_add}")

result_subtract = subtract(10, 5)
print(f"Subtraction Result: {result_subtract}")

result_multiply = multiply(10, 5)
print(f"Multiplication Result: {result_multiply}")


result_divide = divide(result_add, 0)
print(f"Division Result: {result_divide}")


