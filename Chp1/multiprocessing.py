import multiprocessing
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

# ---------- Multiprocessing Calculator ----------

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

# Helper function for pool
def run_operation(name, func, a, b):
    return (name, func(a, b))

# ---------- Main Program ----------

if __name__ == "__main__":
    print("==== Parallel & Distributed Computing: Calculator ====")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    # Sequential
    sequential_calculator(a, b)

    # Multiprocessing
    multiprocessing_calculator(a, b)
