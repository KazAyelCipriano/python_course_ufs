#!/usr/bin/python

i=0
while (i<10):
    print "i:", i
    i+=2;

k=0
while (True):
    print "k:", k
    k+=3
    if (k>=17):
        print "k>17\nsaindo..."
        break

print "Saiu com k:",k
