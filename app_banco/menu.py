import tkinter as tk
from login import Login 
from register import Register
class Menu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Menu")
        self.resizable(0,0)
        self.componentes()
        self.mainloop()

    def componentes(self):
        #Label
        tk.Label(self, text="Iniciar Sesion:",font=("Arial",14)).place(relx=.5, rely=.3,anchor="center")
        tk.Label(self, text="Registrate:",font=("Arial",14)).place(relx=.5, rely=.7,anchor="center")
        #Botones
        tk.Button(self, text="Iniciar Sesion", command= self.login).place(relx=.5, rely=.45, anchor="center")
        tk.Button(self, text="Registrate", command=self.registrarse).place(relx=.5, rely=.85, anchor="center")

    def login(self):
        self.destroy()
        Login()
    def registrarse(self):
        self.destroy()
        Register()

if __name__ == "__main__":
    Menu()