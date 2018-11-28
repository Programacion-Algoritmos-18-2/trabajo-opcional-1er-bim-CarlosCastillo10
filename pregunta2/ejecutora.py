#Autor: Carlos Castillo

# Importamos todo de las 2 clases
from personal_academico.modelo import *
from sector_estudiantil.modelo2 import *

        
nombre_alumno = input("\nIngrese el nombre del estudiante: ")# Guarda el nombre del alumno
        
# Datos del docente de Matematicas
print("\nDatos del docente de Matematicas")
nombre_docente = input(("\n\tNombre: ")) # Guarda el nombre del docente de matematicas
        
apellido_docente = input(("\tApellido: "))# Guarda el apellido del docente de matematicas.
        
titulo = input("\tTitulo: ")# Guarda el titulo del docente de matematicas
        
# Crea el objeto de tipo docente y envia los parametros del constructor
d1 = Docente(nombre_docente,apellido_docente,titulo)
        
# Datos del docente de sociales
print("\nDatos del docente de Sociales")
nombre_docente = input(("\n\tNombre: ")) # Guarda el nombre del docente de sociales
        
apellido_docente = input(("\tApellido: "))# Guarda el apellido del docente de sociales
        
titulo = input("\tTitulo: ")# Guarda el titulo del docente de sociales
        
# Crea el objeto de tipo docente y envia los parametros del constructor
d2 = Docente(nombre_docente,apellido_docente,titulo)
        
# Crea el objeto de tipo alumno.
a1 = Alumno(nombre_alumno,d1,d2)
     
print("\n%20s\n%s\n\tDocente Matematicas\n%s\n\n\tDocente Sociales\n%s\n\n"%("REPORTE",a1.presentar_datos()
	,d1.presentar_datos(),d2.presentar_datos()))# Presenta en pantalla los datos.