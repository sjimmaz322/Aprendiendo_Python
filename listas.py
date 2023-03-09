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

#Podemos concatenar listas directamente
print(mi_lista + mi_otra_lista)
#Tanto en el print como en otra variable lista
lista_completa = mi_lista + mi_otra_lista
print(lista_completa)

#mi_lista = "Hola Python"
#print(mi_lista)
#print(type(mi_lista))

#Podemos añadir elementos a la lista, con append lo pone al final
mi_otra_lista.append("PacheDevs")
print(mi_otra_lista)

#Insert pide el índice donde lo pondrá
mi_otra_lista.insert(0, "Samuel")
print(mi_otra_lista)

#También podemos elminiar
#Ponemos directamente el elemento a eliminar
#Elimina el primer elemento que encuentre
mi_otra_lista.remove("Samuel")
print(mi_otra_lista)

#Pop quita el último
#Pero devuelve el valor que hemos quitado
"""
mi_otra_lista.pop()
print(mi_otra_lista.pop())
print(mi_otra_lista)

#Si pasamos un número borrará ese índice
mi_otra_lista.pop(2)
print(mi_otra_lista)
"""
#del borra ese valor, no devuelve nada
#del mi_otra_lista[0]
#Clear limpia completamente la lista, la deja vacia
#mi_otra_lista.clear()
#print(mi_otra_lista)

#Así podemos cambiar el valor del índice que queramos de la lista
mi_otra_lista[0] = 700
print(mi_otra_lista)

#Podemos copiar la lista, pero son dos listas independientes
#No es paso por referencia
lista_copiada = mi_otra_lista.copy()
mi_otra_lista.clear()

print(mi_otra_lista)
print(lista_copiada)

#Con reverse podemos darle la vuelta a la lista
#NO se puede hacer dentro del print
lista_copiada.reverse()
print(lista_copiada)

#Ordena por orden natural si todos los elementos son del mismo tipo
mi_lista.sort()
print(mi_lista)

#Vamos a ver como hacer sublistas
#Usando los subíndices como en las variables