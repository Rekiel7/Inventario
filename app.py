# Programa principal del Inventario Avanzado

from servicios import (
    agregar_producto, mostrar_inventario, buscar_producto,
    actualizar_producto, eliminar_producto, calcular_estadisticas
)
from archivos import guardar_csv, cargar_csv
import os

def mostrar_menu():
    print("=====================================")
    print("       SISTEMA DE INVENTARIO AVANZADO")
    print("=====================================")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Buscar producto")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Ver estadísticas")
    print("7. Guardar inventario en CSV")
    print("8. Cargar inventario desde CSV")
    print("9. Salir")
    print("======================================")


def main():
    inventario = []  # Lista de diccionarios
    
    while True:
        mostrar_menu()
        try:
            opcion = int(input("\nSeleccione una opción de (1-9): "))
        except ValueError:
            print("Error: Debe ingresar un número.")
            continue
        
        if opcion == 1:  # Agregar
            nombre = input("Nombre del producto: ").strip()
            if not nombre:
                print("Error: El nombre no puede estar vacío.")
                continue
            try:
                precio = float(input("Precio unitario: "))
                cantidad = int(input("Cantidad en stock: "))
                if precio < 0 or cantidad < 0:
                    print("Error El Precio y cantidad deben ser positivos!")
                    continue
                agregar_producto(inventario, nombre, precio, cantidad)
            except ValueError:
                print("Error: Precio y cantidad deben ser números válidos!")
        
        elif opcion == 2:  # Mostrar
            mostrar_inventario(inventario)
        
        elif opcion == 3:  # Buscar
            nombre = input("Nombre del producto a buscar: ").strip()
            producto = buscar_producto(inventario, nombre)
            if producto:
                print(f"\nProducto encontrado:")
                print(f"Nombre: {producto['nombre']}")
                print(f"Precio: ${producto['precio']:.2f}")
                print(f"Cantidad: {producto['cantidad']}")
            else:
                print("Producto no encontrado.")
        
        elif opcion == 4:  # Actualizar
            nombre = input("Nombre del producto a actualizar: ").strip()
            if not buscar_producto(inventario, nombre):
                continue
            try:
                precio_input = input("Nuevo precio (Enter para mantener): ").strip()
                cantidad_input = input("Nueva cantidad (Enter para mantener): ").strip()
                
                nuevo_precio = float(precio_input) if precio_input else None
                nueva_cantidad = int(cantidad_input) if cantidad_input else None
                
                actualizar_producto(inventario, nombre, nuevo_precio, nueva_cantidad)
            except ValueError:
                print("Error: Valores numéricos inválidos.")
        
        elif opcion == 5:  # Eliminar
            nombre = input("Nombre del producto a eliminar: ").strip()
            eliminar_producto(inventario, nombre)
        
        elif opcion == 6:  # Estadísticas
            stats = calcular_estadisticas(inventario)
            print("\n=== ESTADÍSTICAS DEL INVENTARIO ===")
            print(f"Unidades totales: {stats['unidades_totales']}")
            print(f"Valor total del inventario: ${stats['valor_total']:.2f}")
            print(f"Producto más caro: {stats['producto_mas_caro'][0]} (${stats['producto_mas_caro'][1]:.2f})")
            print(f"Producto con mayor stock: {stats['producto_mayor_stock'][0]} ({stats['producto_mayor_stock'][1]} unidades)")
        
        elif opcion == 7:  # Guardar a CSV
            ruta = input("Ruta del archivo CSV (ej: inventario.csv o carpeta/inventario.csv): ").strip()
            if not ruta:
                ruta = "inventario.csv"
            guardar_csv(inventario, ruta)
        
        elif opcion == 8:  # Cargar CSV
            ruta = input("Ruta del archivo CSV a cargar: ").strip()
            if not ruta:
                print("Debe ingresar una ruta.")
                continue
            
            productos_nuevos, cargados, invalidas = cargar_csv(ruta)
            
            if cargados == 0 and invalidas == 0:
                continue
            
            print(f"\nSe cargaron {cargados} productos válidos. {invalidas} filas inválidas fueron omitidas.")
            
            if not inventario:
                # Si está vacío, sobrescribir directamente
                inventario.extend(productos_nuevos)
                print("Inventario cargado correctamente (sobrescritura automática).")
            else:
                accion = input("¿Sobrescribir inventario actual? (S/N): ").strip().upper()
                if accion == 'S':
                    inventario.clear()
                    inventario.extend(productos_nuevos)
                    print("Inventario sobrescrito correctamente.")
                else:
                    # Fusión (suma cantidad, actualiza precio si es diferente)
                    print("Fusionando inventario (se sumará la cantidad, se actualizará el precio si gusta diferir)...")
                    for p in productos_nuevos:
                        existente = buscar_producto(inventario, p["nombre"])
                        if existente:
                            existente["cantidad"] += p["cantidad"]
                            if existente["precio"] != p["precio"]:
                                existente["precio"] = p["precio"]
                                print(f"Precio de '{p['nombre']}' actualizado a ${p['precio']:.2f}")
                        else:
                            inventario.append(p)
                    print("Fusión completada.")
        
        elif opcion == 9:  # Salir
            print("Fin del programa... Gracias por usar nuestro sistema de inventario!")
            break
        
        else:
            print("Opción inválida. Por favor seleccione solo del 1 al 9.")

if __name__ == "__main__":
    main()