import math
import random

def calculate_area(shape, **kwargs):
    """
    Calculates the area of a given shape.

    Args:
        shape (str): The type of shape ("circle" or "rectangle").
        **kwargs:
            For "circle": radius (float)
            For "rectangle": width (float), height (float)

    Returns:
        float: The calculated area of the shape. Returns 0 if the shape is not recognized.
    """
    if shape == "circle":
        # Calculate area of a circle: pi * r^2
        return math.pi * kwargs["radius"] ** 2
    elif shape == "rectangle":
        # Calculate area of a rectangle: width * height
        return kwargs["width"] * kwargs["height"]
    else:
        # Return 0 for unsupported shapes
        return 0


# create a function that divides two numbers
def divide_numbers(a, b):
    """
    Divides two numbers.

    Args:
        a (float): The numerator.
        b (float): The denominator.

    Returns:
        float: The result of the division.

    Raises:
        ZeroDivisionError: If the denominator 'b' is zero.
    """
    return a / b

#create a function that processes a list of numbers
def process_list(items):
    """
    Processes a list of numbers by doubling each item and summing them up.

    Args:
        items (list): A list of numbers (integers or floats).

    Returns:
        float: The sum of all doubled items in the list.
    """
    total = 0
    # Iterate through the list, double each item, and add to total
    for i in range(len(items)):
        total += items[i] * 2
    return total

#create a class that performs basic arithmetic operations
class Calculator:
    """
    A simple calculator class that performs basic arithmetic operations
    and keeps a history of additions.
    """
    def __init__(self):
        """
        Initializes the Calculator with an empty history list.
        """
        self.history = []  # Stores a log of addition operations

    def add(self, a, b):
        """
        Adds two numbers and records the operation in the history.

        Args:
            a (float): The first number.
            b (float): The second number.

        Returns:
            float: The sum of 'a' and 'b'.
        """
        result = a + b
        # Log the addition operation to the history
        self.history.append(f"{a} + {b} = {result}")
        return result

    def divide(self, a, b):
        """
        Divides two numbers using the external divide_numbers function.

        Args:
            a (float): The numerator.
            b (float): The denominator.

        Returns:
            float: The result of the division.

        Raises:
            ZeroDivisionError: If the denominator 'b' is zero.
        """
        # Delegates the division to the standalone function
        return divide_numbers(a, b)

# --- Example Usage ---

# Create an instance of the Calculator class
calc = Calculator()

# Perform an addition operation
result = calc.add(5, 3)

# Calculate the area of a circle
area = calculate_area("circle", radius=5)

# Perform a division operation using the calculator instance
division = calc.divide(10, 2)

# Define a list of numbers for processing
items = [1, 2, 3, 4]
# Process the list
processed = process_list(items)

# Print all calculated results
print(f"Results: {result}, {area:.2f}, {division}, {processed}")