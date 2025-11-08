import multiprocessing
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


# ---------------------- Multiprocessing Example: Process Termination ----------------------

def foo():
    print('Starting function')
    for i in range(0, 10):
        print(f'-->{i}\n')
        time.sleep(1)
    print('Finished function')

def process_termination_demo():
    print("\n--- Multiprocessing: Process Termination Example ---")
    p = multiprocessing.Process(target=foo)
    print('Process before execution:', p, p.is_alive())
    p.start()
    print('Process running:', p, p.is_alive())
    p.terminate()
    print('Process terminated:', p, p.is_alive())
    p.join()
    print('Process joined:', p, p.is_alive())
    print('Process exit code:', p.exitcode)
    print("Process Termination Demo Completed.\n")


# ---------------------- Main Menu ----------------------

if __name__ == "__main__":
    while True:
        print("\n========== MAIN MENU ==========")
        print("1. Run Calculator")
        print("2. Run Process Termination Demo")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            calculator()
        elif choice == '2':
            process_termination_demo()
        elif choice == '3':
            print("Exiting program...")
            break
        else:
            print("Invalid input. Please try again.")
