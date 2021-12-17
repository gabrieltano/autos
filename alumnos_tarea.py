#Una escuela tiene alumnos, cuyas características son:
#*Nombre
#*Apellido
#*Nota Matematica
#*Nota Lengua
#*Nota geografía
#*Promedio
#-Los alumnos pueden dar exámenes.

#La escuela también tiene profesores que tienen las siguientes características:
#*Nombre
#*Apellido
#*Materia que enseña
#-Los profesores toman exámenes y le dan al alumno una nota.
#Se deben cargar distintos alumnos y profesores, que los alumnos den exámenes que toman los profesores y que el resultado sea una nota. El alumno siempre debe tener un promedio (al principio las tres notas son 0).

class Escuela():
    def __init__(self,Nombre, Apellido):
        self.Nombre= Nombre
        self.Apellido= Apellido

class Alumnos(Escuela):
    def __init__ (self,Nombre,Apellido,Nota_Matematica,Nota_Lengua,Nota_Geografia,):
        

