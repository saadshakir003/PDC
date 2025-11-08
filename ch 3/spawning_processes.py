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


# ---------------------- Multiprocessing Example 1 ----------------------

def foo():
    name = multiprocessing.current_process().name
    print(f"Starting {name}\n")
    if name == 'background_process':
        for i in range(0, 5):
            print(f'---> {i}\n')
        time.sleep(1)
    else:
        for i in range(5, 10):
            print(f'---> {i}\n')
        time.sleep(1)
    print(f"Exiting {name}\n")

def multiprocessing_demo():
    print("\n--- Multiprocessing Demo (Non-Daemon Processes) ---")

    background_process = multiprocessing.Process(
        name='background_process',
        target=foo
    )
    background_process.daemon = False

    no_background_process = multiprocessing.Process(
        name='NO_background_process',
        target=foo
    )
    no_background_process.daemon = False

    background_process.start()
    no_background_process.start()

    background_process.join()
    no_background_process.join()
    print("Both processes completed.\n")


# ---------------------- Multiprocessing Example 2: Spawn a Process ----------------------

def myFunc(i):
    print(f'Calling myFunc from process n°: {i}')
    for j in range(0, i):
        print(f'Output from myFunc is : {j}')
    return

def spawn_process_demo():
    print("\n--- Spawn a Process (Process Based Parallelism) ---")
    for i in range(6):
        process = multiprocessing.Process(target=myFunc, args=(i,))
        process.start()
        process.join()
    print("All spawned processes completed.\n")


# ---------------------- Main Menu ----------------------

if __name__ == "__main__":
    while True:
        print("\n========== MAIN MENU ==========")
        print("1. Run Calculator")
        print("2. Run Multiprocessing Demo (Non-Daemon)")
        print("3. Run Spawn Process Demo (Chapter 3)")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            calculator()
        elif choice == '2':
            multiprocessing_demo()
        elif choice == '3':
            spawn_process_demo()
        elif choice == '4':
            print("Exiting program...")
            break
        else:
            print("Invalid input. Please try again.")
