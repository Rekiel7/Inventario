# Lista donde se almacenan los productos del inventario
inventario = []

# Funciones

def agregar_producto():
    """
    Esta funcion permite agregar un producto al inventario.
    Solicita nombre, precio y cantidad, validando los datos ingresados.
    """
    nombre = input("Ingrese el nombre del producto: ")

    try:
        precio = float(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad exacta del producto: "))

        # validacion de valores negativos
        if precio < 0 or cantidad < 0:
            print("Error: el precio y la cantidad deben ser positivos.\n")
            return

    except ValueError:
        print("Error: ingrese valores numericos validos.\n")
        return

    # crear el producto como diccionario
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    # agregar producto a la lista inventario
    inventario.append(producto)
    print("El Producto fue agregado correctamente.\n")


def mostrar_inventario():
    """
    Esta funcion muestra todos los productos almacenados en el inventario.
    Utiliza un bucle for para recorrer la lista.
    """
    if len(inventario) == 0:
        print("El inventario esta vacío.\n")
        return

    print("\n--- INVENTARIO ---")
    for producto in inventario:
        print(f"Producto: {producto['nombre']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']}")
    print()


def calcular_estadisticas():
    """
    Esta funcion calcula:
    - El valor total del inventario (precio * cantidad)
    - La cantidad total de productos (sumatoria de cantidades)
    """
    if len(inventario) == 0:
        print("No hay productos para calcular estadisticas.\n")
        return

    valor_total = 0
    total_productos = 0

    for producto in inventario:
        valor_total += producto["precio"] * producto["cantidad"]
        total_productos += producto["cantidad"]

    print("\n--- ESTADISTICAS ---")
    print(f"Valor total del inventario: {valor_total}")
    print(f"Cantidad total de productos: {total_productos}\n")


# Menu principal

def menu():
    """
    Menu interactivo que se ejecuta en un bucle while
    hasta que el usuario decide salir.
    """
    while True:
        print("===== MENÚ =====")
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Calcular estadisticas")
        print("4. Salir")

        opcion = input("Seleccione una opcion: ")

        # Estructura condicional para manejar opciones
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            mostrar_inventario()
        elif opcion == "3":
            calcular_estadisticas()
        elif opcion == "4":
            print("Saliendo del programa!...")
            break
        else:
            print("Opcion invalida, porfavor Intente nuevamente.\n")


# Ejecutar el programa
menu()



# Este programa permite gestionar un inventario
# utilizando listas y diccionarios. Implementa
# estructuras de control como condicionales y bucles,
# y organiza el codigo mediante funciones para hacerlo
# mas claro, reutilizable y facil de mantener.
