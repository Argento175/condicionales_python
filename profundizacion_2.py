# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un programa que solicite el ingreso de tres números
enteros, y luego en cada caso informe si el número es par
o impar.
Para cada caso imprimir el resultado en pantalla.
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio
num_1 = int(input("Ingresá un número cualquiera... (ENTERO, por favor!)\n"))
num_2 = int(input("Ingresá otro número... (ENTERO también!\n"))
num_3 = int(input("Para terminar, ingresá un último número... (ENTERO, of course!\n"))
res_1 = (num_1 % 2)
res_2 = (num_2 % 2)
res_3 = (num_3 % 2)

if res_1 == 0 :
    print("El primer número,",num_1,", es par.")
else:
    print("El primer número,",num_1,", es impar.")

if res_2 == 0 :
    print("El segundo número,",num_2,", es par.")
else:
    print("El segundo número,",num_2,", es impar.")

if res_3 == 0 :
    print("El tercer número,",num_3,", es par.")
else:
    print("El tercer número,",num_3,", es impar.")
