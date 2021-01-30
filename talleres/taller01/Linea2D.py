
import math
from punto import Punto2D

class Line2D():
    """Representacion de punto en 2 dimensiones"""

    def __init__(self, x1, y1, x2, y2):
        self.__punto1 = Punto2D(x1, y1)
        self.__punto2 = Punto2D(x2, y2)

    def punto1(self):
        return self.__punto1

    def punto1(self):
        return self.__punto2

    def puntosIntermedios(self):
        dy = (self.__punto2.get_y() - self.__punto1.get_y())
        dx = (self.__punto2.get_x() - self.__punto1.get_x())
        gcf = math.gcd(dy, dx)
        dy /= gcf
        dx /= gcf
        x = self.__punto1.get_x()
        y = self.__punto1.get_y()
        punto = Punto2D(x, y)
        puntos = [punto]
        while x != self.__punto2.get_x() and y != self.__punto2.get_y():
            x += dx
            y += dy
            punto = Punto2D(x, y)
            puntos.append(punto)
            pass
        return puntos


