#!/usr/bin/python

n=raw_input('Digite um valor:')
print n

try:
    c = int(n)
    print 'c:', c
except:
    print 'Deu ruim!!!'
else:
    print 'Deu bom!!'

