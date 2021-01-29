#!/usr/bin/python
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
        return (self.__x ** 2 + self.__y ** 2) ** (1/2)
    
    def angulo_polar(self):
       return math.atan(self.__y / self.__x)

    def dist_euclidiana(self, other):
        return ((other.__x - self.__x) ** 2 + (other.__y - self.__y) ** 2) ** (1/2)
