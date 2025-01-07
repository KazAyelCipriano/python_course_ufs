a = ['lista A', 1,2,3,4,5,6,7,8]
b = ['lista B', 9,8,7,6,5,4,3,2];s = ' '
## Escrevendo em arquivo
#w - escrita (do zero)
#r - leitura
#a - escrita (adicionando ao arquivo)
file = open('dados.txt','w')
file.write(s.join(str(it_a) for it_a in a))
file.write('\n')
file.write(s.join(str(it_b) for it_b in b))
file.close()
file = open('dados.txt','r')
linhas=file.readlines()
print linhas
lista1 = linhas[0].split()
lista2 = linhas[1].split()
print 'lista1::', lista1
print 'lista2::', lista2
dadosA=[];dadosB=[]
for i in range(2,len(lista1)):
    dadosA.append(float(lista1[i]))
    dadosB.append(float(lista2[i]))
print dadosA
print dadosB
