import tkinter as tk
import csv
from tkinter import messagebox
from banco import Banco

class Login(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Inicio de sesión")
        self.resizable(0,0)
        self.componentes()
        self.mainloop()

    def componentes(self):
        tk.Label(self, text="Login").place(relx=.5,rely=.1, anchor="center")
        tk.Label(self, text="Usuario:").place(relx=.5, rely=.25,anchor="center")
        tk.Label(self, text="Contraseña:").place(relx=.5,rely=.5,anchor="center")
        self.entry_usuario = tk.Entry(self)
        self.entry_usuario.place(anchor="center",relx=.5, rely=.35)
        self.entry_contrasena = tk.Entry(self)
        self.entry_contrasena.place(anchor="center",relx=.5, rely=.62)
        tk.Button(self, text="Iniciar Sesión", command=self.verificar).place(anchor="center",relx=.5, rely=.8)


    def verificar(self):
        usuario = self.entry_usuario.get()
        contrasena = self.entry_contrasena.get()
        with open("C:\\Users\\Admin\\Documents\\PYTHON\\app_banco\\registro.txt" , "r") as archivo:
            datos = csv.reader(archivo)
            for linea in datos:
                if linea[2] == usuario and linea[3] == contrasena:
                    messagebox.showinfo("Correcto","Verificación Correcta puede continuar")
                    self.destroy()
                    Banco(usuario, contrasena)
                else:
                    messagebox.showerror("Error","Vuelva a intentar: Login")


if __name__ =="__main__":
    Login()