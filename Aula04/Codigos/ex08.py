#!/usr/bin/python
v1=8; v2=10 # Variaveis globais
def volRect(b,h):
    global v2
    v1=100
    v2=200
    print 'v1:{} v2:{}'.format(v1,v2)
    return b*b*h

volRect(h=4,b=10)
print 'v1:{} v2:{}'.format(v1,v2)
