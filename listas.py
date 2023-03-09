# Aquí vamos a aprender sobre las listas

mi_lista = list()
mi_lista = [3,13,69,616,3,17,3]

print(mi_lista)
print(len(mi_lista))

#Permite crear listas de objetos directamente
mi_otra_lista = [29, 1.69, "Pache", "Devs"]

print(mi_otra_lista)
print(type(mi_otra_lista))

#[N] permite ver el elemento N de la lista
#Si ponemos números negativos mirará desde el último que es [-1]
print(mi_otra_lista[0])
#Count te dice cuantas veces se encuentra el elemento en la lista
print(mi_lista.count(3))

#Igualamos cada elemento de la lista a un variable
#Importante el orden
edad, altura, nombre, tipo = mi_otra_lista

print(edad)