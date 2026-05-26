import math

def get_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

distance = get_distance(1, 2, 4, 6)
print(distance)  # Output: 5.0