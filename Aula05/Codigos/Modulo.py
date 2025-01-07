class Caixa:
    def __init__(self,c,l,h):
        self.c = c
        self.l = l
        self.h = h

    def volume(self):
        return self.c*self.l*self.h

    def area(self):
        return 2*self.c*self.l +2*self.c*self.h + 2*self.l*self.h
