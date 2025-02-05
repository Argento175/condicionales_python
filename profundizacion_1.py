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
Realice un programa que solicite por consola 2 números
Calcule la diferencia entre ellos e informe por pantalla
si el resultado es positivo, negativo o cero.
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio
num_1 = float(input("Ingresá un número cualquiera (entero o decimal)\n"))
num_2 = float(input("Ingresá otro número cualquiera... (también puede ser decimal)\n"))
resta = float(num_1-num_2)
if resta > 0:
    print("El resultado es positivo:",resta)
elif resta < 0:
    print("El resultado es negativo:",resta)
else:
    print("El resultado es 0!!")