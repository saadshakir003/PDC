import multiprocessing
from datetime import datetime
from multiprocessing import Barrier, Lock, Process
from time import sleep, time

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


# ---------------------- Multiprocessing Barrier Example ----------------------

def test_with_barrier(synchronizer, serializer):
    name = multiprocessing.current_process().name
    synchronizer.wait()
    now = time()
    with serializer:
        print(f"process {name} ----> {datetime.fromtimestamp(now)}")

def test_without_barrier():
    name = multiprocessing.current_process().name
    now = time()
    print(f"process {name} ----> {datetime.fromtimestamp(now)}")

def multiprocessing_barrier_demo():
    print("\n--- Multiprocessing Barrier & Lock Demo ---")
    synchronizer = Barrier(2)
    serializer = Lock()

    p1 = Process(name='p1 - test_with_barrier', target=test_with_barrier, args=(synchronizer, serializer))
    p2 = Process(name='p2 - test_with_barrier', target=test_with_barrier, args=(synchronizer, serializer))
    p3 = Process(name='p3 - test_without_barrier', target=test_without_barrier)
    p4 = Process(name='p4 - test_without_barrier', target=test_without_barrier)

    p1.start()
    p2.start()
    p3.start()
    p4.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()

    print("All processes completed.\n")


# ---------------------- Main Menu ----------------------

if __name__ == "__main__":
    while True:
        print("\n========== MAIN MENU ==========")
        print("1. Run Calculator")
        print("2. Run Multiprocessing Barrier & Lock Demo")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            calculator()
        elif choice == '2':
            multiprocessing_barrier_demo()
        elif choice == '3':
            print("Exiting program...")
            break
        else:
            print("Invalid input. Please try again.")
