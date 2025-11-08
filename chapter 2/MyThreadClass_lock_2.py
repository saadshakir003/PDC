import os
import threading
import time
from random import randint
from threading import Thread


# ------------------- Calculator -------------------
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b


# ------------------- Thread with Lock (Version 2) -------------------
threadLock = threading.Lock()

class MyThreadClass(Thread):
    def __init__(self, name, duration):
        Thread.__init__(self)
        self.name = name
        self.duration = duration

    def run(self):
        # Acquire the Lock
        threadLock.acquire()
        print(f"---> {self.name} running, belonging to process ID {os.getpid()}")
        # Release the Lock early to allow others to proceed
        threadLock.release()

        time.sleep(self.duration)
        print(f"---> {self.name} over\n")


# ------------------- Main Program -------------------
def main():
    calc = Calculator()

    print("\n===== CALCULATOR + THREAD LOCK (VERSION 2) DEMO =====\n")

    # Perform calculator operation
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Enter operation (+, -, *, /): ")

    if op == '+':
        print("Result:", calc.add(a, b))
    elif op == '-':
        print("Result:", calc.subtract(a, b))
    elif op == '*':
        print("Result:", calc.multiply(a, b))
    elif op == '/':
        print("Result:", calc.divide(a, b))
    else:
        print("Invalid operation!")

    print("\nNow demonstrating threads with early LOCK release...\n")

    start_time = time.time()

    # Create multiple threads
    threads = [
        MyThreadClass(f"Thread#{i+1}", randint(1, 5)) for i in range(5)
    ]

    # Start all threads
    for t in threads:
        t.start()

    # Wait for all threads to complete
    for t in threads:
        t.join()

    print("All threads completed!")
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()
