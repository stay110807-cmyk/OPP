import tkinter as tk
from model.usermodel import UserModel
from view.loginview import LoginView
from controller.authentication import Authentication

class System:
    def __init__(self):
        self.root = tk.Tk()
        self.modelo = UserModel()
        self.vista = LoginView(self.root)
        self.controlador = Authentication(self.modelo, self.vista)
        
    def start(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = System()
    app.start()