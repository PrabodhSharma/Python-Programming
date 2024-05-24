
# Global constants for operations
ADD = '+'
SUBTRACT = '-'
MULTIPLY = '*'
DIVIDE = '/'

print("Welcome to the simple calculator")

# Get user inputs for numbers
# Try-except block to handle the case where non-numeric values are entered.
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
except ValueError:
    print("Error: Please enter a valid numeric values")
    exit()

# Get user inputs for operations
operation = input("choose an operation (+, -, *, /): ")

# Function to perform calculation based on operation
def calculate(num1, num2, operation):
    if operation == ADD:
        return num1 + num2
    elif operation ==  SUBTRACT:
        return num1 - num2
    elif operation == MULTIPLY:
        return num1 * num2
    elif operation == DIVIDE:
        if num2 == 0:
            raise ValueError("Error: Cannot divide by zero!")
        return num1 / num2
    else:
        raise ValueError("Invalid Operation.")
    
# Convert user input to constant
if operation in {ADD, SUBTRACT,  MULTIPLY, DIVIDE}:

    # Perform calculation and handle errors
    try:
        result = calculate(num1, num2, operation)
        print(f"The result is: {result:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
else:
    print("Error: Invalid operation.")