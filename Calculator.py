# -------------------------------
# Calculator App
# -------------------------------

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a / b


# Main calculator loop
def calculator():
    print("\n=== Welcome to CLI Calculator ===")

    while True:
        print("\nChoose an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")

        # Exit condition
        if choice == '5':
            print("Exiting the calculator. Goodbye! 👋")
            break

        # Validate input
        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice. Please enter a number between 1 and 5.")
            continue

        # user input for numbers
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values only.")
            continue

        # calculation based on choice
        if choice == '1':
            result = add(num1, num2)
            symbol = '+'
        elif choice == '2':
            result = subtract(num1, num2)
            symbol = '-'
        elif choice == '3':
            result = multiply(num1, num2)
            symbol = '*'
        elif choice == '4':
            result = divide(num1, num2)
            symbol = '/'

        print(f"\nResult: {num1} {symbol} {num2} = {result}")

# Run calculator
if __name__ == "__main__":
    calculator()
