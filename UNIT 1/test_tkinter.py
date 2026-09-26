import tkinter as tk
from tkinter import ttk
# root = Tk()
# frm = ttk.Frame(root, padding=10)
# frm.grid()
# ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
# root.mainloop()

root = tk.Tk()
root.title("My aplication")
root.geometry("640x400")
root.minsize(320, 240)

ttk.Label(root, text="Revivio el Cruz Azul").pack(padx=20, pady=20)

root.mainloop()

# root = tk.Tk()

# # Create the application variable and give it an initial value.
# contents = tk.StringVar(value="this is a variable")

# # Tell the entry widget to track the variable.
# entry = ttk.Entry(root, textvariable=contents)
# entry.pack()

# # Print the current value whenever the user presses Return.
# def print_contents(event):
#     print("The current entry content is:", contents.get())

# entry.bind("<Return>", print_contents)

# # Setting the variable from the program updates the entry through the
# # same link.
# def clear():
#     contents.set("")

# ttk.Button(root, text="Clear", command=clear).pack()

# root.mainloop()