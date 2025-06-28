"""
Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
Luego, mostrá el promedio de cada alumno.
"""
alumnos = {}
notas = []

for j in range(1,4): # bucle para pedir ingrese 3 alumnos
    nombre = input(f"Ingresa el nombre del alumno nro {j}: ")
    for i in range(1,4):    # bucle para pedir 3 notas
        nota = int(input(f"Ingresa la nota {i}: "))
        notas.append(nota)
    alumnos[nombre] = tuple(notas)
    print(f"El promedio del alumno {nombre} es {sum(notas)/3:.2f}")
    notas = []


#print(notas)
#print(alumnos)