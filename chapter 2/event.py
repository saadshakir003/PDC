import logging
import random
import threading
import time

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(threadName)-17s %(message)s')

event = threading.Event()
result = None

def calculator_operation(a, b, op):
    if op == '+': return a + b
    elif op == '-': return a - b
    elif op == '*': return a * b
    elif op == '/': return a / b if b != 0 else "Division by zero!"
    else: return "Invalid operation"

def producer(a, b, op):
    global result
    time.sleep(2)
    result = calculator_operation(a, b, op)
    logging.info(f"Producer calculated: {a} {op} {b} = {result}")
    event.set()

def consumer():
    logging.info("Consumer waiting for result...")
    event.wait()
    logging.info(f"Consumer got result: {result}")

def main():
    print("=== Calculator with Event Synchronization ===")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    op = input("Enter operation (+, -, *, /): ")

    t1 = threading.Thread(target=consumer)
    t2 = threading.Thread(target=producer, args=(a, b, op))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

if __name__ == "__main__":
    main()
