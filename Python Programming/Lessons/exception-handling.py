def divide_by(a, b):
    return a / b


try:
    print(divide_by(40, 0))
except ZeroDivisionError:
    print("You can't divide by zero!")
