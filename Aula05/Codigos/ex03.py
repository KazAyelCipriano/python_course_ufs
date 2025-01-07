class Caixa:
    def __init__(self):
        print('Criando uma caixa')

    def set_dimensions(self,c,l,h):
        self.c = c
        self.l = l
        self.h = h

    def volume(self):
        return self.c*self.l*self.h

    def area(self):
        return 2*self.c*self.l +2*self.c*self.h + 2*self.l*self.h

class CaixaBombom(Caixa):
    def __init__(self, qt):
        self.qt = qt

cx = Caixa()
cx.set_dimensions(2,3,4)
cxBB = CaixaBombom(100)
cxBB.set_dimensions(5,3,4)

print('caixa Normal: Volume {} e Area {}'.format(cx.volume(), cx.area()))
print('caixa de Bombom: Quantidade {} Volume {} e Area {}'.format(cxBB.qt, cxBB.volume(), cxBB.area()))

