from Tkinter import *
import tkMessageBox

window = Tk()
window.title("Segunda Tela")
window.geometry("400x400")

def msg():
    tkMessageBox.showinfo( "Tela de Msg", "Alguma coisa aconteceu!!!")

bt1 = Button(window, text = "Envia msg", command = msg)
bt1.grid(row=1)
txt = Entry(window)
txt.insert(0,'Digite Seu texto')
txt.grid(row=2, column=3)

lb1 = Label(window, text="Esse texto eh fixo")
lb1.grid(row=2,columnspan=2)

window.mainloop()
#Nada depois desse codigo eh executado

