"""
Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
y Parcial 2:
• Mostrá los que aprobaron ambos parciales.
• Mostrá los que aprobaron solo uno de los dos.
• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir)
"""

parcial_1 = {"James", "Lars", "Kirk", "Norberto", "Rob", "Janis", "Diana"}
parcial_2 = {"James", "Lars", "Ricardo", "Janis", "Charly", "Mick"}

print("Alumnos que aprobaron ambos parciales:", *parcial_1.intersection(parcial_2))
print("Alumnos que aprobaron solo uno de los dos parciales:", *parcial_1.difference(parcial_2))
print("Alumnos que aprobaron al menos un parcial:", *parcial_1.union(parcial_2))