"""
Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
Permití al usuario:
• Consultar el stock de un producto ingresado.
• Agregar unidades al stock si el producto ya existe.
• Agregar un nuevo producto si no existe.
"""

inventario = {"lapicera": 5, "lapiz": 3, "marcador": 19, "goma": 3, "sacapuntas": 1, "regla": 25}

print("*** INVENTARIO ***")
opcion = int(input("1-Consultar stock \n2-Agregar stock a producto existente \n3-Agregar un producto nuevo\n\nQue querés hacer? Indica el nro de opción: "))

producto = input("Ingresa el nombre del producto: ").lower()

if opcion == 1:
    if producto in inventario:
        print(f"Stock disponible: {inventario[producto]}")
    else:
        print("El producto ingresado NO EXISTE en el inventario.")
elif opcion == 2:
    if producto in inventario:
        suma_stock = int(input("Cuántos unidades deseas agregar al stock? "))
        inventario[producto] += suma_stock
        print(f"Stock actualizado! {producto} = {inventario[producto]} unidades")
    else:
        print("El producto ingresado NO EXISTE en el inventario.")
elif opcion == 3:
    if producto in inventario:
        print("El producto ingresado YA EXISTE en el inventario.")
    else:
        suma_stock = int(input("Cuántos unidades deseas agregar al stock? "))
        inventario[producto] = suma_stock
        print(f"Perfecto! Producto añadido... {producto} = {inventario[producto]} unidades")  