#Autor: Carlos Castillo

from mipaquete.modelo import * #Importamos de mi paquete.modelo todo

e = Equipo("Manchester United","Inglaterra") # Creamos el objeto de tipo Equipo

# Creamos el objeto de tipo Futbolista y llamamos a sus metodos
f = Futbolista("Antonio","Valencia",e)
f.agregar_posicion("lateral")
f.agregar_dorsal(25)

e2 = Equipo("Necaxa","Mexico") # Creamos el objeto de tipo Equipo

# Creamos el objeto de tipo Futbolista y llamamos a sus metodos
f2 = Futbolista("Alex","Aguinaga",e2)
f2.agregar_posicion("mediocentro")
f2.agregar_dorsal(7)

e3 = Equipo("Lazio","Italia")# Creamos el objeto de tipo Equipo

# Creamos el objeto de tipo Futbolista y llamamos a sus metodos
f3 = Futbolista("Felipe","Caicedo",e3)
f3.agregar_posicion("delantero")
f3. agregar_dorsal(12)

lista = [f, f2, f3] # Guardamos los objetos en una lista

for x in lista:
	print(x.presentar_datos()) # Presentamos el metodo presentar_datos de cada objeto
