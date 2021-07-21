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
Realice un programa que solicite ingresar tres valores de temperatura
De las temperaturas ingresadas por consola determinar:
1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
3 - ¿Cuál es el promedio de las temperaturas ingresadas?

En cada caso imprimir en pantalla el resultado

IMPORTANTE: Para ordenar las temperatuas debe utilizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido. Recomendamos pensar bien este problema de lógica con un lápiz y papel.
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio
temp_1 = float(input("Ingrese un primer valor de temperatura:\n"))          # 36.0
temp_2 = float(input("Ingrese un segundo valor de temperatura:\n"))         # 28.7
temp_3 = float(input("Ingrese un tercer valor de temperatura:\n"))          # 12.2

if temp_1 > temp_2 and temp_1 > temp_3:
    print("El primer valor de temperatura, (",temp_1,"), es el valor mayor.")
elif temp_2 > temp_1 and temp_2 > temp_3:
    print("El segundo valor de temperatura, (",temp_2,"), es el valor mayor.")
else:
    print("El tercer valor de temperatura, (",temp_3,"), es el valor mayor.")

# Desarrollé el ejercicio dando como resultado final la primera opción como válida...
# Aunque creo que el planteo es correcto en caso de que la opción fuese otra.