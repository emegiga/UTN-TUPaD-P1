"""
Escribí un programa que permita almacenar y consultar números telefónicos.
• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
• Luego, pedí un nombre y mostrale el número asociado, si existe.
"""

contactos = {"Jimmy": 18091970, "Janis": 4101970}

for carga in range(5):
    nombre = input("Ingresa nombre: ")
    numero = input("Ingresa número de teléfono: ")
    contactos[nombre] = numero

#print(contactos)

consulta = input("Consultas? Decime el nombre y lo buscamos: ")
if consulta in contactos.keys():
    print(contactos[consulta])
else:
    print("El contacto ingresado no existe.")
