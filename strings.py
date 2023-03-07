# Empezamos con los String
my_string = "Pachito"

print(len(my_string))

#Podemos concatenar Strings
print(my_string+" "+'McPacherson')

#Podemos añadir saltos de líneas con \n
print(my_string +"\nRaza: Procyon Loctor")

#Podemos añadir tabulaciones con \t
print("\t"+my_string+" "+'McPacherson')

#Podemos poner los caracteres especiales metiendo otra /
print("\\n vale para hacer saltos de línea \\t sirve para tabular")

#Podemos formatear Strings
name, ocupacion, edad = "Pache", "Devs", 29
#Forma primera
print("Yo soy {}, soy un {} y tengo {} años".format(name, ocupacion, edad))
#Forma segunda, muy recomendable
print("Yo soy %s, soy un %s y tengo %d años" %(name, ocupacion, edad))
#Inferencia de datos, la más elegante
print(f"Yo soy {name}, soy un {ocupacion} y tengo {edad}")

#Desempaquetado de caracteres
#Podemos crear una variable nueva y luego asignar otra
#subvariable para cada caracter de la variable
language = "python"
a,b,c,d,e,f = language
print(a)
print(c)
print(e)
print(b)
print(d)
print(f)

#División de Strings
#Pilla de la posición de la izquierda hasta la de la derecha
language_slice = language[1:3] 
print(language_slice)

#Pilla de la posición izda al final
language_slice = language[1:] 
print(language_slice)

#Pilla del inicio hasta la posición de la derecha
language_slice = language[:3] 
print(language_slice)

#Pilla desde el final la posición indicada empezando en -1
language_slice = language[-2] 
print(language_slice)

#Cogemos todo pero nos saltamos los pares (orden natural)
language_slice = language[0:6:2] 
print(language_slice)

#Dar la vuelta
reversed_language = language[::-1]
print(reversed_language)

#Funciones
print(language.capitalize())#Pone la primera en mayúscula
print(language.upper())#Todo en mayúscula
print(language.count("t"))#Cuenta cuantas veces se repite lo colocado
print("478512".isnumeric())#Dice si es un número aunque sea String
print(language.lower()) #Todo a minúsculas
print(language.upper().isupper()) #Podemos concatenar funciones
print(language.startswith("Py")) #Dice si empieza con lo introducido
print(language.endswith("on"))#Dice si termina con lo introducido