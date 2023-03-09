# Vamos a ver que son las tuplas y como se trabaja con ellas

# Una tupla es un conjunto de valores

# Así creamos tuplas
mi_tupla = tuple()
mi_otra_tupla = ()

# Vemos que es tipo tuple
print(type(mi_tupla))

mi_tupla = (29, 1.69, "Pache", "Devs")
print(mi_tupla)

print(mi_tupla[0])
print(mi_tupla[-1])

# Count igual que en las listas
print(mi_tupla.count("Pache"))

# Index nos indica el índice donde se encuentra lo buscado
# Muestra el primero que encuentra
# Se puede usar en lista también
# Si peta es porque no ha encontrado lo buscado
print(mi_tupla.index("Pache"))

# mi_tupla[1] = 1.70
# print(mi_tupla)
# Las tuplas son inmutables, no deja cambiar valores
# Tampoco deja añadir o borrar elementos

mi_otra_tupla = (35, 60, 30)
print(mi_tupla+mi_otra_tupla)

# Podemos concatenar tuplas, pero no modificar
mi_tupla_sumada = mi_tupla+mi_otra_tupla
print(mi_tupla_sumada)

# Igualmente podemos sacar slices
print(mi_tupla_sumada[0:3])

# Si queremos una tupla mutable en verdad lo que queremos es una lista

mi_otra_tupla = list(mi_otra_tupla)
# Ahora mi_otra_tupla es una lista
print(type(mi_otra_tupla))
mi_otra_tupla = tuple(mi_otra_tupla)
# Ahora mi_otra_tupla es una tupla de nuevo
print(type(mi_otra_tupla))
# Al castearlo a lista ahora si podemos modificar los valores
# Y luego podríamos castearlo de nuevo a tupla

del mi_otra_tupla  # Borra completamente la tupla
