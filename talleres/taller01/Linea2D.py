#!/usr/bin/python
import math
import punto as Punto2D

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
        dy = (self.__punto2.getY() - self.__punto1.getY())
        dx = (self.__punto2.getX() - self.__punto1.getX())
        gcf = math.gcd(dy, dx)
        dy /= gcf
        dx /= gcf
        x = self.__punto1.getX()
        y = self.__punto1.getY()
        punto = Punto2D(x, y)
        puntos = [punto]
        while x != self.__punto2.getX() and y != self.__punto2.getY():
            x += dx
            y += dy
            punto = Punto2D(x, y)
            puntos.append(punto)
            pass
        return puntos

       
