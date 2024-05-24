# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero!"
    return x / y

# Main function to run the calculator
def calculator():
    print("Welcome to the Basic Calculator!")

    # Input first number
    num1 = float(input("Enter the first number: "))

    # Input second number
    num2 = float(input("Enter the second number: "))
    
    # Display operation options
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    # Input operation choice
    choice = input("Enter choice (1/2/3/4): ")

    # Perform selected operation
    if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        result = divide(num1, num2)
        if isinstance(result, str):
            print(result)
        else:
            print(f"{num1} / {num2} = {result}")
    else:
        print("Invalid choice. Please choose a valid operation.")

# Run the calculator
calculator()
