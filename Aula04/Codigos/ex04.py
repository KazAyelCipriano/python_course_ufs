lista=[0,1,2,'00', 3]
print lista
lista.append(4)
lista.extend([5,6,7,5,5,'AA',8])
print lista
lista.insert(2,'Aqui')
print lista
print 'Quantos 5::', lista.count(5)
print '.pop()::',lista.pop()
print lista
print '.pop(2)::',lista.pop(2)
print lista
print '.remove(5)::',lista.remove(5)
print lista
lista.reverse()
print lista
lista.sort()
print lista
