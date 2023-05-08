
producto_analizar = input("Ingrese producto a analizar: ")

fondas = []
precio_min= 0
precio_max= 0
fonda_precio_min= 0
fonda_precio_max= 0
cantidad_fondas_con_producto= 0

continuar = True
while continuar == True:
    nombre_fonda = input("Ingrese nombre de la fonda: ")
    if nombre_fonda == "FIN":
        break
    cantidad_productos_fonda_uno = int(input("Cantidad de productos que vende la fonda: "))
    productos = []
    for i in range(cantidad_productos_fonda_uno):
        producto = input("Nombre producto " + str(i + 1) + ": ")
        precio = int(input("Precio del producto " + str(i + 1) + ": "))

        if producto == producto_analizar:
            cantidad_fondas_con_producto += 1
            if precio_min == 0 or precio < precio_min:
                precio_min = precio
                fonda_precio_min = nombre_fonda
            if precio_max == 0 or precio > precio_max:
                precio_max = precio
                fonda_precio_max = nombre_fonda

if precio_min is None or precio_max is None:
    print("No existen datos para generar el rango de precios.")
else:
    print(f"El rango de precios del producto {producto_analizar} es de {precio_min} a {precio_max}.")
    print(f"La fonda que vende el producto al menor precio es {fonda_precio_min} a {precio_min}.")
    print(f"La fonda que vende el producto al mayor precio es {fonda_precio_max} a {precio_max}.")
    print(f"Hay un total de {cantidad_fondas_con_producto} fondas que ofrecen el producto {producto_analizar}.")    
    
