# Vamos a ver los operadores aritméticos
#---
print(3+4) #Nos hace la suma
print(4-3) #Nos hace la resta
print(3*4) #Nos hace la multiplicación
print(4/3) #Nos hace la división
#---
print(4%3) #Nos hace el módulo o sea saca el resto
print(10//3) #Nos devuelve el último entero completo de la división
print(2**3) #Nos devuelve un exponente, el primero elevado al segundo
#---
print("Hola"+" Mundo") #Concatena las cadenas de texto
#--- 
print("Hola "+str(5)) #Hacemos el casting para poder concatenar
print("Hola "*5) #Imprime en la misma linea N veces lo escrito

#---
# Operadores comparativos
#---
print(3>4)
print(3<4)
print(3>=4)
print(3<=4)
print(3==4)
print(3!=4)
#---
print("Hola"=="Hola")
print("Hola"=="hola")
print("B">"A") #Comprueba ordenación alfabética por ASCII

#---
# Operadores Lógicos
#---
print(3>4 and "Hola">"Python") #Equivalente a &&
print(3<4 or "Hola">"Python") #Equivalente a ||
print(not(3>4)) #Equivalente a !()