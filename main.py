import numpy as np
import time

# Create a list and a NumPy array with 1 million numbers
size = 1_000_000
python_list = list(range(size))
numpy_array = np.arange(size)

# Squaring with Python list (using list comprehension)
start_time = time.time()
python_list_squared = [x**2 for x in python_list]
end_time = time.time()
python_list_time = end_time - start_time

# Squaring with NumPy array (vectorized operation)
start_time = time.time()
numpy_array_squared = numpy_array ** 2
end_time = time.time()
numpy_time = end_time - start_time

# Print results
print(f"Python List Time: {python_list_time:.6f} seconds")
print(f"NumPy Array Time: {numpy_time:.6f} seconds")
print(f"NumPy is {python_list_time / numpy_time:.2f} times faster!")

# NumPy is faster because it uses optimized C-based operations,
# vectorization, and contiguous memory storage, reducing Python's
# loop overhead and enabling efficient parallel computation.

matrix = np.array([
    [1,2,3,4]
    ,[5,6,7,8]
    ,[9,10,11,12]
    ,[13,14,15,16]
])

print("Matrix:\n", matrix)
print("Shape:", matrix.shape)   # (rows, columns)
print("Size:", matrix.size)     # Total number of elements
print("Dimensions:", matrix.ndim)  # Number of dimensions (2D, 3D, etc.)

identity_matrix = np.eye(3)
print("\n3x3 identity matrix matrix: \n", identity_matrix)

random_array = np.random.randint(1,101, size = 20)
print("\n1D Array of 20 Random Integers:\n", random_array)


matrix1 = np.arange(1,26).reshape(5,5)
third_row = matrix[2, :]
print("\nThird Row:", third_row)

# Extract the last two columns
last_two_columns = matrix[:, -2:]
print("\nLast Two Columns:\n", last_two_columns)

# Extract a 3x3 submatrix from the center
center_3x3_submatrix = matrix[1:4, 1:4]
print("\n3x3 Center Submatrix:\n", center_3x3_submatrix)

matrix2 = np.arange(1,21)
print("\n" , matrix2)
matrix3 = matrix2.reshape(4,5)
print("\n" , matrix3)
