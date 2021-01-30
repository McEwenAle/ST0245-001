#!/usr/bin/python
import math

class Line2D():
    """Representacion de punto en 2 dimensiones"""

    def __init__(self, x1, x2, y1, y2):
        self.__punto1 = Punto2D(x1, y1)
        self.__punto2 = Punto2D(x1, y1)

    def punto1(self):
        return self.__punto1

    def punto1(self):
        return self.__punto2

    def puntosIntermedios(self):
        m = (self.__punto2.getY() - self.__punto1.getY()) / (self.__punto2.getX() - self.__punto1.getX())
        x = self.__punto1.getX()
        y = self.__punto1.getY()
        puntos = [(x, y)]
        while x != self.__punto2.getX() and y != self.__punto2.getY():
            pass

       
