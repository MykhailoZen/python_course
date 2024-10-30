from typing import Union


def print_func():
    """
    Function prints "Hello World"
    """
    print("Hello World")


def calculate_rectangle_area(length: Union[int, float] = 4.0, width: Union[int, float] = 2.0):
    """
    Function calculates the area of a rectangle.
    The function should accept the length and width of the rectangle as arguments and return the calculated area.
    @param length: The length of the rectangle.
    @param width: The width of the rectangle.
    """
    print(f"The area of the {length} x {width} rectangle is: {length * width}")


if __name__ == "__main__":
    print_func()
    calculate_rectangle_area()
    calculate_rectangle_area(2, 3)
    calculate_rectangle_area(1.2, 3.4)
    length_inp, width_inp = map(float, input("Enter the length of the custom rectangle separated by a space: ").split())
    calculate_rectangle_area(length_inp, width_inp)
