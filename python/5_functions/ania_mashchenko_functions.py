# Create a function without arguments that outputs "Hello World!".
#  Create a function that calculates the area of a rectangle.
# The function should accept the length and width of the rectangle as arguments and return the calculated area.
# Additionally, include a docstring that provides a description of what it does.
# Specific requirements for the exercise:
# Create a function named calculate_rectangle_area that takes two arguments: length and width.
# The function should return the area of the rectangle, which is calculated as multiplication of length and width.
# Include a docstring in the function that provides a description of the function's purpose.
# Test your function by calling it with various inputs and printing the results.
# Solution should include:
# The Python function calculate_rectangle_area with the required functionality and docstring.
# At least three function usage examples demonstrating the use of the function with different inputs and the expected output.
from typing import Union


def print_hello():
    """
    This function prints "Hello world!"
    """
    print("Hello world!")


def calculate_rectangle_area(length: Union[int, float] = 2, width: Union[int, float] = 5) -> Union[int, float]:
    """
    Function return the area of the rectangle,which is calculated as multiplication of length and width.
    :param length: length of rectangle
    :param width:width of rectangle
    :return: rectangle area
    """
    return length * width


if __name__ == "__main__":
    print_hello()
    print(f"this is the area of rectangle: {calculate_rectangle_area(5, 2)}")
    print(f"this is the area of rectangle: {calculate_rectangle_area(6.2, 3.4)}")
    print(f"this is the area of rectangle: {calculate_rectangle_area()}")
