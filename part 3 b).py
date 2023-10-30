def calculate(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operator"

try:
    num1 = int(input("Enter the first integer: "))
    operator = input("Enter an operator (+, -, *, /): ")
    num2 = int(input("Enter the second integer: "))

    result = calculate(num1, operator, num2)
    print("Result: ", result)
except ValueError:
    print("Error: Invalid input. Please enter valid integers.")