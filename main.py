from tkinter import *
from tkinter import ttk

import calculator
#from calculator import *

def imprimeuno():
    print(1)

class MainApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        #self.geometry("272x300")
        self.title("Calculadora")

        self.display = calculator.Display(self)
        self.display.pack(side=TOP, fill=BOTH, expand=True)

        self.teclado = calculator.Keyboard_con_diccionario(self)
        self.teclado.pack(side=TOP)

        #self.teclado = ttk.Frame(self, width=calculator.WIDTH*4, height=calculator.HEIGHT * 5)
        #self.teclado.grid_propagate(0)#con esto lo que conseguimos es que salga toda la pantalla, y no solo los botones que hemos creado
        #self.teclado.pack(side=TOP, fill=BOTH, expand=True)

        

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()