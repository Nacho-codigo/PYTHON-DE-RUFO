#PROMOCION
preguntas=["1) ¿Cuál es la función para obtener la entrada del usuario en Python?","2) ¿Qué hará el siguiente código? print(2+3)","3) ¿Cuál de las siguientes opciones es una lista en Python?","4) ¿Para que sirve python?"
,"5) ¿Para qué sirve el método upper() en Python?", "6) ¿Para qué se utiliza el bucle for en Python?","7) ¿Cómo se agrega un elemento al final de una lista en Python?","8) ¿Cual es el resultado de 5//2 ?",
"9) ¿Qué hace la función range(3) en un bucle for?", "¿Cuál es el resultado de 5*3 ?"]
opciones=["A) input()  B) print()  C) get()  D) read()", "A) Muestra 23  B) Muestra 2  C) Muestra 5  D) Muestra ERROR","A) ()  B) <>  C) ==  D) []",
"A) Desarrollo web, análisis de datos, inteligencia artificial y automatización  B) Solo para desarrollo web  C) Desarrollo de videojuegos  D) Desarrollo de software de escritorio",
"A) Convierte todas las letras de una cadena de texto a minúsculas  B) Convierte todas las letras de una cadena de texto a mayúsculas  C) Elimina los espacios en blanco de una cadena  D) Convierte una cadena a su forma más corta",
"A) Para ejecutar un bloque de código un número específico de veces  B) Para definir un condicional  C) Para declarar una variable  D) Para crear una función en Python","A) add()  B) insert()  C) extend()  D) append()",
"A) 3  B) 2  C)2,5  D) Error","A) Itera sobre los valores de 0 a 3  B) Itera sobre los valores de 1 a 3  C) Itera sobre los valores de 0 a 2  D) Ninguna de las anteriores","A) 15  B) 5  C) 2  D) 8"]
correctas=["A","C","D","A","B","A","D","B","C","A"]
notas=0
nombre=input("Bienvenido, ingrese su nombre:  ")
input(f"¡Bienvenido {nombre}! Presione ENTER para comenzar el juego...")
for x in range(len(preguntas)):
    print(preguntas[x])
    print("")
    print(opciones[x])
    print("")
    respuesta=input("Ingrese la respuesta correcta:  ").upper()
    if respuesta==correctas[x]:
        print("¡Felicidades! Respuesta correcta")
        print("")
        notas=notas+1
    else:
        print("Respuesta incorrecta")
        print("")
if notas>=6:
    print(f"Felicidades {nombre} usted aprobó con una nota de {notas}")
else:
    print(f"Lo siento por usted {nombre}, desaprobó con una nota de {notas}")   
print("¡Gracias por jugar!")