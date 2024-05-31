while True:
    opcion = int(input("""
                       Menu de opciones
                       1. Decir hola mundo
                       0. Cerrar programa
                       """))
    if opcion == 0:
        break
    elif opcion == 1:
        print("Hola mundo")
        continue
    else:
        print("TA MALO, INTENTA DENUEVO \n")
        continue