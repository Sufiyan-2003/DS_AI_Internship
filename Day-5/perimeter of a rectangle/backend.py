def calc_rectangle(length, width):
    """Calculate area and perimeter of a rectangle."""
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

print("Rectangle Calculator")
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

area, perimeter = calc_rectangle(length, width)

print(f"Area: {area}, Perimeter: {perimeter}")