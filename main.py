# All Arthmetic Operations Module

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


def show_operations():
    print("\n--- Arithmetic Operations Menu ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

def main():
    while True:
        show_operations()
        choice = input("Select an operation (1-5): ")

        if choice == '5':
            print("Exiting the program.")
            break

        if choice in ['1', '2', '3', '4']:
            try:
                n1 = float(input("Enter first number: "))
                n2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue

            if choice == '1':
                print(f"Result: {add(n1, n2)}")
            elif choice == '2':
                print(f"Result: {subtract(n1, n2)}")
            elif choice == '3':
                print(f"Result: {multiply(n1, n2    )}")
            elif choice == '4':
                print(f"Result: {divide(n1, n2)}")
        else:
            print("Invalid choice. Please select a valid operation.")

if __name__ == "__main__":
    main()