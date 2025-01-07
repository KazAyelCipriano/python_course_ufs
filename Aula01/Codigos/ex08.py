#!/usr/bin/python
seq=range(1,5)
print seq

for i in seq:
    print "i:",i

for i in range(17,23):
    print "i:",i

nome = 'Jose Gilmar'
print nome
for letra in nome:
    print letra

lista = [1,3,'casa',5.431,'azul', 'bolo']
print lista
for elemento in lista:
    print elemento

for k in range(0,len(lista)):
    if (lista[k]=='azul'): 
        print "Elemento encontrado na posicao ", k
    else: print lista[k]

lista2=['casa', 'bolo', 'bola', 'dudu', 'bala']
print lista2
for k in range(0,len(lista2)):
    if ('a' in lista2[k]): 
        print lista2[k], " possui a letra a"

