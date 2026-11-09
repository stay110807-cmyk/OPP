import tkinter as tk
from Views import LoginVentana

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginVentana(root)
    root.mainloop()


"The library fpdf we can use it to create an archive that export our database in the JSON, TXT, PDF, CSV format"