import multiprocessing
import random
import time

# ---------------------- Calculator Section ----------------------

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply_calc(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

def calculator():
    print("\n--- Simple Calculator ---")
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter choice (1/2/3/4): ")

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    if choice == '1':
        print(f"The result is: {add(num1, num2)}")
    elif choice == '2':
        print(f"The result is: {subtract(num1, num2)}")
    elif choice == '3':
        print(f"The result is: {multiply_calc(num1, num2)}")
    elif choice == '4':
        print(f"The result is: {divide(num1, num2)}")
    else:
        print("Invalid choice! Please select from 1 to 4.")


# ---------------------- Multiprocessing: Process Name Example ----------------------

def myFunc():
    name = multiprocessing.current_process().name
    print(f"Starting process name = {name}\n")
    time.sleep(3)
    print(f"Exiting process name = {name}\n")

def multiprocessing_process_demo():
    print("\n--- Multiprocessing Process Name Demo ---")

    process_with_name = multiprocessing.Process(
        name='myFunc process',
        target=myFunc
    )

    process_with_default_name = multiprocessing.Process(
        target=myFunc
    )

    process_with_name.start()
    process_with_default_name.start()

    process_with_name.join()
    process_with_default_name.join()

    print("Both processes finished execution.")


# ---------------------- Main Menu ----------------------

if __name__ == "__main__":
    while True:
        print("\n========== MAIN MENU ==========")
        print("1. Run Calculator")
        print("2. Run Multiprocessing Process Name Demo")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            calculator()
        elif choice == '2':
            multiprocessing_process_demo()
        elif choice == '3':
            print("Exiting program...")
            break
        else:
            print("Invalid input. Please try again.")
