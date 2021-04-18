import queue

class Nodo:
	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data

	def __repr__(self):
		return f'{self.data}'

class BinaryTree:
    def __init__(self):
        self.root = None
    
    #Complejidad O(n)
    def insertar(self, data):
        if self.root is None:
            self.root = Nodo(data)
        else:
            self.__insertar_aux(data, self.root)

    def __insertar_aux(self, data, actual):
        if data < actual.data and actual.left == None:
            actual.left = Nodo(data)
        elif data >= actual.data and actual.right == None:
            actual.right = Nodo(data)
        elif data < actual.data:
            self.__insertar_aux(data, actual.left)
        else:
            self.__insertar_aux(data, actual.right)

    #Complejidad O(n)   
    def buscar(self, data):
        return self.__buscar_aux(data, self.root)
    
    def __buscar_aux(self, data, actual):
        if actual == None:
            return None
        if actual.data == data:
            return actual
        elif data < actual.data:
            return self.__buscar_aux(data, actual.left)
        else:
            return self.__insertar_aux(data, actual.right)
            
    #Complejidad O(n)
    def borrar(self, data):
        self.__borrar_aux(data, self.root)

    def __borrar_aux(self, data, actual):
        if actual == None:
            return None
        if actual.left != None and actual.left.data == data:
            return self.__auxSwitch(actual, actual.left)
        elif actual.right != None and actual.right.data == data:
            return self.__auxSwitch(actual, actual.right)
        elif data < actual.data:
            return self.__borrar_aux(data, actual.left)
        else:
            return self.__borrar_aux(data, actual.right)

    def __auxSwitch(self, parent, switch):
        result = None
        if switch.left != None :
            result = switch.left
        elif switch.right != None:
            result = switch.right
        if parent.left == switch:
            parent.left = result
        else:
            parent.right = result
        return switch
    # ------------------------------------------------------
    # In-Orden        
    def imprimir(self):
        self.__imprimir_aux(self.root)
        
    def __imprimir_aux(self, actual):
        if actual is not None:
            self.__imprimir_aux(actual.left)
            print(actual.data)
            self.__imprimir_aux(actual.right)
            
    # O(e) e = numero de conectiones
    def dibujar(self):
        return  f'digraph G {"{"}\n{self.__dibujar_aux(self.root)}\n{"}"}'
    
    def __dibujar_aux(self, actual):
        s = " "
        if actual.left != None:
            s =  s + actual.__repr__() + "->" + actual.left.__repr__() + "\n"
            s = s + self.__dibujar_aux(actual.left)
        if actual.right != None:
            s = s + actual.__repr__() + "->" + actual.right.__repr__() + "\n"
            s = s + self.__dibujar_aux(actual.right)
        return s



if __name__ == '__main__':
    b = BinaryTree()
    b.insertar(4)
    b.insertar(3)
    b.insertar(5)
    b.insertar(8)
    # print(b.buscar(3))
    b.imprimir()
    print(b.dibujar())

