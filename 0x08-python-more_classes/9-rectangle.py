#!/usr/bin/python3
class Rectangle:
    """
    Rectangle Class
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle
        Args:
            width (int): width of rectangle
            height (int): height of rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """
        Returns a printable string representation of a rectangle
        """
        if self.width == 0 or self.height == 0:
            return ""
        return (str(self.print_symbol) * self.width + "\n") * self.height

    def __repr__(self):
        """
        Returns a string representation of the rectangle to be able to recreate
        a new instance by using eval().
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """
        Deletes an instance of a rectangle
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def width(self):
        """
        Getter for the width of rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width of rectangle
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter for the height of rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height of rectangle
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Returns the area of a rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
        Returns the perimeter of a rectangle
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns the biggest rectangle based on the area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area() or rect_1.area() > rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Returns a new rectangle instance with width == height == size
        """
        return cls(size, size)
