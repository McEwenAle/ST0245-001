
import math

class Punto3D():
    """Representacion de punto en 2 dimensiones"""

    def __init__(self, x, y, z):
        self.__x = x
        self.__y = y
        self.__z = z

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_z(self):
        return self.__z

    def radio_polar(self):
        return math.sqrt(pow(self.__x, 2) + pow(self.__y, 2) + pow(self.__z, 2))
    
    def angulo_polar(self):
       return (math.atan(math.sqrt(pow(self.__x, 2) + pow(self.__y, 2)) / self.__z), math.atan(self.__y / self.__x))

    def dist_euclidiana(self, other):
        return math.sqrt(pow(other.__x - self.__x, 2) + pow(other.__y - self.__y, 2) + pow(other.__z - self.__z, 2))

    def __str__(self):
        return "(" + str(self.__x) + "," + str(self.__y) + "," + str(self.__z) + ")"



