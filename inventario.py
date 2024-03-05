inventario = []

def agregar_producto():
    nombre = input("Ingree el nombre del produccto: ")
    cantidad = int(input("Ingrese la cantidad disponible: "))
    precio = input("Ingrese el precio del producto: ")
    producto = {"nombre": nombre, "cantidad": cantidad, "precio": precio}
    inventario.append(producto)
    print("Producto agregado al inventario.")

def actualizar_cantidad():
    nombre = input("Ingree el nombre del producto que va a atualizar: ")
    for producto in inventario:
        if producto["nombre"] == nombre:
            nuevaCantidad = int(input("Ingrese la nueva cantidad disponible: "))
            producto["cantidad"] = nuevaCantidad
            print("Cantidad actualizada.")
            return
    print("El productso no esrta encontrado en inventario")


def eliminar_producto():
    nombre = input("Ingree el nombre del producto que va a eliminar: ")
    for producto in inventario:
        if producto["nombre"] == nombre:
            inventario.remove(producto)
            print("Producto ah sido elimminado del inventario.")
            return
    print("Producto no encontrado en el inventario.")

def mostrar_inventario():
    print("Inventario:")
    for producto in inventario:
        print("Nombre:", producto,"nombre","- Cantidad: ", producto,"cantidad" "- Precio: ", producto,"precio")

def buscar_producto():
    nombre = input("Ingrese el nombre del producto a buscar: ")
    for producto in inventario:
        if producto["nombre"] == nombre:
            print("Nombre:", producto,'nombre',"- Cantidad: ", producto,'cantidad' "- Precio: ", producto,"precio")
            return
    print("Producto no encontrado en el inventario")

while True:
    opcion = int(input("Seleccione una opción:\n1. Agregar producto\n2. Actualizar cantidad\n3. Eliminar producto\n4. Mostrar inventario\n5. Buscar producto\n6. Salir\n"))

    if opcion == 1:
        agregar_producto()
    elif opcion == 2:
        actualizar_cantidad()
    elif opcion == 3:
        eliminar_producto()
    elif opcion == 4:
        mostrar_inventario()
    elif opcion == 5:
        buscar_producto()
    elif opcion == 6:
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")