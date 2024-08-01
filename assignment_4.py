import math

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# Prompt the user for coordinates
x1 = get_float_input("Please enter the x-coordinate of the first point: ")
y1 = get_float_input("Please enter the y-coordinate of the first point: ")
x2 = get_float_input("Please enter the x-coordinate of the second point: ")
y2 = get_float_input("Please enter the y-coordinate of the second point: ")

# Calculate the distance
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Display the result
print(f"The distance between the two points is {distance:.2f}.")
