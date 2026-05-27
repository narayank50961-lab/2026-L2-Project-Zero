def calculate_gradient(point1, point2):
    x1, y1 = point1
    x2, y2 = point2

    # Check if the line is vertical to avoid division by zero
    if x2 == x1:
        raise ValueError("Gradient is undefined (vertical line).")

    gradient = (y2 - y1) / (x2 - x1)
    return gradient


# Example usage:
# Point 1: (1, 2), Point 2: (3, 8)
m = calculate_gradient((1, 2), (3, 8))
print(f"The gradient is: {m}")  # Output: 3.0