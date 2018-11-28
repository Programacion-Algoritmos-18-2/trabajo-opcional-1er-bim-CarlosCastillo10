"""
    @CarlosCastillo10
"""

class Equipo(object):

    # Constructor
    def __init__(self, ne, nc):
        
        self.agregar_nombre_equipo(ne)
        self.agregar_nombre_pais(nc)

    # Metodos de agregar
    def agregar_nombre_equipo(self, ne):
        self.nombre_equipo = ne

    def agregar_nombre_pais(self, nc):
        self.nombre_pais = nc

    # Metodos de obtener
    def obtener_nombre_equipo(self):
        return self.nombre_equipo

    def obtener_nombre_pais(self):
        return self.nombre_pais

class Futbolista(object):

    # Constructor
    def __init__(self, n,a,e):
        self.agregar_nombre(n)
        self.agregar_apellido(a)
        self.agregar_equipo(e)
        self.posicion = ""
        self.dorsal = 0
    
    # Metodos de agregar
    def agregar_nombre(self, n):
        self.nombre = n

    def agregar_apellido(self, a):
        self.apellido = a

    def agregar_equipo(self, e):
        self.equipo = e

    def agregar_posicion(self, p):
        self.posicion = p
    
    def agregar_dorsal(self, d):
        self.dorsal = d

    # Metodos de obtener
    def obtener_nombre(self):
        return self.nombre

    def obtener_apellido(self):
        return self.apellido

    def obtener_equipo(self):
        return self.equipo

    def obtener_posicion(self):
        return self.posicion

    def obtener_dorsal(self):
        return self.dorsal

    # Metodo de presentar datos
    def presentar_datos(self):
        cadena = ("\nJugador:\n\t%s %s,\n\tpertenece al equipo %s del pais %s,\n\tsu posicion es %s y,\n\tsu dorsal es %d.\n" %(self.obtener_nombre(),self.obtener_apellido(),
            self.obtener_equipo().obtener_nombre_equipo(),self.obtener_equipo().obtener_nombre_pais(),self.obtener_posicion().upper(),self.obtener_dorsal())) 
        return cadena

     