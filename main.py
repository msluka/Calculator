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

    finish = False

    def check_if_numeric(prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Invalid input.")

    def check_if_in_range():
        while True:
            try:
                chosen_num = str(int(check_if_numeric("Enter the number corresponding to the operation (1/2/3/4/5/6):\n")))
                if chosen_num in ('1', '2', '3', '4', '5', '6'):
                    return chosen_num
            except ValueError:
                print("Invalid input")

    def continue_or_exit():
        global finish
        user_decision = input("Do you want to exit? Type 'yes' to exit, or press any other key to continue.")
        if user_decision.lower() == "yes":
            finish = True
        else:
            finish = False

    while not finish:

        choice = check_if_in_range()

        if choice == '6':
            try:
                num = check_if_numeric("Enter the number: ")
                if num < 0:
                    print("Error: Cannot calculate the square root of a negative number.")
                else:
                    result = math.sqrt(num)
                    print(f"The square root of {num} is: {result}")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

            continue_or_exit()
        else:
            try:
                num1 = float(check_if_numeric("Enter the first number: "))
                num2 = float(check_if_numeric("Enter the second number: "))
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

            continue_or_exit()

calculator()
