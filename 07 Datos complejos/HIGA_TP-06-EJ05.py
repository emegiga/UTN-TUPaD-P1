"""
Solicita al usuario una frase e imprime:
• Las palabras únicas (usando un set).
• Un diccionario con la cantidad de veces que aparece cada palabra.
"""

frase = input("Decime una frase: ")

# usamos lower para formatear todo en minusculas
palabras = frase.lower().split()

unicas = set(palabras)
print(unicas)

cantidad = {}
for palabra in palabras:
    if palabra in cantidad:
        cantidad[palabra] += 1
    else:
        cantidad[palabra] = 1
print(cantidad)


