texto='Casa bola casa Casa caso Bola dolar'
print 'casa:{} bola:{}'.format(texto.count('casa'),texto.count('bola'))
print 'casa:{} bola:{}'.format(texto.lower().count('casa'),texto.lower().count('bola'))
print 'Start:Cas:{} Ends:lar:{}'.format(texto.startswith('Cas'),texto.endswith('lar'))
print 'Start:sa:{}'.format(texto.startswith('sa',2,10))
print 'find:: as:{} ol:{}'.format(texto.find('as'),texto.find('ol'))
print 'find:: as:{} ol:{}'.format(texto.rfind('as'),texto.rfind('ol'))
print 'find:: as:{} ol:{}'.format(texto.rfind('as',2,20),texto.rfind('ol',2,20))

seq=['1','2','3','4','5']
s='-'
print 'join: ', s.join(seq)
