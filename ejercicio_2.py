# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Comparadores
# Ingrese dos palabras cualesquiera y realice las sigueintes
# comparaciones entre ellas
texto_1 = str(input('Ingrese la primera palabra:\n'))       # Perro

texto_2 = str(input('Ingrese la segunda palabra:\n'))       # Gato

# Compare cual de las dos palabras es mayor (alfabéticamente)
# Imprima en pantalla según corresponda
if (texto_1) > (texto_2):
    print(texto_2, "está antes que", texto_1)
else:
    print(texto_1, "está antes que", texto_2)

# Compare cual de las dos palabras tiene mayor
# cantidad de letras
# Imprima en pantalla según corresponda
if len(texto_1) > len(texto_2):
    print(texto_1, "es más largo/a que", texto_2)
else:
    print(texto_2, "es más largo/a que", texto_1)

# Verifique si la primera letra de la primera palabra
# es mayor a la primera letra de la segunda palabra
# Imprima en pantalla según corresponda
if (texto_1[0]) > (texto_2[0]):
    print("La primera letra", (texto_1[0]),"de la palabra", texto_1,"es mayor que la primera letra",(texto_2[0]),"de la palabra",texto_2)
else:
    print("La letra", (texto_2[0]),"de la palabra", texto_2,"es mayor que la primera letra",(texto_1[0]),"de la palabra",texto_1)

copia_texto_1 = texto_1  # Copia de la variable texto_1

# Verifique que copia_texto_1 es igual a texto_1
# Imprima en pantalla según corresponda
if copia_texto_1 == texto_1:
    print("La copia es igual al original.")
else:
    print("La copia es diferente al original.")

# Verifique que copia_texto_1 es distinta a texto_2
# Imprima en pantalla según corresponda
if copia_texto_1 != texto_2:
    print(copia_texto_1,"es diferente a",texto_2)
