# Se te encomienda la misión de fabricar un sistema en el cuál pueda
# guardar la lista de nombres de personas asistentes a un evento.
lista = []

# Necesito tener la capacidad de anotar el nombre completo de la persona
# en 1 sólo input. Además, debo de ser capaz de confirmar si quiero
# insertar el nombre de la persona. Sí el nombre está registrado, que
# notifique al operador que este nombre ya está registrado.
nombreCompleto = input()
opcion = input()
try:
    print(lista.index(nombreCompleto) == None)
except:
    print("Hubo un error")

# También, necesito visualizar la lista total de personas que llevo
# registradas en la lista junto con su índice respectivo.
print(lista)

# El sistema debe de ser capaz de permitir al usuario modificar el
# nombre por su indice respectivo.
lista[0] = "valor nuevo"

# El sistema debe de ser capaz de permitir al usuario borrar el nombre
# por su indice respectivo.
lista.pop(0)
