textoA = '    eliminacao    e    alteracao     ' 
textoB = '9999eliminacao9999e9999alteracao99999' 
print 'strip :', textoA.strip()
print 'lstrip:', textoA.lstrip()
print 'rstrip:', textoA.rstrip()
print 'strip :', textoB.strip('9')
print 'lstrip:', textoB.lstrip('9')
print 'rstrip:', textoB.rstrip('9')

print 'replace:', textoB.replace('9',' ')
print 'replace:', textoB.replace('9',' ',2)

from string import maketrans
intab = "aeiosh"
outtab = "@31057"
trantab = maketrans(intab, outtab)

str = "Que texto mais lindo!!!";
print str
print str.translate(trantab)
print str.translate(trantab, 'xl')

seq=['1','2','3','4','5']
s='-'
print 'join: ', s.join(seq)
