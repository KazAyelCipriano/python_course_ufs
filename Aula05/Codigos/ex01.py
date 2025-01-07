class Caixa:
    def __init__(self, c,l,h):
        self.c = c
        self.l = l
        self.h = h
    
    def volume(self):
        return self.c*self.l*self.h

    def area(self):
        return 2*self.c*self.l +2*self.c*self.h + 2*self.l*self.h


cx1 = Caixa(2,3,4)
cx2 = Caixa(10,3,3)

print('caixa {}: Volume {} e Area {}'.format(1,cx1.volume(), cx1.area()))
print('caixa {}: Volume {} e Area {}'.format(2,cx2.volume(), cx2.area()))
