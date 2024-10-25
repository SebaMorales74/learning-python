import os
from modules import *

ventas = []


def registrarCliente() -> Cliente:
    os.system("cls")
    print("1. Datos del cliente [1/2]")
    cliente = Cliente(
        rut=input("Ingrese rut del cliente: \n"),
        nombre=input("Ingrese nombre del cliente: \n"),
        apellido=input("Ingrese apellido del cliente: \n"),
        telefono=input("Ingrese telefono del cliente: \n"),
        email=input("Ingrese email del cliente: \n")
    )
    print(cliente)
    input("Presiona ENTER para continuar...")
    return cliente

def registrarEntradas() -> list:
    entradas = []
    while True:
        os.system("cls")
        print("2. Comprar entradas [2/2]")

        try:
            cantidadInfantes = int(input("Ingrese la cantidad de infantes: "))
            cantidadAdultos = int(input("Ingrese la cantidad de adultos: "))
            cantidadAdultosMayores = int(
                input("Ingrese la cantidad de adultos mayores:"))
        except ValueError:
            print("Ingresa SÓLO valores númericos 🙄")
            input("Presiona ENTER para continuar...")

        if cantidadInfantes > 0 and cantidadAdultos == 0 or cantidadInfantes > 0 and cantidadAdultosMayores == 0:
            print("Los niños DEBEN de estar acompañados por un adulto")
            input("Presiona ENTER para continuar...")

        else:
            for infante in range(cantidadInfantes):
                infante = Infante(input(f"Ingrese el nombre del responsable para el infante N°{infante+1}: "))
                entradas.append(infante)
            for adulto in range(cantidadAdultos):
                adulto = Adulto()
                entradas.append(adulto)
            for adultoMayor in range(cantidadAdultosMayores):
                adultoMayor = AdultoMayor()
                entradas.append(adultoMayor)
            break
    return entradas

def calcularTotal(entradas: list[Entrada]) -> int:
    total = 0
    for entrada in entradas:
        total += entrada.precio
    return total

def generarVenta(vendedor: Vendedor) -> Venta:
    cliente: Cliente = registrarCliente()
    entradas: list[Entrada] = registrarEntradas()
    total: int = calcularTotal(entradas)
    venta = Venta(vendedor=vendedor, cliente=cliente,
                  entradas=entradas, total=total)
    return venta

def main():
    vendedor = Vendedor(input("Ingrese el nombre del vendedor: "))
    while True:
        os.system("cls")
        print(
            f"""
            ¡Bienvenido {vendedor.nombre}!

            ==============================
            Punto de Venta - Cine Mar y ConCon
            ==============================
            1. Realizar Venta de Entradas
            2. Ver las entradas vendidas
            3. Salir
            """
        )
        try:
            opcion = int(input("Ingresa una opción [1-3]: "))
        except ValueError:
            print("Elige una opción correcta, porfavor.")
            input("Presiona ENTER para continuar...")

        if opcion == 1:
            os.system("cls")
            venta = generarVenta(vendedor)
            ventas.append(venta)
            input("Presiona ENTER para continuar...")
        elif opcion == 2:
            os.system("cls")
            for venta in ventas:
                print(venta)
            input("Presiona ENTER para continuar...")
        elif opcion == 3:
            os.system("cls")
            print("¡Adios! 🛌")
            input("Presiona ENTER para continuar...")
            break
        else:
            print("Opcion invalida ♿")
            input("Presiona ENTER para continuar...")


if __name__ == "__main__":
    main()
