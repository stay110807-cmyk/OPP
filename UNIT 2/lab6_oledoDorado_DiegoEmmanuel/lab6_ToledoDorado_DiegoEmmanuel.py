import tkinter as tk
from tkinter import ttk
import os 
from abc import ABC, abstractmethod #

class smartDevice(ABC):
    def __init__(self, name: str):
        self.name = name


    @abstractmethod
    def turn_on(self)-> str:
        pass 

class smartTV(smartDevice):
    def __init__(self, name):
        super().__init__("Tv de Diego")

    def turn_on(self) -> str:
        return f"{self.name}, is paying the lore of Elden Ring"

class smartPhone(smartDevice):
    def __init__(self, name):
        super().__init__("Telefono de diego")

    def turn_on(self) ->str:
        return f"{self.name}, is texting to mom"

class smartWatch(smartDevice):
    def __init__(self, name: str):
        super().__init__("Reloj de Diego")

    def turn_on(self) -> str:
        return f"{self.name}, is showing the hour"







class SmartHomeApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # --- 1. WINDOW SETTINGS---
        self.title("Lab 6: Polymorphism GUI - by Toledo Dorado Diego Emmanuel")
        self.geometry("480x360")
        self.resizable(False, False)

        current_dir = os.path.dirname(os.fspath(__file__))
        icon_dir = os.path.join(current_dir, "app_icon.png")

        if os.path.exists(icon_dir):
            self.app_icon = tk.PhotoImage(file=icon_dir)
            self.iconphoto(True, self.app_icon)
        else: 
            print("The icon file doesn't exist") 

        # --- 2. OBJECT REGISTRY---
        # Map a friendly Radiobutton label to an instantiated object:
        self.items = {
            "smartTV": smartTV(self),
            "smartPhone": smartPhone(self),
            "smartWatch": smartWatch(self),
        }

        # Build visual components
        self._build_interface()

    def _build_interface(self):
        # Header / Title Banner
        lbl_header = tk.Label(
            self,
            text="Smart Home Center",
            font=("Arial", 15, "bold"),
            fg="#2c3e50"
        )
        lbl_header.pack(pady=12)

        # Selection Group (Radiobuttons)
        group_box = tk.LabelFrame(
            self,
            text=" Select an Option ",
            font=("Arial", 20, "bold"),
            padx=15,
            pady=10
        )
        group_box.pack(fill="x", padx=20, pady=5)

        # Default selection: first key in dictionary
        first_key = list(self.items.keys())[0]
        self.selected_key = tk.StringVar(value=first_key)

        # Automatically generates a radiobutton for each item in self.items
        for key in self.items.keys():
            rb = ttk.Radiobutton(
                group_box,
                text=key,
                value=key,
                variable=self.selected_key
            )
            rb.pack(anchor="w", pady=3)

        # Trigger Action Button
        btn_action = tk.Button(
            self,
            text="Turn on Device",
            command=self._handle_action,
            bg="#2980b9",
            fg="white",
            font=("Arial", 10, "bold"),
            relief="raised",
            cursor="hand2",
            padx=12,
            pady=6
        )
        btn_action.pack(pady=15)

        # Output / Results Box
        self.lbl_output = tk.Label(
            self,
            text="Select an option above and click 'EXECUTE ACTION'.",
            font=("Arial", 10, "italic"),
            bg="#ecf0f1",
            fg="#34495e",
            relief="groove",
            height=3,
            wraplength=420,
            justify="center"
        )
        self.lbl_output.pack(fill="x", padx=20, pady=5)

    def _handle_action(self):
        # 1. Get the current key selected by the user
        chosen_key = self.selected_key.get()

        # 2. Retrieve the active polymorphic object
        active_object: smartDevice = self.items[chosen_key]

        # 3. POLYMORPHIC EXECUTION:
        # No 'if/elif' logic needed. Python runs the appropriate implementation!
        result_message = active_object.turn_on()

        # 4. Display result in the UI
        self.lbl_output.config(text=result_message, font=("Arial", 10, "normal"))



# LAUNCHER
if __name__ == "__main__":
    app = SmartHomeApp()
    app.mainloop()