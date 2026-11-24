
def calcular_cantidad_a_pedir(stock_actual, stock_minimo):
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    else:
        return 0


inventario = []

for i in range(5):
    print(f"\nArtículo {i + 1}")
    codigo = input("Código del artículo: ")
    nombre = input("Nombre del artículo: ")
    stock_actual = int(input("Stock actual: "))
    stock_minimo = int(input("Stock mínimo requerido: "))

    inventario.append([codigo, nombre, stock_actual, stock_minimo])



print("-" * 40)
print("\nREPORTE DE REABASTECIMIENTO")
print("-" * 40)

for articulo in inventario:
    codigo, nombre, stock_actual, stock_minimo = articulo
    cantidad_a_pedir = calcular_cantidad_a_pedir(stock_actual, stock_minimo)
    print(f"Artículo: {nombre} (Código: {codigo})")
    print(f"  Stock actual: {stock_actual}")
    print(f"  Stock mínimo requerido: {stock_minimo}")
    print(f"  Cantidad a pedir: {cantidad_a_pedir}")
    print()