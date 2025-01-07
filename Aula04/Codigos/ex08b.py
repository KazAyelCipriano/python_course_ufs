#!/usr/bin/python
v1=8; v2=10 # Variaveis globais
def func1():
    print 'v1:{} v2:{}'.format(v1,v2)

def func2():
    print 'v1:{} v2:{}'.format(v1,v2)
    v1=7

func1()
func2()
