# Original 2D array
matrix = [
  [0, 0, 0, 0, 0],
  [0, 0, 1, 0, 0],
  [0, 1, 1, 1, 0],
  [0, 0, 1, 0, 0],
  [0, 0, 0, 0, 0]
]

# Optimized representation using a dictionary
optimized_matrix = {
    (1, 2): 1,
    (2, 1): 1, (2, 2): 1, (2, 3): 1,
    (3, 2): 1
}

# Function to access elements in the optimized matrix
def get_element(matrix, row, col):
    return matrix.get((row, col), 0)

# Example usage
print(get_element(optimized_matrix, 1, 2))  # Output: 1
print(get_element(optimized_matrix, 0, 0))  # Output: 0
