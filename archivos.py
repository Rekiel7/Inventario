# Modulo para manejo de persistencia con archivos CSV

import csv
import os

def guardar_csv(inventario, ruta, incluir_header=True):
    """
    Guarda el inventario en un archivo CSV.
    
    Parámetros:
        inventario (list): Lista de productos
        ruta (str): Ruta completa del archiv
        incluir_header (bool): Si se incluye el encabesado
    """
    if not inventario:
        print("No se puede guardar: el inventario esta vacio!")
        return False
    
    try:
        # Crear directorios si no existen
        os.makedirs(os.path.dirname(ruta), exist_ok=True)
        
        with open(ruta, mode='w', newline='', encoding='utf-8') as archivo:
            escritor = csv.writer(archivo)
            
            if incluir_header:
                escritor.writerow(['nombre', 'precio', 'cantidad'])
            
            for p in inventario:
                escritor.writerow([p['nombre'], p['precio'], p['cantidad']])
        
        print(f"Inventario guardado exitosamente en: {ruta}")
        return True
    
    except PermissionError:
        print(f"Lo siento pero No tienes permisos para escribir en {ruta}")
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")
    return False


def cargar_csv(ruta):
    """
    Carg productos desde un archivo CSV con validaciones.
    Retorna: (lista_productos, filas_cargadas, filas_invalidas)
    """
    productos = []
    filas_invalidas = 0
    
    try:
        with open(ruta, mode='r', newline='', encoding='utf-8') as archivo:
            lector = csv.reader(archivo)
            filas = list(lector)
            
            if not filas:
                print("El archivo CSV esta vacio.")
                return [], 0, 0
            
            # Validar encabezado
            header = [h.strip().lower() for h in filas[0]]
            if header != ['nombre', 'precio', 'cantidad']:
                print("Error! El encabezado del CSV no es valido (debe ser: nombre,precio,cantidad)")
                return [], 0, 0
            
            # Procesar filas de datos
            for i, fila in enumerate(filas[1:], start=2):
                try:
                    if len(fila) != 3:
                        raise ValueError("No tiene exactamente 3 columnas")
                    
                    nombre = fila[0].strip()
                    precio = float(fila[1])
                    cantidad = int(fila[2])
                    
                    if precio < 0 or cantidad < 0:
                        raise ValueError("Precio o cantidad negativos")
                    if not nombre:
                        raise ValueError("Nombre vacio")
                    
                    productos.append({
                        "nombre": nombre,
                        "precio": precio,
                        "cantidad": cantidad
                    })
                    
                except (ValueError, TypeError):
                    filas_invalidas += 1
                    print(f"Fila {i} invalida y omitida.")
    
    except FileNotFoundError:
        print(f"Error! No se encontro el archivo {ruta}")
        return [], 0, 0
    except UnicodeDecodeError:
        print("Error! El archivo tiene una codificacion no compatible.")
        return [], 0, 0
    except Exception as e:
        print(f"Error inesperado al leer el CSV: {e}")
        return [], 0, 0
    
    return productos, len(productos), filas_invalidas