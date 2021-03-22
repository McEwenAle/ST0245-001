from Estudiantes import Clase, Estudiante, Evaluacion
import pandas as pd


notasFundamentos = pd.read_csv('NOTAS ST0242.csv')
notasFundamentos.columns = ["nombre","codigo","Cod. Materia","Semestre","Grupo","Vacio1","Vacio2","Descripcion Evaluacion","Porcentaje","Descripcion","Nom. Materia","Vacio3","Nota","Nota Definitiva"]

estudiantes = []
e = notasFundamentos
codigo = -1
for i in range(len(e)):
    if e["codigo"][i] != codigo:
        codigo = e["codigo"][i]
        estudiantes.append(Estudiante(e["codigo"][i], e["nombre"][i]))
        estudiantes[-1].addClass(Clase(e["Cod. Materia"][i],e["Nom. Materia"][i], e["Semestre"][i], e["Grupo"][i], e["Nota Definitiva"][i]))
    estudiantes[-1].clases[-1].addEvaluacion(Evaluacion(e["Descripcion Evaluacion"][i],e["Porcentaje"][i],e["Descripcion"][i],e["Nota"][i]))  

notasEstrucutras1 = pd.read_csv('NOTAS ST0245.csv')
notasEstrucutras1.columns = ["nombre","codigo","Cod. Materia","Semestre","Grupo","Vacio1","Vacio2","Descripcion Evaluacion","Porcentaje","Descripcion","Nom. Materia","Vacio3","Nota","Nota Definitiva"]
e = notasEstrucutras1
codigo = -1
for i in range(len(e)):
    if e["codigo"][i] != codigo:
        codigo = e["codigo"][i]
        estudiantes[codigo].addClass(Clase(e["Cod. Materia"][i],e["Nom. Materia"][i], e["Semestre"][i], e["Grupo"][i], e["Nota Definitiva"][i]))
    estudiantes[codigo].clases[-1].addEvaluacion(Evaluacion(e["Descripcion Evaluacion"][i],e["Porcentaje"][i],e["Descripcion"][i],e["Nota"][i]))

notasEstrucutras2 = pd.read_csv('NOTAS ST0247.csv')
notasEstrucutras2.columns = ["nombre","codigo","Cod. Materia","Semestre","Grupo","Vacio1","Vacio2","Descripcion Evaluacion","Porcentaje","Descripcion","Nom. Materia","Vacio3","Nota","Nota Definitiva"]
e = notasEstrucutras2
codigo = -1
for i in range(len(e)):
    if e["codigo"][i] != codigo:
        codigo = e["codigo"][i]
        estudiantes[codigo].addClass(Clase(e["Cod. Materia"][i],e["Nom. Materia"][i], e["Semestre"][i], e["Grupo"][i], e["Nota Definitiva"][i]))
    estudiantes[codigo].clases[-1].addEvaluacion(Evaluacion(e["Descripcion Evaluacion"][i],e["Porcentaje"][i],e["Descripcion"][i],e["Nota"][i]))

for e in estudiantes:
    print(e)  