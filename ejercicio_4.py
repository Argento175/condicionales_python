# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

texto_1 = '5'
texto_2 = '7'

# 1-Verifique cual de los dos textos es mayor alfabéticamente
# La comparación alfabética es aquella que se logra cuando
# se utiliza el operador mayor o menor con Strings (textos)
# Imprima en pantalla según corresponda
if (texto_1[0]) > (texto_2[0]):
    print(texto_1)
else:
    print(texto_2)

# 2-Transforma esas variables tipo texto en variables numéricas con (int)
# y almacénalas en nuevas variables.
# Compare las nuevas variables para ver cual es mayor o menor
# utilizando los operadores correspondientes
# ¿Cuál de las nuevas variables es mayor?
# Imprima en pantalla según corresponda
x = int(texto_1)
y = int(texto_2)
if x > y:
    print(x,"es mayor que",y)
elif x < y:
    print(y,"es mayor que",x)
else:
     print("Ambos números son iguales!!")
# Para pensar!
# ¿Por qué cree que texto_2 es mayor a texto_1?
# Siendo números tiene sentido, pero son caracteres, texto,
# aún así el operador arroja el mismo resultado que con las
# variables numéricas, cierto? ¿Por qué creen que es así?
# Esta pregunta estará repetida en el Campus para que puedan
# responder.
# NOTA: La respuesta no se encuentra en el apunte, sino en Google ;)

'''
 Resp: '7' es el número "siete", es decir, comienza con la letra 's', que es 55 en código ASCII...
 En tanto que '5' (el número 5), comienza con la letra 'c', que es 53 en el mismo código...
 55 > 53 ---> 7 > 5 ;) 
'''