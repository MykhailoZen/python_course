# 1) Create a function without arguments that outputs "Hello World!".
#
# 2) Create a function that calculates the area of a rectangle.
# The function should accept the length and width of the rectangle as arguments and return the calculated area.
# Additionally, include a docstring that provides a description of what it does.
# Specific requirements for the exercise:
# Create a function named calculate_rectangle_area that takes two arguments: length and width.
# The function should return the area of the rectangle, which is calculated as multiplication of length and width.
# Include a docstring in the function that provides a description of the function's purpose.
# Test your function by calling it with various inputs and printing the results.
# Solution should include:
# The Python function calculate_rectangle_area with the required functionality and docstring.
# At least three function usage examples demonstrating the use of the function with different inputs and the expected
# output.
import math
from typing import Union


def hello_world() -> None:
    print("Hello World!")


def calculate_rectangle_area(**kwargs: Union[int, float]) -> float:
    """
    Function return the value of area of a rectangle.
    """
    return math.prod(kwargs.values())


if __name__ == "__main__":
    hello_world()
    print(f"The area of a rectangle = {calculate_rectangle_area(length=1.3, width=45)}")
    print(f"The area of a rectangle = {calculate_rectangle_area(length=3, width=4.33)}")
    print(f"The area of a rectangle = {calculate_rectangle_area(length=15, width=7)}")
