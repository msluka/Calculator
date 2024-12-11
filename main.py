# Calculator
import math

def calculator():
    print("Welcome to the Calculator!\n")
    print("Select an operation to perform:\n")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (^)")
    print("6. Square Root (√)")

    try:

        choice = input("Enter the number corresponding to the operation (1/2/3/4/5/6):\n")

        if choice not in ('1', '2', '3', '4', '5', '6'):
            print("Invalid input. Please select a valid operation.")
            return  # Exit the function if an invalid choice is made

        if choice == '6':

            try:
                num = float(input("Enter the number: "))
                if num < 0:
                    print("Error: Cannot calculate the square root of a negative number.")
                else:
                    result = math.sqrt(num)
                    print(f"The square root of {num} is: {result}")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        else:

            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                return  # Exit the function if invalid input is encountered

            if choice == '1':
                result = num1 + num2
                print(f"The result of addition is: {result}")
            elif choice == '2':
                result = num1 - num2
                print(f"The result of subtraction is: {result}")
            elif choice == '3':
                result = num1 * num2
                print(f"The result of multiplication is: {result}")
            elif choice == '4':
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                else:
                    result = num1 / num2
                    print(f"The result of division is: {result}")
            elif choice == '5':
                result = math.pow(num1, num2)
                print(f"The result of {num1} raised to the power of {num2} is: {result}")

    except ValueError:
        print("Invalid input. Please enter numeric values.")

calculator()
