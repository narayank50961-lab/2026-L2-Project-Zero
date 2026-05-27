import numpy as np

# 1D array of values
f = np.array([0, 1, 4, 9, 16])

# Calculate the gradient
gradient_values = np.gradient(f)

print(gradient_values)
# Output: [1. 2. 3. 4. 5.]