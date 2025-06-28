"""
Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
Permití consultar qué actividad hay en cierto día y hora.
"""

agenda = {
    ("lunes","09:30"): "Clase de Portugués",
    ("jueves","10:00"): "Ir a buscar pedido al correo",
    ("jueves","14:00"): "Turno médico",
    ("viernes","15:00"): "Dormir siesta",
    ("viernes","20:30"): "Cena con amigos",
}

dia = "jueves"
hora = "14:00"

print("*** AGENDA ***")
evento = agenda.get((dia, hora))
if evento:
    print(f"El evento del {dia} a las {hora} es: {evento}")
else:
    print(f"No hay ningún evento programado el {dia} a las {hora}.")



