a='a02';b='Acasa'; c=u'1235'; d=u'12.35'
print 'a:{} b:{} c:{} d:{}'.format(a,b,c,d)
print 'a:: AlNum:{} Alpha:{}'.format(a.isalnum(), a.isalpha())
print 'b:: AlNum:{} Alpha:{}'.format(b.isalnum(), b.isalpha())
print 'c:: Di:{} Nu:{} De:{}'.format(c.isdigit(),c.isnumeric(), c.isdecimal())
print 'd:: Di:{} Nu:{} De:{}'.format(d.isdigit(),d.isnumeric(), d.isdecimal())
e='1235'
print 'e:{} :: Di:{}'.format(e,e.isdigit())
print b.istitle()
seq=['1','2','3','4','5']
s='-'
print 'join: ', s.join(seq)
