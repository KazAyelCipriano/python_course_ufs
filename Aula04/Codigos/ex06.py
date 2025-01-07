# Funcao Basica
def myFunc(af,bf,l1f,l2f):
    af+=2
    bf=5
    l1f.extend([4,5,6])
    l2f =[4,5,6]
    print '[f]a:',af,' b:',bf
    print '[f]l1:',l1f,' l2:',l2f

a = 7
b = 7
l1 = [1,2,3]
l2 = [1,2,3]
l3 = l1
l4=[];l4.extend(l1)
myFunc(a,b,l1,l2)
print '[m]a:',a,' b:',b
print '[m]l1:',l1,' l2:',l2
print 'l3:',l3
print 'l4:',l4
