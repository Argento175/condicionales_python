# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de práctica numérica

# Comparadores
# Ingrese dos números cualesquiera y realice las sigueintes
# comparaciones entre ellos
numero_1 = int(input('Ingrese el primer número:\n'))        # 30

numero_2 = int(input('Ingrese el segundo número:\n'))       # -10

# Compare cual de los dos números es mayor
# Imprima en pantalla según corresponda

# Verifique si el numero_1 positivo, negativo o cero
# Imprima el resultado en cada caso

# Verifique si el numero_1 es mayor a 0 y menor a 100
# Imprima en pantalla si se cumple o no la condición

# Verifique si el numero_1 es menor a 10 o el numero_2
# es mayor a -2
# Imprima en pantalla si se cumple o no la condición
if numero_1 > numero_2:
    print("El primer número,", numero_1," es mayor que el segundo número,", numero_2)
else:
    print("El segundo número,",numero_2," es mayor que el primer número,", numero_1)

if numero_1 > 0:
    print("El número",numero_1,"es positivo.")
elif numero_1 < 0:
    print("El numero",numero_1,"es negativo.")
else:
    print("El número",numero_1,"es el 0!")

if numero_1 > 0 and numero_1 < 100:
    print("El número",numero_1,"está entre 0 y 100.\nCumple la condición.")
else:
    print("El número",numero_1,"no está entre 0 y 100.\nNO cumple la condición.")

if numero_1 < 10 or numero_2 > -2:
    print("La condición se cumple.")
else:
    print("La condición no se cumple.")