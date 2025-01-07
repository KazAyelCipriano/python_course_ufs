#!/usr/bin/python
a=1; b=7; c=15

if (a>=b):
    print "a>=b"
elif (b<c):
    print "a<b<c"
else:
    print "a<b e b>=c"

lista=[1,2,3,4,5]

print "lista:", lista
if (a in lista): print "a estah na lista"
else: print "a nao estah na lista"

if (b in lista): print "b estah na lista"
else: print "b nao estah na lista"

if (b in lista) or (a in lista): print "a ou b estao na lista"
elif (b in lista) and (a in lista): print "a e b estao na lista"

if (b not in lista) and (c not in lista): print "nem b e nem c estao na lista"
    
