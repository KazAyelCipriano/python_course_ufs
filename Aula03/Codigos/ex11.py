texto='123asczk#'
print 'min:{} max:{}'.format(min(texto),max(texto))

seq=['1','2','3','4','5']
s='-'
print 'join: ', s.join(seq)
str1='0 1 2 3 4 as 4 v asa'
str2='0 1 2-3 4 as-4-v asa'
print 'lista1:{}'.format(str1.split())
print 'lista1:{}  :max 3'.format(str1.split(' ',3))
print 'lista2:{}'.format(str2.split())
print 'lista2:{}  :com -'.format(str2.split('-'))
