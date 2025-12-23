#!/bin/python3
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /):")
result = 0

match operation:
    case '+':
        result = num1 + num2
    case '-':
        result = num1 - num2
    case '*':
        result = num1 * num2
    case '/':
        if num2 > 0:
            result = num1 / num2
        elif num2 == 0:
            print("Cannot divide by zero")

if result > 0:
    print(f"The result is {result}")
