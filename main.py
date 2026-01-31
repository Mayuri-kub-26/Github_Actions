# All Arthmetic Operations Module

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
def modulus(a, b):
    return a % b
def power(a, b):
    return a ** b
def floor_divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a // b

def main():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    switch = input("Enter operation (add, subtract, multiply, divide, modulus, power, floor_divide): ")
    if switch == 'add' or switch == '+':
        print("Addition:", add(a, b))
    elif switch == 'subtract' or switch == '-':
        print("Subtraction:", subtract(a, b))
    elif switch == 'multiply' or switch == '*':
        print("Multiplication:", multiply(a, b))
    elif switch == '/':
        print("Division:", divide(a, b))
    elif switch == '%':
        print("Modulus:", modulus(a, b))
    elif switch == '**':
        print("Power:", power(a, b))
    elif switch == '//':
        print("Floor Division:", floor_divide(a, b))
    else:
        print("Invalid operation.")
#print("All Arithmetic Operations Module has successfully implemented.")

if __name__ == "__main__":
    main()