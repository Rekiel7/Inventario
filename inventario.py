# programa de inventario simple que permite registrar un producto, su precio y su 
# cantidad, luego calcula el costo total.

# Solicitar nombre del producto a tomar

product_name = input("Enter the product here: ")

while True:
    try:
        price = float(input("Please enter the product price: "))
        break
    except ValueError:
        print("Error: please enter a valid price for the product to take it. ")

# Validar la cantidad introducida
while True:
    try:
        quantity = int(input("Please enter the product quantity here: "))
        break
    except ValueError:
        print("Error: Please enter a valid integer for the product to take it. ")
 
      
# Calcular el costo total
total_cost = price * quantity

# Mostrar los resultados de la consola

print("\n-----Result-----")
print("Product:", product_name)
print("Unit Price:", price)
print("Quantity:", quantity)
print("Total cost:", total_cost)

# Fin del programa
# Este programa solicita al usuario los datos del producto, valida las entradas,
# calcula el coste total y muestra el resultado en la consola


        
 
         
        

    
