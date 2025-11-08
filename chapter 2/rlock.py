import threading
import time
from threading import RLock


def calculator_operation(a, b, op):
    if op == '+': return a + b
    elif op == '-': return a - b
    elif op == '*': return a * b
    elif op == '/': return a / b if b != 0 else "Division by zero!"
    else: return "Invalid operation"

class Calculator:
    def __init__(self):
        self.lock = RLock()
        self.result = 0

    def execute(self, a, b, op):
        with self.lock:
            self.result = calculator_operation(a, b, op)
            print(f"Result: {self.result}")

def task(calc, a, b, op):
    time.sleep(1)
    calc.execute(a, b, op)

def main():
    print("=== Calculator with RLock Synchronization ===")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    op = input("Enter operation (+, -, *, /): ")

    calc = Calculator()
    t1 = threading.Thread(target=task, args=(calc, a, b, op))
    t2 = threading.Thread(target=task, args=(calc, a, b, op))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

if __name__ == "__main__":
    main()
