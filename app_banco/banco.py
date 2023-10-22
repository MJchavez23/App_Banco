import tkinter as tk
import csv
from tkinter import messagebox

def iniciar_saldo(func):
    def wrapper(self):
        with open("C:\\Users\\Admin\\Documents\\PYTHON\\app_banco\\registro.csv", "r") as archivo:
            archivo_csv = csv.reader(archivo, delimiter=",")
            for line in archivo_csv:
                try:
                    if self.usuario == line[2] and self.contrasena == line[3]:
                        self.saldo_valor = int(line[4])
                except:
                    pass
        return func(self)
    return wrapper

def actualizar_saldo(func):
    def wrapper(self):
        if func.__name__ == "depositar":
            saldo_nuevo = self.saldo_valor + int(self.entry_deposito.get())
            self.saldo_valor = saldo_nuevo
            self.saldo.config(text = saldo_nuevo)
        else:
            saldo_nuevo = self.saldo_valor - int(self.entry_retiro.get())
            self.saldo_valor = saldo_nuevo
            self.saldo.config(text = saldo_nuevo)

        return func(self)
    return wrapper


class Banco(tk.Tk):
    def __init__(self, usuario, contrasena):
        super().__init__()
        self.usuario = usuario
        self.contrasena = contrasena
        self.geometry("300x180")
        self.title("Banco")
        self.resizable(0,0)
        self.saldo_valor = 0
        self.componentes()
        self.mainloop()

    @iniciar_saldo
    def componentes(self):
        tk.Label(self, text="Banco", font=("Arial",16)).place(relx=.5, rely=.13,anchor="center")
        tk.Label(self, text="Saldo: ", font=("Arial",16)).place(relx=.2, rely=.3,anchor="center")
        self.saldo = tk.Label(self, text=self.saldo_valor,font=("Arial",16))
        self.saldo.place(relx=.5, rely=.3, anchor="center")
        self.entry_deposito = tk.Entry(self)
        self.entry_deposito.place(relx=.5, rely=.55, anchor="center")
        self.entry_retiro = tk.Entry(self)
        self.entry_retiro.place(relx=.5, rely=.75, anchor="center")
        tk.Button(self, text="Depositar", command=self.depositar).place(relx=.85, rely=.55, anchor="center")
        tk.Button(self, text="Retirar", command=self.retirar).place(relx=.85, rely=.75, anchor="center")
        tk.Button(self, text="Salir", command=self.salida).place(relx=.5, rely=.9, anchor="center")
    
    
    
    @actualizar_saldo
    def depositar(self):
        messagebox.showinfo("Deposito","Deposito Realizado")


    @actualizar_saldo
    def retirar(self):
        messagebox.showinfo("Retiro","Retiro Realizado")


    def salida(self):
        lista_nuevo = []
        with open("C:\\Users\\Admin\\Documents\\PYTHON\\app_banco\\registro.csv", "r", newline="") as archivo:
            lista_csv= list(csv.reader(archivo))
        #print(lista_csv)
        for line in lista_csv:
            if line[2] == self.usuario and line[3] == self.contrasena:
                line[4] = str(self.saldo_valor)
            lista_nuevo.append(line)
        #print(lista_nuevo)
        with open("C:\\Users\\Admin\\Documents\\PYTHON\\app_banco\\registro.csv", "w",newline="") as archivo:
            archivo_csv = csv.writer(archivo)
            for line in lista_nuevo:
                archivo_csv.writerow(line)


if __name__ == "__main__":
    Banco("admin","admin")