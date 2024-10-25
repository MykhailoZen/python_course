from typing import Union


def print_hw():
    """
    Print "Hello world"
    :return:
    """
    print("Hello World!")


def calculate_rectangle_area(length: Union[float, int], width: Union[float, int]) -> Union[float, int]:
    """
    Calculate rectangle area by multiply length on width
    :param length:  length of the rectangle
    :param width:  width of the rectangle
    :return: multiplication of length and width
    """
    return length * width


if __name__ == '__main__':
    print_hw()
    print(f"Rectangle area calculation: {calculate_rectangle_area(5, 5)}")
    print(f"Rectangle area calculation: {calculate_rectangle_area(1.5, 5)}")
    print(f"Rectangle area calculation: {calculate_rectangle_area(0, 5)}")
