print("practica 3 OLIVER ABSALON ESTRADA LOZANO")

nombre_producto = input("Nombre del producto ")
clave_articulo = input("Clave del artículo: ")
clave_minusculas = clave_articulo.lower()
print(f"la clave del articulo correcto es: {clave_minusculas}")
precio_producto = float(input("Precio del producto: "))
cantidad_productos = int(input("Cantidad de productos: "))


total_compra = cantidad_productos*precio_producto 
print("\nResumen de la compra:")
print(f"- El producto que compraste es: {nombre_producto} "f"    Su clave es: {clave_minusculas}")
print(f"- La cantidad de artículos comprados es: {cantidad_productos}  "f"     El total de tu compra es: ${total_compra:.2f}")