import tkinter as tk
from tkinter import ttk
import os
from abc import ABC, abstractmethod
from datetime import datetime
 
 
# ======================================================================
# DEVICE CLASSES (the polymorphic part)
# ======================================================================
class SmartDevice(ABC):
    def __init__(self, name: str):
        self.name = name
 
    @abstractmethod
    def turn_on(self) -> str:
        pass
 
    # NEW: second polymorphic behaviour. Every subclass MUST implement it.
    @abstractmethod
    def turn_off(self) -> str:
        pass
 
 
class SmartTV(SmartDevice):
    def __init__(self):
        super().__init__("TV de Diego")
 
    def turn_on(self) -> str:
        return f"{self.name} is playing the lore of Elden Ring"
 
    def turn_off(self) -> str:
        return f"{self.name} stop to playing the lore of Elden Ring"
 
 
class SmartPhone(SmartDevice):
    def __init__(self):
        super().__init__("smartphone de Diego")
 
    def turn_on(self) -> str:
        return f"{self.name} is texting to mom"
 
    def turn_off(self) -> str:
        return f"{self.name} stop to texting to mom"
 
 
class SmartWatch(SmartDevice):
    def __init__(self):
        super().__init__("smartwatch de Diego")
 
    def turn_on(self) -> str:
        return f"{self.name} is showing the hour"
 
    def turn_off(self) -> str:
        return f"{self.name} stop to showing the hour"
 
 
# NEW: scalability test. Added with ZERO changes to the GUI logic;
# the only other edit is one line in the registry (self.items).
class SmartRodo(SmartDevice):
    def __init__(self):
        super().__init__("smartrodo de Diego")
 
    def turn_on(self) -> str:
        return f"{self.name} is thinking"
 
    def turn_off(self) -> str:
        return f"{self.name} stop to think"
 
 
# ======================================================================
# GUI
# ======================================================================
class SmartHomeApp(tk.Tk):
    def __init__(self):
        super().__init__()
 
        # --- 1. WINDOW SETTINGS ---
        self.title("Lab 6: Polymorphism GUI - by Rodolfo Rosado")
        self.geometry("480x560")
        self.resizable(False, False)
 
        current_dir = os.path.dirname(os.path.abspath(__file__))
        icon_dir = os.path.join(current_dir, "App_icon.png")
 
        if os.path.exists(icon_dir):
            self.app_icon = tk.PhotoImage(file=icon_dir)
            self.iconphoto(True, self.app_icon)
        else:
            print("The icon file doesn't exist")
 
        # --- 2. OBJECT REGISTRY ---
        # Map a friendly Radiobutton label to an instantiated object:
        self.items = {
            "TV": SmartTV(),
            "Phone": SmartPhone(),
            "Watch": SmartWatch(),
            "Rodo": SmartRodo(),  # new device, radiobutton appears automatically
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
            text=" Select a Device ",
            font=("Arial", 12, "bold"),
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
 
        # Buttons row (Turn On / Turn Off)
        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=12)
 
        btn_on = tk.Button(
            btn_frame,
            text="Turn On Device",
            command=self._handle_turn_on,
            bg="#27ae60",
            fg="white",
            font=("Arial", 10, "bold"),
            relief="raised",
            cursor="hand2",
            padx=12,
            pady=6
        )
        btn_on.pack(side="left", padx=8)
 
        btn_off = tk.Button(
            btn_frame,
            text="Turn Off Device",
            command=self._handle_turn_off,
            bg="#c0392b",
            fg="white",
            font=("Arial", 10, "bold"),
            relief="raised",
            cursor="hand2",
            padx=12,
            pady=6
        )
        btn_off.pack(side="left", padx=8)
 
        # Output / Results Box
        self.lbl_output = tk.Label(
            self,
            text="Select a device above and click 'Turn On' or 'Turn Off'.",
            font=("Arial", 10, "italic"),
            bg="#ecf0f1",
            fg="#34495e",
            relief="groove",
            height=3,
            wraplength=420,
            justify="center"
        )
        self.lbl_output.pack(fill="x", padx=20, pady=5)
 
        # Activity Log
        log_box = tk.LabelFrame(
            self,
            text=" Activity Log ",
            font=("Arial", 10, "bold"),
            padx=8,
            pady=6
        )
        log_box.pack(fill="both", expand=True, padx=20, pady=(8, 5))
 
        scrollbar = ttk.Scrollbar(log_box, orient="vertical")
        self.txt_log = tk.Text(
            log_box,
            height=8,
            wrap="word",
            font=("Consolas", 9),
            bg="#fdfefe",
            state="disabled",  # read-only; we unlock it only when writing
            yscrollcommand=scrollbar.set
        )
        scrollbar.config(command=self.txt_log.yview)
        scrollbar.pack(side="right", fill="y")
        self.txt_log.pack(side="left", fill="both", expand=True)
 
        btn_clear = tk.Button(
            self,
            text="Clear Log",
            command=self._clear_log,
            font=("Arial", 9),
            cursor="hand2"
        )
        btn_clear.pack(pady=(0, 10))
 
    # ------------------------------------------------------------------
    # Actions
    # ------------------------------------------------------------------
    def _get_active_device(self) -> SmartDevice:
        chosen_key = self.selected_key.get()
        return self.items[chosen_key]
 
    def _handle_turn_on(self):
        device = self._get_active_device()
        # POLYMORPHIC EXECUTION: no if/elif needed
        self._show_result(device.turn_on(), "ON ")
 
    def _handle_turn_off(self):
        device = self._get_active_device()
        # POLYMORPHIC EXECUTION: same idea, second behaviour
        self._show_result(device.turn_off(), "OFF")
 
    def _show_result(self, message: str, action_tag: str):
        # Display in the output label
        self.lbl_output.config(text=message, font=("Arial", 10, "normal"))
        # Record in the activity log
        self._log(f"[{action_tag}] {message}")
 
    # ------------------------------------------------------------------
    # Log helpers
    # ------------------------------------------------------------------
    def _log(self, message: str):
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.txt_log.config(state="normal")
        self.txt_log.insert("end", f"{timestamp}  {message}\n")
        self.txt_log.see("end")  # auto-scroll to the newest entry
        self.txt_log.config(state="disabled")
 
    def _clear_log(self):
        self.txt_log.config(state="normal")
        self.txt_log.delete("1.0", "end")
        self.txt_log.config(state="disabled")
 
 
# LAUNCHER
if __name__ == "__main__":
    app = SmartHomeApp()
    app.mainloop()