from Tkinter import *
import ttk ## Used to create separators
## Libraries used to plot graphs
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import random, math

class Application:
    def __init__(self, master):
        self.master=master
        self.master.title('Application Screen')
        self.master.geometry("700x500")

        ## Create the main frame
        self.mainFrame = Frame(master)
        self.mainFrame.grid() # Creates the main frame
       
        ## Create widgets
        Button(self.mainFrame, text = "Gera", command = self.gera_grafico).grid(row=1, column=0)
        ttk.Separator(self.mainFrame,orient=HORIZONTAL).grid(row=0, columnspan=6,sticky="ew")
        ttk.Separator(self.mainFrame,orient=VERTICAL).grid(row=0, column=1,rowspan=5,sticky="ns")
        ttk.Separator(self.mainFrame,orient=HORIZONTAL).grid(row=5, columnspan=6,sticky="ew")
        
        ## First plot
        self.fig = Figure()
        self.ax = self.fig.add_subplot(111)
        self.fig.set_size_inches(8, 6)
        self.canvas = FigureCanvasTkAgg(self.fig,master=self.mainFrame)
        self.canvas.get_tk_widget().grid(row=1, column=2, rowspan=4, columnspan=4,sticky=W)


    def gera_grafico(self):
        dados=[]
        tempo=[]
        for i in range(100):
            tempo.append(i)
            dados.append(5*math.sin(i/5)+random.random())
        self.ax.cla()
        self.ax.plot(tempo,dados)
        self.canvas.show()

window = Tk()
myApp = Application(window)
window.mainloop()
#Nada depois desse codigo eh executado
