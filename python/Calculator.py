from math import sqrt

class Calculator:
    @staticmethod
    def function(num1, operator, num2=None):
        if operator == "addition":
            return num1 + num2
        elif operator == "subtraction":
            return num1 - num2
        elif operator == "multiplication":
            return num1 * num2
        elif operator == "division":
            return num1 / num2
        elif operator == "square":
            return pow(num1, 2)
        elif operator == "squareroot":
            return sqrt(num1)
        else:
            return "Not able to calculate"

# Main program
print("Welcome to the Calculator!")
num1 = float(input("What is your first number? "))

print("\nWhat Mathematical operation do you want to do:\n")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Square")
print("6. SquareRoot")

choice = input("\nEnter the number corresponding to the operation: ").strip()

# Map user choice to operation name
operation_map = {
    "1": "addition",
    "2": "subtraction",
    "3": "multiplication",
    "4": "division",
    "5": "square",
    "6": "squareroot"
}

operator = operation_map.get(choice)
if not operator:
    print("Invalid operation choice.")
else:
    if operator in ["square", "squareroot"]:
        result = Calculator.function(num1, operator)
    else:
        num2 = float(input("What is your second number? "))
        result = Calculator.function(num1, operator, num2)

    print(f"The result of your calculation is: {result}")

