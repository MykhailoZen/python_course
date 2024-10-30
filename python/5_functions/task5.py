def printfunc():
    print("Hello World")


def calculate_rectangle_area(length=4.0, width=2.0):
    """
    Function calculates the area of a rectangle.
    The function should accept the length and width of the rectangle as arguments and return the calculated area.
    """
    print(f"The area of the {length} x {width} rectangle is: {length * width}")


printfunc()
calculate_rectangle_area()
calculate_rectangle_area(2, 3)
calculate_rectangle_area(1.2, 3.4)
length, width = map(float, input("Enter the length of the custom rectangle separated by a space: ").split())
calculate_rectangle_area(length, width)
