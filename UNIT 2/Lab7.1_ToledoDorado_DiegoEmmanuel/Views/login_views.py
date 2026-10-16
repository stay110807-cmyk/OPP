import tkinter as tk
from tkinter import messagebox
from Models.login_model import User
import os
from Views.home_view import HomeView

class login_screen:
    def __init__(self, root):
        self.root = root
        self.root.title("System Lab 7")
        self.root.geometry("300x300")
        self.reasizable(False, False)

    def create_interface(self):
        lbl_titulo = tk.Label(self.root, text="Incio de sesión", font=("Helvetica", 20) )
        lbl_username = tk.Label(self.root, text="Incio de sesión", font=("Helvetica", 20) )
        self.entry_usario = tk.Entry(self.root, font=("Helvica", 10))     
        lbl_passw = tk.Label(self.root, text="Ingrese su contraseña", font=("Arial", 15) )  

class LoginVentana:
    """Ventana de inicio de sesión."""

    def __init__(self, root):
        self.root = root
        self.root.title("Acceso al Sistema")
        self.root.geometry("350x380")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e2f")

        self._poner_icono()


        # Construir la interfaz
        self._crear_interfaz()

    def _poner_icono(self):
        ruta = os.path.join(os.path.dirname(__file__), "icono.png")
        try:
            imagen = tk.PhotoImage(file=ruta)
            self.root.iconphoto(True, imagen)
            self.icono = imagen
        except tk.TclError as e:
            print("No se encontró el ícono", e)
            print("Ruta buscada", ruta)

    def _crear_interfaz(self):
        # Título
        lbl_titulo = tk.Label(self.root, text="Iniciar Sesión", font=("Helvetica", 16, "bold"))
        lbl_titulo.pack(pady=25)

        # Campo Usuario
        lbl_usuario = tk.Label(self.root, text="Usuario:", font=("Helvetica", 10))
        lbl_usuario.pack(anchor="w", padx=30, pady=(5, 2))
        
        self.entry_usuario = tk.Entry(self.root, font=("Helvetica", 11))
        self.entry_usuario.pack(fill="x", padx=30)

        # Campo Contraseña
        lbl_pass = tk.Label(self.root, text="Contraseña:", font=("Helvetica", 10))
        lbl_pass.pack(anchor="w", padx=30, pady=(15, 2))
        
        self.entry_pass = tk.Entry(self.root, font=("Helvetica", 11), show="*")
        self.entry_pass.pack(fill="x", padx=30)

        # Botón Ingresar
        btn_ingresar = tk.Button(
            self.root, 
            text="Entrar", 
            font=("Helvetica", 11, "bold"),
            bg="#2196F3", 
            fg="white", 
            cursor="hand2",
            command=self._validar_login
        )
        btn_ingresar.pack(fill="x", padx=30, pady=30)

    def _validar_login(self):
        usuario_texto = self.entry_usuario.get().strip()
        pass_texto = self.entry_pass.get().strip()

        # Validación básica de campos vacíos
        if not usuario_texto or not pass_texto:
            messagebox.showwarning("Campos Vacíos", "Por favor ingresa usuario y contraseña.")
            return

        # Instanciar el modelo Usuario y autenticar
        usuario_obj = User (usuario_texto, pass_texto)
        datos_usuario = usuario_obj.auth()

        if datos_usuario:
            nombre = datos_usuario[0]['name_user']
            messagebox.showinfo("Bienvenido", f"¡Hola {nombre}! Acceso concedido.")
            self._abrir_dashboard(nombre)
        else:
            messagebox.showerror("Error de Acceso", "Usuario o contraseña incorrectos.")

    def _abrir_dashboard(self, nombre_completo):
        self.root.destroy()
        root_home = tk.Tk()
        HomeView(root_home, nombre_completo)
        root_home.mainloop()

class DashboardVentana:


    def __init__(self, root, nombre_usuario):
        self.root = root
        self.root.title("Panel Principal")
        self.root.geometry("400x250")

        lbl_mensaje = tk.Label(
            self.root, 
            text=f"¡Bienvenido/a al Sistema!\n\nUsuario activo:\n{nombre_usuario}", 
            font=("Helvetica", 12),
            justify="center"
        )
        lbl_mensaje.pack(expand=True)                     