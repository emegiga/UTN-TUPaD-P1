import math # Para usar en ejercicio 4

# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!".
print("Hola Mundo!")

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
# realizar la impresión por pantalla.  
nombre = input("Ingresa tu nombre: ")

print(f"Hola {nombre}!")

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
# años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
# la impresión por pantalla. 
name = input("Ingresa tu nombre: ")
surname = input("Ingresa tu apelido: ")
age = int(input("Ingresa tu edad: "))
location = input("Ingresa tu lugar de residencia: ")

print(f"Soy {name} {surname}, tengo {age} años y vivo en {location}.")

# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.
radio = int(input("Ingresa el radio del círculo: "))

perimetro = 2 * math.pi * radio
area = math.pi * radio ** 2

print(f"El perímetro del círculo es {perimetro:.2f}.")
print(f"El área del círculo es {area:.2f}.")

# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.
segundos = int(input("Ingresa cantidad de segundos: "))

horas = segundos / 3600     # 3600 = 60 x 60

print(f"{segundos} segundos equivalen a {horas:.2f} horas.")

# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.
numero = int(input("Ingresa un número: "))

for x in range(1, 11):
    print(f"{numero} x {x} = {numero * x}")

# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
num1 = int(input("Ingresa el 1er número entero mayor a cero: "))
num2 = int(input("Ingresa el 1er número entero mayor a cero: "))

print(f"Suma: {num1 + num2}")
print(f"Resta: {num1 - num2}")
print(f"Multiplicación: {num1 * num2}")
print(f"División: {(num1 / num2):.2f}")

# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal. 
# Tener en cuenta que el índice de masa corporal se calcula del siguiente modo: IMC = peso kg / altura en mts * altura en mts
altura = int(input("Ingresa tu altura (en centímetros): "))
peso = int(input("Ingrese su peso (en kgs): "))

imc = peso / (altura / 100) ** 2

print(f"Dado el peso {peso} kgs y la altura {altura/100} mts, tu índice de masa corporal es {imc:.2f}.")

# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit. 
# Tener en cuenta la siguiente equivalencia: 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 = 9/5 x 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32

temp_celsius = float(input("Ingresa una temperatura (en Celsius): "))

temp_fahrenheit = (9/5) * temp_celsius + 32

print(f"{temp_celsius}°C equivalen a {temp_fahrenheit}°F.")

# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.
num01 = int(input("Ingresa el 1er número: "))
num02 = int(input("Ingresa el 2do número: "))
num03 = int(input("Ingresa el 3er número: "))

print(f"El promedio de los números ingresados ({num01}, {num02}, {num03}) es de {(num01 + num02 + num03) / 3}")