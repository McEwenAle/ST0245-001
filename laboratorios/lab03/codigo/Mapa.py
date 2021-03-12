class Node:
    def __init__(self, ID, x, y, nombre) -> None:
        self.__id = ID
        self.__x = x
        self.__y = y
        self.__nombre = nombre
        self.__conections = []

    def addConection(self, id, d, nombre):
        conection = Connection(self.__id, id, d, nombre)
        self.__conections.append(conection)

    def __str__(self):
        s = str(self.__id) + " " + str(self.__x) + " " + str(self.__y) + " " + str(self.__nombre) + "\n" + "Conections:"
        for e in self.__conections:
            s = s + "\n" + str(e)
        s = s + "\n"
        return s

class Connection:
    def __init__(self, origin, destination, d, nombre) -> None:
        self.__origin = origin
        self.__destination = destination
        self.__distance = d
        self.__nombre = nombre

    def __str__(self):
        return str(self.__origin) + " " + str(self.__destination) + " " + str(self.__distance) + " " + str(self.__nombre)