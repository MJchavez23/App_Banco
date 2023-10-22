import tkinter as tk
from tkinter import messagebox
from login import Login
class Register(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Registro")
        #self.resizable(0,0)
        self.componentes()
        self.mainloop()

    def componentes(self):
        tk.Label(self, text="Registro\n(Complete todos los campos)").place(relx=.5, anchor="center",rely=.1)
        tk.Label(self, text= "Nombre: ").place(relx=.13,rely=.259)
        tk.Label(self, text= "Apellido: ").place(relx=.13,rely=.359)
        tk.Label(self, text= "Usuario: ").place(relx=.13,rely=.459)
        tk.Label(self, text= "Contraseña: ").place(relx=.13,rely=.559)
        self.entry_nombre = tk.Entry(self)
        self.entry_nombre.place(relx=.5,rely=.25)
        self.entry_apellido = tk.Entry(self)
        self.entry_apellido.place(relx=.5,rely=.35)
        self.entry_usuario = tk.Entry(self)
        self.entry_usuario.place(relx=.5,rely=.45)
        self.entry_contrasena = tk.Entry(self)
        self.entry_contrasena.place(relx=.5,rely=.55)
        tk.Button(self, text="Guardar",command=self.guardar).place(relx=.5, rely=.8, anchor="center")


    def guardar(self):
        nombre = self.entry_nombre.get()
        apellido = self.entry_apellido.get()
        usuario = self.entry_usuario.get()
        contrasena = self.entry_contrasena.get()
        if nombre and apellido and usuario and contrasena:
            with open("C:\\Users\\Admin\\Documents\\PYTHON\\app_banco\\registro.txt" , "a") as archivo:
                archivo.write(f"{nombre},{apellido},{usuario},{contrasena},0\n")
                messagebox.showinfo("Gracias!!","Su informacion se a guardado correctamente.")
                self.destroy()
                Login()
                
        else: 
            messagebox.showerror("Error","Complete todos los campos para poder continuar")


if __name__ == "__main__":
    Register()