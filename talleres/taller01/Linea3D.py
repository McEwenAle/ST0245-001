
import math
from Punto3D import Punto3D

class Line3D():
    """Representacion de punto en 2 dimensiones"""

    def __init__(self, x1, y1, z1, x2, y2, z2):
        self.__punto1 = Punto3D(x1, y1, z1)
        self.__punto2 = Punto3D(x2, y2, z2)

    def punto1(self):
        return self.__punto1

    def punto2(self):
        return self.__punto2

    def puntosIntermedios(self):
        dz = (self.__punto2.get_z() - self.__punto1.get_z())
        dy = (self.__punto2.get_y() - self.__punto1.get_y())
        dx = (self.__punto2.get_x() - self.__punto1.get_x())
        gcf = math.gcd(dy, math.gcd(dx, dz))
        dz /= gcf
        dy /= gcf
        dx /= gcf
        x = self.__punto1.get_x()
        y = self.__punto1.get_y()
        z = self.__punto1.get_z()
        punto = Punto3D(x, y, z)
        puntos = [punto]
        while x != self.__punto2.get_x() and y != self.__punto2.get_y() and z != self.__punto2.get_z():
            x += dx
            y += dy
            z += dz
            punto = Punto3D(x, y, z)
            puntos.append(punto)
            pass
        return puntos

linea = Line3D(0, 0, 0, 3, 3, 3)
puntos = linea.puntosIntermedios()
for p in puntos:
    print(p)