#Vamos a aprender sobre las variables
#Nombre variable = valor de la variable
#En python se usa snakecase, todo en minúsculas y
#las palabras separadas por guión bajo

#No hay que declarar que guardará la variable
mi_nombre = "Samuel Jiménez"
mi_edad = 29
mi_altura = 1.69

print(mi_nombre)
print(mi_edad)
print(mi_altura)

#Podemos imprimir varias variables de una separadas por comas, entre
#cada una habrá un espacio
print("Soy", mi_nombre, "tengo", mi_edad, "años y mido", mi_altura)

#Podemos hacer un casting como en Java
mi_edad_str = str(mi_edad)
print(type(mi_edad)) #Es int
print(type(mi_edad_str)) #Es String

#len devuelve la longitud del str
print(len(mi_edad_str))

#No se pueden crear constantes, se puede pero no se puede definir directamente