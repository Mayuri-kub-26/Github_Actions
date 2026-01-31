from calculator import add, subtract, multiply, divide

def show_menu():
    print("\n--- Arithmetic Operations Menu ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

def main():
    while True:
        show_menu()
        choice = input("Select an operation (1-5): ")

        if choice == "5":
            print("Exiting the calculator. Goodbye!")
            break

        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == "1":
            print("Result:", add(a, b))
        elif choice == "2":
            print("Result:", subtract(a, b))
        elif choice == "3":
            print("Result:", multiply(a, b))
        elif choice == "4":
            try:
                print("Result:", divide(a, b))
            except ValueError as e:
                print("Error:", e)
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()