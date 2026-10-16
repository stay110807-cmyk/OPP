import tkinter as tk
import os 
from tkinter import ttk
from Models.login_model import Product

class HomeView:
    def __init__(self, root, nombre_usuario):
        self.root = root
        self.root.title("Panel Principal")
        self.root.geometry("700x400")

        self._poner_icono()

        lbl_bienvenida = tk.Label(self.root, text=f"Bienvenido/a, {nombre_usuario}",
                                  font=("Helvetica", 14, "bold"))
        lbl_bienvenida.pack(pady=15)

        columnas = ("id", "nombre", "descripcion", "precio", "stock")
        self.tabla = ttk.Treeview(self.root, columns=columnas, show="headings")

        titulos = ["ID", "Producto", "Descripción", "Precio", "Stock"]
        for columna, titulo in zip(columnas, titulos):
            self.tabla.heading(columna, text=titulo)
            self.tabla.column(columna, anchor="center", width=120)

        self.tabla.pack(fill="both", expand=True, padx=20, pady=(0, 20))

        self._cargar_productos()



    def _cargar_productos(self):
        productos = Product().get_all()
        if productos:
            for p in productos:
                self.tabla.insert("", "end", values=(
                    p["id_product"],
                    p["name_product"],
                    p["description"],
                    f"${p['price']}",
                    p["stock"]
                ))