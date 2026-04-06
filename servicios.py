# Modulo con las operaciones CRUD y estadisticas del inventario

def agregar_producto(inventario, nombre, precio, cantidad):
    """
    Agrega un nuevo producto al inventario.
    
    Parámetros:
        inventario (list): Lista de diccionarios con los productos.
        nombre (str): Nombre del producto.
        precio (float): Precio unitario.
        cantidad (int): Cantidad en stoc.
    
    Retorna:
        bool: True si se agrego correctamente.
    """
    # Validar que no exista ya el producto
    if buscar_producto(inventario, nombre):
        print(f"¡Error! El producto '{nombre}' ya existe en el inventario.")
        return False
    
    producto = {
        "nombre": nombre.strip(),
        "precio": float(precio),
        "cantidad": int(cantidad)
    }
    inventario.append(producto)
    print(f"Producto '{nombre}' agregado correctamente!")
    return True


def mostrar_inventario(inventario):
    """Muestra todos los productos del inventario de forma legible."""
    if not inventario:
        print("El inventario está vacio.")
        return
    
    print("\n=== INVENTARIO ACTUAL ===")
    print(f"{'Nombre':<25} {'Precio':>10} {'Cantidad':>10} {'Subtotal':>12}")
    print("----------------------------------------------------------------")
    
    for p in inventario:
        subtotal = p["precio"] * p["cantidad"]
        print(f"{p['nombre']:<25} {p['precio']:>10.2f} {p['cantidad']:>10} {subtotal:>12.2f}")
    print("---------------------------------------------------------------------------------")


def buscar_producto(inventario, nombre):
    """
    Busca un producto por nombre.
    Retorna el diccionario del producto o None si no lo encuentra.
    """
    nombre = nombre.strip().lower()
    for p in inventario:
        if p["nombre"].lower() == nombre:
            return p
    return None


def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    """
    Actualiza precio y/o cantidad de un producto.
    """
    producto = buscar_producto(inventario, nombre)
    if not producto:
        print(f"Producto '{nombre}' no encontrado!")
        return False
    
    if nuevo_precio is not None:
        producto["precio"] = float(nuevo_precio)
    if nueva_cantidad is not None:
        producto["cantidad"] = int(nueva_cantidad)
    
    print(f"Producto '{nombre}' actualizado correctamente!")
    return True


def eliminar_producto(inventario, nombre):
    """Elimina un producto del inventario por su nombre."""
    producto = buscar_producto(inventario, nombre)
    if not producto:
        print(f"Producto '{nombre}' no encontrado.")
        return False
    
    inventario.remove(producto)
    print(f"Producto '{nombre}' eliminado correctamente.")
    return True


def calcular_estadisticas(inventario):
    """
    Calcula estadisticas del inventario.
    Retorna un diccionario con las metricas.
    
    (Opcional) Usa lambda para subtotal como se pedia.
    """
    if not inventario:
        return {
            "unidades_totales": 0,
            "valor_total": 0.0,
            "producto_mas_caro": ("Ninguno", 0.0),
            "producto_mayor_stock": ("Ninguno", 0)
        }
    
    # Lambda para calcular el subtotl 
    subtotal = lambda p: p["precio"] * p["cantidad"]
    
    unidades_totales = sum(p["cantidad"] for p in inventario)
    valor_total = sum(subtotal(p) for p in inventario)
    
    # Producto más caro
    mas_caro = max(inventario, key=lambda p: p["precio"])
    # Producto con mayor stock
    mayor_stock = max(inventario, key=lambda p: p["cantidad"])
    
    return {
        "unidades_totales": unidades_totales,
        "valor_total": valor_total,
        "producto_mas_caro": (mas_caro["nombre"], mas_caro["precio"]),
        "producto_mayor_stock": (mayor_stock["nombre"], mayor_stock["cantidad"])
    }