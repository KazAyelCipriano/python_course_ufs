from Tkinter import *
import tkMessageBox

class Application:
    def __init__(self, master):
        self.master=master
        self.master.title('Application Screen')
        self.master.geometry("400x200")

        # Label StringVar
        self.txt_lbA = StringVar()
        # Accumulator
        self.count=0

        ## Create the main frame
        self.mainFrame = Frame(master)
        self.mainFrame.grid() # Creates the main frame
       
        ## Create widgets
        self.txt = Entry(self.mainFrame)
        self.txt.grid(row=1, column=3,columnspan=2)
        self.txt.insert(0,'Digite sua mensagem')

        # Notice that I did not create an attribute
        Button(self.mainFrame, text = "Envia msg", command = self.msg).grid(row=1, column=0)
        Button(self.mainFrame, text = "++", command = self.conta_click).grid(row=3,column=0)
        Label(self.mainFrame, textvariable=self.txt_lbA).grid(row=3,column=2,columnspan=2)

    def msg(self):
        tkMessageBox.showinfo( "Tela de Msg", "mensagem::"+self.txt.get())

    def conta_click(self):
        self.count+=1
        self.txt_lbA.set("clicks::"+str(self.count))

window = Tk()
myApp = Application(window)
window.mainloop()
#Nada depois desse codigo eh executado
