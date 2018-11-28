"""
    @CarlosCastillo10
"""

class Docente(object):

    # Constructor
    def __init__(self, n,a,t):
        
        self.agregar_nombre(n)
        self.agregar_apellido(a)
        self.agregar_titulo(t)

    # Metodos de agregar
    def agregar_nombre(self, n):
        self.nombre = n

    def agregar_apellido(self, a):
        self.apellido = a

    def agregar_titulo(self, t):
        self.titulo = t

    # Metodos de obtener
    def obtener_nombre(self):
        return self.nombre

    def obtener_apellido(self):
        return self.apellido

    def obtener_titulo(self):
        return self.titulo

    # Metodo de presentar datos
    def presentar_datos(self):
        cadena = ("\n\t\tNombre: %s\n\t\tApellido: %s\n\t\tTitulo: %s"%(self.obtener_nombre().upper(),self.obtener_apellido().upper(),
                self.obtener_titulo().upper()))
        return cadena

