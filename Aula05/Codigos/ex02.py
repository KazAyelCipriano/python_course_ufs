class Caixa:
    n_cx=0
    def __init__(self, c,l,h):
        self.c = c
        self.l = l
        self.h = h

        Caixa.n_cx+=1
        self.__name = 'caixa '+ str(Caixa.n_cx)
    
    def volume(self):
        return self.c*self.l*self.h

    def area(self):
        return 2*self.c*self.l +2*self.c*self.h + 2*self.l*self.h

    def get_name(self):
        return self.__name


cx1 = Caixa(2,3,4)
cx2 = Caixa(10,3,3)
cx3 = Caixa(10,3,3)

print('Numero de caixas: {}'.format(Caixa.n_cx))
print('caixa {}: H {} Volume {} e Area {}'.format(cx2.get_name(),cx2.h,cx2.volume(), cx2.area()))
print('caixa {}: Volume {} e Area {}'.format(cx2.__name,cx2.h, cx2.volume(), cx2.area()))

