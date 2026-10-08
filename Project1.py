def calcu(num1 ,op ,num2):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operator"
def main():
    print("====Calculator====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice = input("Enter your choice (1/2/3/4): ")
    if choice == '1':
        num1 = float(input("Enter the first number: "))
        op = '+'
    elif choice == '2':
        num1 = float(input("Enter the first number: "))
        op = '-'
    elif choice == '3':
        num1 = float(input("Enter the first number: "))
        op = '*'
    elif choice == '4':
        num1 = float(input("Enter the first number: "))
        op = '/'
    else:
        print("Invalid choice")
        return
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = calcu(num1, op, num2)
    print("Result: ", result)