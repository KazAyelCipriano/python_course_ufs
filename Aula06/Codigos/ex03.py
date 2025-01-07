from Tkinter import *
import tkMessageBox

window = Tk()
window.title("Terceira Tela")
window.geometry("400x400")

# Variavel dos labels
txt_lbA = StringVar()
txt_lbB = StringVar()

def msg(txt_msg):
    tkMessageBox.showinfo( "Tela de Msg", "mensagem::"+txt_msg)

conta = 0
def conta_click():
    global conta, txt_lbA
    conta+=1
    txt_lbA.set("clicks::"+str(conta))

txt = Entry(window)
txt.insert(0,'Digite sua mensagem')
txt.grid(row=1, column=3)

bt1 = Button(window, text = "Envia msg", command = lambda:msg(txt.get()))
bt1.grid(row=1)

lbA = Label(window, textvariable=txt_lbA)
txt_lbA.set("Inciando Contagem")
lbA.grid(row=3,column=2,columnspan=2)

bt2 = Button(window, text = "++", command = conta_click)
bt2.grid(row=3,column=0)

window.mainloop()
#Nada depois desse codigo eh executado
