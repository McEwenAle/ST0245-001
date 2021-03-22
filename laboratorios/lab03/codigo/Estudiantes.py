class Evaluacion :
    def __init__(self, descripcion, porcentaje, tipo, nota) -> None:
        self.descripcion = descripcion
        self.porcentaje = porcentaje
        self.tipo = tipo
        self.nota = nota

    def __str__(self) -> str:
        return str(self.descripcion) + " " + str(self.tipo) + " " + str(self.nota) + " " + str(self.porcentaje)
        

class Clase:
    def __init__(self, codigo, clase, semestre, grupo, nota) -> None:
        self.codigo = codigo
        self.clase = clase
        self.nota = nota
        self.evaluaciones = []
        self.semestre = semestre
        self.grupo = grupo

    def addEvaluacion(self, evaluacion : Evaluacion):
        self.evaluaciones.append(evaluacion)

    def __str__(self) -> str:
        s = str(self.codigo) + " " + str(self.clase) + " " + str(self.grupo) + " "  + str(self.semestre) + " " + str(self.nota) + "\nEvaluaciones:"
        for e in self.evaluaciones:
            s = s + "\n" + str(e)
        return s

class Estudiante:
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre
        self.clases = []
    
    def addClass(self, clase):
        self.clases.append(clase)

    def __str__(self) -> str:
        s = str(self.codigo) + " " + str(self.nombre) + "\nClases:"
        for e in self.clases:
            s = s + "\n" + str(e)
        s = s + "\n\n"
        return s

