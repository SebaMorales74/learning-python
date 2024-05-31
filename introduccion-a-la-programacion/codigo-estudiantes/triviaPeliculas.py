correctas=0
print("¡¡JUEGO DE PREGUNTAS SOBRE PELICULAS!!")
print("¡COMENCEMOS!")
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

print("¿Quien protagonizo la pelicula Soy Leyenda?")
print("1) Don Ramon.")
print("2) Will Smith.")
print("3) Brad Pitt.")
print("4) La Roca.")
preg1=int(input("Respuesta: "))
if preg1==2:
    print("¡Correcto!")
    correctas+=1
else:
    print("Incorrecto.")

print("¿Que pelicula esta relacionado con el mundo del I.A?")
print("1) Detroit.")
print("2) Call of Duty.")
print("3) The matrix.")
print("4) Volver al Futuro")
preg2=int(input("Respuesta: "))
if preg2==3:
    print("¡Correcto!")
    correctas+=1
else:
    print("Incorrecto.")

print("¿Que Juego tiene una PELICULA? ")
print("1) Resident Evil.")
print("2) Detroit.")
print("3) Call of Duty.")
print("4) The Last of Us.")
preg3=int(input("Respuesta: "))
if preg3==1:
    print("Correcto.")
    correctas+=1
else:
    print("Equivocado.")

print("RESULTADOS:")

if correctas==3:
    print("3/3 ¡EXCELENTE! SABES DE PELICULA :).")
elif correctas==2:
    print("2/3 BIEN")
elif correctas==1:
    print("1/3 DEFICIENTE")
elif correctas==0:
    print("0/3 A VER MAS PELICULAS.")