"""
    @CarlosCastillo10
"""

class Alumno(object):

    # Constructor
    def __init__(self, nom,docentem,docentes):
        
        self.agregar_nombres(nom)
        self.agregar_docente_matematicas(docentem)
        self.agregar_docente_sociales(docentes)

    # Metodos de agregar
    def agregar_nombres(self, nom):
        self.nombres = nom

    def agregar_docente_matematicas(self, docentem):
        self.docente_matematicas = docentem

    def agregar_docente_sociales(self, docentes):
        self.docente_sociales = docentes

    # Metodos de obtener
    def obtener_nombres(self):
        return self.nombres

    def obtener_docente_matematicas(self):
        return self.docente_matematicas

    def obtener_docente_sociales(self):
        return self.docente_sociales
    
    # Metodo de presentar datos
    def presentar_datos(self):
        cadena = ("\nNombre del alumno: %s\n"%self.obtener_nombres().upper())
        
        return cadena

