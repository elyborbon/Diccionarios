#Iterar datos 
datos = {"nombre" : "Juan", "apellido" : "Lopez", "Manzana": "20", "apellido_2" :"30"}

for valor in datos:
    print (valor)
# Devuelve el valor 
for valor in datos:
    print (datos[valor])

for valor in datos.values():
    print(valor)

#Iterar valores 
for clave, valor in datos.items():
    print (clave, valor)