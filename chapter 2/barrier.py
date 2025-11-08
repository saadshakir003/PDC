import random
import threading
import time
from threading import Barrier


def calculator_operation(a, b, op):
    if op == '+': return a + b
    elif op == '-': return a - b
    elif op == '*': return a * b
    elif op == '/': return a / b if b != 0 else "Division by zero!"
    else: return "Invalid operation"

def runner(barrier, a, b, op, name):
    time.sleep(random.randint(1, 3))
    print(f"{name} reached the barrier.")
    barrier.wait()
    print(f"{name} performing calculation: {a} {op} {b}")
    print(f"{name} result: {calculator_operation(a, b, op)}")

def main():
    print("=== Calculator with Barrier Synchronization ===")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    op = input("Enter operation (+, -, *, /): ")

    barrier = Barrier(3)
    runners = ['Thread-1', 'Thread-2', 'Thread-3']

    threads = [threading.Thread(target=runner, args=(barrier, a, b, op, r)) for r in runners]
    for t in threads: t.start()
    for t in threads: t.join()
    print("All threads completed after barrier.")

if __name__ == "__main__":
    main()
