# 1. Create a function without arguments that outputs "Hello World!".
#
# 2. Create a function that calculates the area of a rectangle.
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


def greetings() -> None:
    """
    This function prints out the greetings.
    @return: print greeting
    """
    print('Hello World!')


def calculate_rectangle_area(length: Union[int, float], width: Union[int, float]) -> Union[int, float]:
    """
    This function calculates the area of a rectangle.
    @param length: the length of the rectangle
    @param width: the width of the rectangle
    @return: calculates the area of a rectangle
    """
    return length * width


if __name__ == "__main__":
    greetings()
    print(f'The result of calculating rectangle area is {calculate_rectangle_area(100, 100)}')
    print(f'The result of calculating rectangle area is {calculate_rectangle_area(12.6, 3.6)}')
    print(f'The result of calculating rectangle area is {calculate_rectangle_area(6, 3.6)}')
