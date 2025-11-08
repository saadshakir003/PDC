import multiprocessing
import os
import threading
import time


# --- Calculator Operations ---
def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b if b != 0 else "Undefined"

# --- Task Function for Threads/Processes ---
def do_calculation(a, b, operation, results, index):
    if operation == '1':
        results[index] = add(a, b)
    elif operation == '2':
        results[index] = subtract(a, b)
    elif operation == '3':
        results[index] = multiply(a, b)
    elif operation == '4':
        results[index] = divide(a, b)

# --- Sequential Execution ---
def sequential_mode(a, b, operation):
    start = time.time()
    result = do_calculation(a, b, operation, {}, 0)
    end = time.time()
    print(f"\nSequential execution time: {end - start:.5f} seconds")

# --- Multithreading Execution ---
def multithreading_mode(a, b, operation):
    start = time.time()
    results = [None] * 10
    threads = []
    for i in range(10):
        t = threading.Thread(target=do_calculation, args=(a, b, operation, results, i))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    end = time.time()
    print(f"\nMultithreading execution time: {end - start:.5f} seconds")
    print(f"Results (threads): {results}")

# --- Multiprocessing Execution ---
def multiprocessing_mode(a, b, operation):
    start = time.time()
    with multiprocessing.Manager() as manager:
        results = manager.list([None] * 10)
        processes = []
        for i in range(10):
            p = multiprocessing.Process(target=do_calculation, args=(a, b, operation, results, i))
            processes.append(p)
            p.start()
        for p in processes:
            p.join()
        end = time.time()
        print(f"\nMultiprocessing execution time: {end - start:.5f} seconds")
        print(f"Results (processes): {list(results)}")

# --- Main Menu ---
if __name__ == "__main__":
    print("===== Parallel & Distributed Calculator =====")
    print("Select Operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    operation = input("Enter choice (1/2/3/4): ")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print("\nChoose Execution Mode:")
    print("1. Sequential")
    print("2. Multithreading")
    print("3. Multiprocessing")

    mode = input("Enter choice (1/2/3): ")

    if mode == '1':
        sequential_mode(a, b, operation)
    elif mode == '2':
        multithreading_mode(a, b, operation)
    elif mode == '3':
        multiprocessing_mode(a, b, operation)
    else:
        print("Invalid mode selected!")

    print("\n--- Program Complete ---")
