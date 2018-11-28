#Autor: Carlos Castillo

from prestamo.modelo import *

# Creamos el objeto de tipo Deudor Garante para presentar sus datos
d = Garante("Jose Castillo","Loja",800.93)

# Creamos el objeto de tipo Prestamo 
p = Prestamo("Carlos Castillo",563.45,1000,10,2,d)

# Creamos el objeto de tipo Deudor Garante para presentar sus datos
d1 = Garante("Vilma Giron","Cuenca",1100.93)
        
# Creamos el objeto de tipo PrestamosVehiculo.
p1 = PrestamosAutomovil("Juan Salinas", 900.32, 5000, 5, 10, "Garante Solidario", "Propio", "Chevrolet", d1)

        
#Presentamos en pantalla los metodos toString de cada objeto
print("\n%s%s\n\n"%(p.presentar_datos(),d.presentar_datos()))
print("%s%s\n\n"%(p1.presentar_datos(),d1.presentar_datos()))