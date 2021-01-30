
import math

class Punto2D():
    """Representacion de punto en 2 dimensiones"""

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def radio_polar(self):
        return math.sqrt(pow(self.__x, 2) + pow(self.__y, 2))
    
    def angulo_polar(self):
       return math.atan(self.__y / self.__x)

    def dist_euclidiana(self, other):
        return math.sqrt(pow(other.__x - self.__x, 2) + pow(other.__y - self.__y, 2))

    def __str__(self):
        return "(" + str(self.__x) + "," + str(self.__y) + ")"



