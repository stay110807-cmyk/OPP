import tkinter as tk
from Views.login_views import LoginVentana 

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginVentana(root)
    root.mainloop()
