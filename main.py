import math

class Vector:
    """
    A class for representing a 2D vector with x and y coordinates.
        Supports basic operations on vectors.

    """
    def __init__(self, x, y):
        """
        " x " = coordinate on the abscissa axis (int or float)
        " y " = coordinate on the ordinate axis (int or float)
        """
        if not isinstance(x, (int, float)):
            raise TypeError("The coordinate must be a numeric value")
        if not isinstance(y, (int, float)):
            raise TypeError("The coordinate must be a numeric value")
        self.__x = x
        self.__y = y

    def __str__(self):
        """
        Prints the coordinate value in the form "x/y = N"
        Where, "x" , "y" are the coordinates, and "N" is the number
        """
        return f"Vector(x={self.__x}, y={self.__y})"

    def __add__(self, other):
        """
        Adding the coordinates of any two already given vectors (x, y)
            self.__x/y = Vector1
            other.__x/y = Vector2
        """
        if not isinstance(other, Vector):
            raise TypeError("You can only use a vector")
        return Vector(self.__x + other.__x, self.__y + other.__y)

    def __sub__(self, other):
        """
        Subtracting the coordinates of any two already given vectors (x, y)
            self.__x/y = Vector1
            other.__x/y = Vector2
        """
        if not isinstance(other, Vector):
            raise TypeError("You can only use a vector")
        return Vector(self.__x - other.__x, self.__y - other.__y)

    def __mul__(self, scalar):
        """
        Multiplying a given vector by a scalar.
        " scalar " = number (scalar)
        """
        if not isinstance(scalar, (int, float)):
            raise TypeError("You can only multiply by a number (scalar)")
        return Vector(self.__x * scalar, self.__y * scalar)

    def __eq__(self, other):
        """
        Checking if vectors have the same coordinates (True or False)
            other.__x/y = Vector2
            self.__x/y = Vector1
        """
        if not isinstance(other, Vector):
            return False
        return self.__x == other.__x and self.__y == other.__y

    def length(self):
        """
        calculating the length (length/magnitude) of the vector, And rounding to “0.00”.
        """
        length_vector = math.sqrt(self.__x ** 2 + self.__y ** 2)
        return round(length_vector, 2)

    def zero_vector(self):
        """
        Checking for a null vector (True, False)
        """
        return self.__x == 0 and self.__y == 0

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y


if __name__ == "__main__":
    try:
        v0 = Vector(0, 0)
        print("Vector0 =", v0)
        print("Length Vector0 =", v0.length())

        v1 = Vector(2, 4)
        print("Vector1 =", v1)
        print("Length Vector1 =", v1.length())

        v2 = Vector(1, 2)
        print("Vector2 =", v2)
        print("Length Vector2 =", v2.length())

        v3 = Vector(10, -2)
        print("Vector3 =", v3)
        print("Length Vector3 =", v3.length())

        v4 = Vector(0.5, -128.5)
        print("Vector4 =", v4)
        print("Length Vector4 =", v4.length())

        v_sum1 = v1 + v2
        print("The sum of vectors (v1 and v2)=", v_sum1)

        v_sum2 = v4 + v2
        print("The sum of vectors (v4 and v2)=", v_sum2)

        v_min1 = v1 - v2
        print("Vector difference (v1 v2)=", v_min1)

        v_min2 = v4 - v3
        print("Vector difference (v1 v2)=", v_min2)

        v_mlp1 = v1 * 1.5
        print("Multiplication of vectors =", v_mlp1)

        v_mlp2 = v0 * 222
        print("Multiplication of vectors =", v_mlp2)

        print("Equality of vectors (v1 = v2?)", v1 == v2)

        print("v0 Is a zero vector", v0.zero_vector())
        print("v4 Is a zero vector", v4.zero_vector())

    except Exception as input_error:
        print(input_error)

