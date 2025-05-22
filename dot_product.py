import time
import numpy as np
import csv
    
def load_csv(file_name):
    """Loads a CSV file into a Python list, skipping the header."""
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        return [float(row[0]) for row in reader]  # Convert remaining values to float

# Load x values from L1.csv and Q1.csv
x_L1 = load_csv("L1.csv")
x_Q1 = load_csv("Q1.csv")

# Python loop-based element-wise multiplication
start_time = time.time()
dot_product_python = sum(x_L1[i] * x_Q1[i] for i in range(len(x_L1)))
time_python = time.time() - start_time

print(f"Python loop-based dot product: {dot_product_python:.5f}")
print(f"Time taken (Python loop): {time_python:.5f} seconds\n")

# NumPy-based dot product
x_L1_np = np.array(x_L1)
x_Q1_np = np.array(x_Q1)

start_time = time.time()
dot_product_numpy = np.dot(x_L1_np, x_Q1_np)
time_numpy = time.time() - start_time

print(f"NumPy dot product: {dot_product_numpy:.5f}")
print(f"Time taken (NumPy): {time_numpy:.5f} seconds\n")

# Load Q2.csv and compute its square
x_Q2 = load_csv("Q2.csv")
x_Q2_np = np.array(x_Q2)

# Python loop-based square
start_time = time.time()
x_Q2_squared_python = [x ** 2 for x in x_Q2]
time_python_square = time.time() - start_time

print(f"Time taken (Python loop, square): {time_python_square:.5f} seconds")

# NumPy-based square
start_time = time.time()
x_Q2_squared_numpy = np.square(x_Q2_np)
time_numpy_square = time.time() - start_time

print(f"Time taken (NumPy, square): {time_numpy_square:.5f} seconds")
