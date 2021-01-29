  
 class Fecha():
    
    def __init__(self,d, m, a)
        self.__dia = d
        self.__mes = m
        self.__anio = a
        
    def dia(self):
        return self.__dia
    
    def mes(self):
        return self.__mes
    
    def anio(self):
        return self.__anio  
    
    def comparar(self, otra):
        x = self.__anio*10000 + self.__mes*100 + self.__dia 
        y = otro.anio()*10000 + otro.mes()*100 + otro.dia() 
        
        if(x>y):
            return 1
        elif(x<y):
            return -1
        else:
            return 0        
        
    def __str__(self): 
        return "Dia: " + self.__dia + "\n" + "Mes: " + self.__mes + "\n" + "Año: " + self.__anio
