def find_midpoint(x1, y1, x2, y2):
    mid_x = (x1 + x2) / 2
    mid_y = (y1 + y2) / 2
    return (mid_x, mid_y)

# Example usage:
point1 = (0, 0)
point2 = (4, 6)
print("Midpoint:", find_midpoint(point1[0], point1[1], point2[0], point2[1]))