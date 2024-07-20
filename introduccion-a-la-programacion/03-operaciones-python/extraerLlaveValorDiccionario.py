inventario = {
    "Manzana": 15,
    "Peras": 20,
    "Naranjas": 5
}

for nombre, cantidad in inventario.items():
    print(f"El producto {nombre} tiene {cantidad} en stock")