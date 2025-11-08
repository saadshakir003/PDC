import multiprocessing
import threading
import time

# ---------- Basic Calculator Functions ----------

def add(a, b):
    time.sleep(1)  # simulate heavy computation
    return a + b

def subtract(a, b):
    time.sleep(1)
    return a - b

def multiply(a, b):
    time.sleep(1)
    return a * b

def divide(a, b):
    time.sleep(1)
    if b == 0:
        return "Error: Division by zero"
    return a / b


# ---------- Sequential Calculator ----------

def sequential_calculator(a, b):
    print("\n=== Sequential Execution ===")
    start_time = time.time()
    results = {
        "Addition": add(a, b),
        "Subtraction": subtract(a, b),
        "Multiplication": multiply(a, b),
        "Division": divide(a, b)
    }
    end_time = time.time()

    for key, value in results.items():
        print(f"{key}: {value}")
    print(f"Sequential Time: {end_time - start_time:.4f} seconds\n")
    return results


# ---------- Multithreading Calculator ----------

def thread_worker(name, func, a, b, results):
    """Thread worker function."""
    results[name] = func(a, b)

def multithreading_calculator(a, b):
    print("=== Multithreading Execution ===")
    start_time = time.time()

    results = {}
    threads = []
    operations = {
        "Addition": add,
        "Subtraction": subtract,
        "Multiplication": multiply,
        "Division": divide
    }

    for name, func in operations.items():
        t = threading.Thread(target=thread_worker, args=(name, func, a, b, results))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    end_time = time.time()
    for key, value in results.items():
        print(f"{key}: {value}")
    print(f"Multithreading Time: {end_time - start_time:.4f} seconds\n")
    return results


# ---------- Multiprocessing Calculator ----------

def run_operation(name, func, a, b):
    return (name, func(a, b))

def multiprocessing_calculator(a, b):
    print("=== Multiprocessing Execution ===")
    start_time = time.time()

    with multiprocessing.Pool(processes=4) as pool:
        results = pool.starmap(run_operation, [
            ("Addition", add, a, b),
            ("Subtraction", subtract, a, b),
            ("Multiplication", multiply, a, b),
            ("Division", divide, a, b)
        ])

    end_time = time.time()
    for name, result in results:
        print(f"{name}: {result}")
    print(f"Multiprocessing Time: {end_time - start_time:.4f} seconds\n")
    return results


# ---------- Main Program ----------

if __name__ == "__main__":
    print("==== Parallel & Distributed Computing: Calculator ====")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    while True:
        print("\nSelect Mode:")
        print("1. Sequential Execution")
        print("2. Multithreading Execution")
        print("3. Multiprocessing Execution")
        print("4. Exit")

        choice = input("Enter choice (1-4): ")

        if choice == "1":
            sequential_calculator(a, b)
        elif choice == "2":
            multithreading_calculator(a, b)
        elif choice == "3":
            multiprocessing_calculator(a, b)
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Try again.")
