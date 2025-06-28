"""
Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
diccionario donde:
• Las capitales sean las claves.
• Los países sean los valores
"""
paises = {
    "Argentina": "Buenos Aires",
    "Japon": "Tokio",
    "España": "Madrid",
    "Chile": "Santiago de Chile",
    "Uruguay": "Montevideo",
    "Irlanda": "Dublin"
}

capitales = {}

for pais, capital in paises.items():
    capitales[capital] = pais

print(capitales)