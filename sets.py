# Vamos a ver los sets

mi_set = set()
mi_otro_set = {}

print(type(mi_set))
print(type(mi_otro_set))  # Dice que es un dict

mi_otro_set = {"Pache", "Devs", 29}
print(type(mi_otro_set))  # Ahora dice que es un set
print(len(mi_otro_set))

# print(mi_otro_set[0]) no podemos acceder a los elementos como con una lista

print(mi_otro_set)

mi_otro_set.add("Mapache")
# No admite elementos repetidos
mi_otro_set.add("Mapache")

print(mi_otro_set)  # Un set no es una estructura ordenada, no tiene índice

# Como comprobar si un elemento está en un Set
print("Pache" in mi_otro_set)
print("Pachito" in mi_otro_set)

mi_otro_set.remove("Mapache")
print(mi_otro_set)

mi_otro_set.clear()
print(len(mi_otro_set))

del mi_otro_set  # Borramos la variable mi_otro_set completamente
# print(mi_otro_set) # Dice que no existe la variable

# Si tenemos un Set podemos convertirlo en List
# Como el Set se crea en orden aleatorio no es recomendable
mi_set = {"Pache", "Devs", 29}
# mi_lista = list(mi_set)
# print(mi_lista[0])

mi_otro_set = {"Java", "HTML", "Python"}

# Podemos concatenar Sets con union
mi_nuevo_set = mi_set.union(mi_otro_set)

print(mi_nuevo_set)
# Si hacemos un union en un set hacemos el union solo para esa ejecución
print(mi_nuevo_set.union({"C#", "JavaScript"}))

# Imprime los elementos que no están contenidos dentro del set pasado
print(mi_nuevo_set.difference(mi_set))
