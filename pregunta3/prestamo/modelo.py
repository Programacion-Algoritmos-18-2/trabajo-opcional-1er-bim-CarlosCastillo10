"""
    @CarlosCastillo10
"""
class Garante(object):

    # Constructor
    def __init__(self, n, c, s):
        self.agregar_nombre(n)
        self.agregar_ciudad(c)
        self.agregar_sueldo(s)
        
    
    # Metodos de agregar.
    def agregar_nombre(self, n):
        self.nombres = n.upper();
    
    
    def agregar_ciudad(self, c):
        self.ciudad = c
    
    
    def agregar_sueldo(self, s):
        self.sueldo = s
    
    
    # Metodos de obtener
    def obtener_nombre(self):
        return self.nombres

    
    def obtener_ciudad(self):
        return self.ciudad
    
    def obtener_sueldo(self):
        return self.sueldo
    
    def presentar_datos(self):
        cadena = ("\t\tNombre: %s\n\t\tCiudad: %s\n\t\tSueldo: %.2f"%(self.obtener_nombre(),self.obtener_ciudad(),self.obtener_sueldo()))

        return cadena
    

class Prestamo(object):

    def __init__(self, n, s, m, i, t, g):
        
        # Llamamos a cada uno de los metodos
        self.agregar_nombre_de_beneficiario(n)
        self.agregar_sueldo(s)
        self.agregar_monto_de_prestamo(m)
        self.agregar_interes(i);
        self.agregar_tiempo_anios(t)
        self.agregar_tipo_garante1(g)
           
    # Metodos de agregar.
    def agregar_nombre_de_beneficiario(self, n):
        self.nombre_de_benefiario = n.upper() # Guarda el nombre
    
    
    def agregar_sueldo(self, s):
        self.sueldo = s # Guarda el sueldo
    
    
    def agregar_monto_de_prestamo(self, m):
        self.monto_de_prestamo = m #Guarda el monto
    
    
    def agregar_interes(self, i):
        self.interes = i # Guarda el interes
    
    
    def agregar_tiempo_anios(self, t):
        self.tiempo_anios = t # Guarda el tiempo de interes
    
    
    def agregar_tipo_garante1(self, g):
        self.tipo_garante1 = g #Guarda el tipo de garante
    
    
    # Metodos de obtener.
    def obtener_nombre_beneficiario(self):
        return self.nombre_de_benefiario # Retorna el nombre
    
    
    def obtener_sueldo(self):
        return self.sueldo #Retorna el sueldo
    
    
    def obtener_monto_prestamo(self):
        return self.monto_de_prestamo # Retorna el monto
    
    
    def obtener_interes(self):
        return self.interes # Retorna el interes
    
    
    def obtener_tiempo_anios(self):
        return self.tiempo_anios #Retorna el tiempo de interes
    
    
    def obtener_tipo_garante1(self):
        return self.tipo_garante1 #Retorna el tipo de garante.

    # Metodo de presentar datos
    def presentar_datos(self):
        cadena = ("Datos del Beneficiario\n\n\tNombre: %s\n\tSueldo: %.2f\n\tMonto de Prestamo: %.2f\n\tInteres: %.0f%s\n\tTiempo de Prestamo: %d %s\n\tTipo de garante 1:\n"%(self.obtener_nombre_beneficiario()
            ,self.obtener_sueldo(),self.obtener_monto_prestamo(),self.obtener_interes(),"%",self.obtener_tiempo_anios(),"años"))
        return cadena

class PrestamosAutomovil(Prestamo):
    
    # Constructor
    def __init__(self, n, s, m, i, t, g, tv, mar, g2):

        super(PrestamosAutomovil, self).__init__(n, s, m, i, t, g) #Llamamos al constructor de la clase padre
        self.agregar_tipo_vehiculo(tv)
        self.agregar_marca(mar)
        self.agregar_tipo_garante2(g2)

    
    # Metodos de agregar.
    def agregar_tipo_vehiculo(self, tv):
        self.tipo_vehiculo = tv
    
    
    def agregar_marca(self, mar):
        self.marca = mar
    
    def agregar_tipo_garante2(self, g2):
        self.tipo_garante2 = g2
    
    
    # Metodos de obtener.
    def obtener_tipo_vehiculo(self):
        return self.tipo_vehiculo
    
    
    def obtener_marca(self):
        return self.marca
    
    def obtener_tipo_garante2(self):
        return self.tipo_garante2
    
    
    # Sobre escribimos el metodo toString.
    
    def presentar_datos(self):
        cadena = ("%s%s\n\n\tTipo de Vehiculo: %s\n\tMarca del Vehiculo: %s\n\tTipo de Garante 2:\n"%(super(PrestamosAutomovil,self).presentar_datos(),self.obtener_tipo_garante1().presentar_datos(),
            self.obtener_tipo_vehiculo(),self.obtener_marca()))
        return cadena
 