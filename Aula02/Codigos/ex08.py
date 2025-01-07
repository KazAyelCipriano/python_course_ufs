#!/usr/bin/python

n=raw_input('Digite um valor:')
print n
a=0
try:
    c = int(n)
    print 'c:', c
    print c/a
except ValueError:
    print 'Nao foi possivel converter o valor'
except:
    print 'Alguma coisa deu ruim!!!'
else:
    print 'Deu bom!!'



'''try:
    # codigo a ser executado
except:
    # codigo executado se ocorrer qualquer excecao
else:
    # codigo executado se nao ocorrer excecao'''

