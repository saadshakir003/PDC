import random
import threading
import time
from queue import Queue

# ---------------- CALCULATOR CODE ----------------

def calculator():
    print("\n--- Simple Calculator ---")
    print("Operations: +, -, *, /")
    while True:
        try:
            num1 = float(input("Enter first number: "))
            op = input("Enter operation (+, -, *, /): ").strip()
            num2 = float(input("Enter second number: "))

            if op == '+':
                print(f"Result: {num1 + num2}")
            elif op == '-':
                print(f"Result: {num1 - num2}")
            elif op == '*':
                print(f"Result: {num1 * num2}")
            elif op == '/':
                if num2 == 0:
                    print("Error: Division by zero!")
                else:
                    print(f"Result: {num1 / num2}")
            else:
                print("Invalid operation!")

            cont = input("Do you want to continue? (y/n): ").lower()
            if cont != 'y':
                break

        except ValueError:
            print("Invalid input! Please enter numeric values.")

# ---------------- THREAD SYNCHRONIZATION WITH QUEUE ----------------

class Producer(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        for i in range(5):
            item = random.randint(0, 256)
            self.queue.put(item)
            print(f'Producer notify: item {item} appended to queue by {self.name}\n')
            time.sleep(1)


class Consumer(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            item = self.queue.get()
            print(f'Consumer notify: {item} popped from queue by {self.name}')
            self.queue.task_done()

# ---------------- MAIN ----------------

if __name__ == "__main__":
    print("1. Run Calculator")
    print("2. Run Thread Synchronization with Queue")
    choice = input("Choose an option (1/2): ").strip()

    if choice == '1':
        calculator()

    elif choice == '2':
        queue = Queue()
        t1 = Producer(queue)
        t2 = Consumer(queue)
        t3 = Consumer(queue)
        t4 = Consumer(queue)

        t1.start()
        t2.start()
        t3.start()
        t4.start()

        t1.join()
        t2.join()
        t3.join()
        t4.join()
    else:
        print("Invalid choice!")
