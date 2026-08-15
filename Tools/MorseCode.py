import tkinter as tk
from tkinter import ttk
import Tools.Libraries.Morse as morse

class Tool:
    def __init__(self, parent):
        self.frame = tk.Frame(parent)
        self.frame.pack(fill="both", expand=True)

        self.grid_frame = tk.Frame(self.frame)
        self.grid_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.grid_frame.columnconfigure(0, weight=1)
        self.grid_frame.rowconfigure(0, weight=1) 
        # self.grid_frame.rowconfigure(3, weight=1) 

        # Title Label (Centered globally on row 1 of the master frame)
        tk.Label(
            self.grid_frame,
            text="Morse Code Translator",
            font=("Arial", 14, "bold")
        ).grid(row=1, column=0, pady=10)

        # CHANGED: Tight nested sub-frame to keep options locked in the center
        options_container = tk.Frame(self.grid_frame)
        options_container.grid(row=2, column=0, pady=5)

        # Mode Selector (Now cleanly aligned inside options_container)
        mode_label = tk.Label(options_container, text="Select mode:")
        mode_label.grid(row=0, column=0, sticky="e", padx=10, pady=5)
        
        self.dropdown = ttk.Combobox(
            options_container,
            values=["Encode", "Decode"],
            state="readonly"
        )
        self.dropdown.set("Encode")
        self.dropdown.grid(row=0, column=1, sticky="w", padx=10, pady=5)

        translate_button = tk.Button(
            self.grid_frame,
            text="Translate",
            command=self.translate
        )
        translate_button.grid(row=3, column=0, pady=10)

    def translate(self):
        mode = self.dropdown.get()
        # Use 'if' and 'try' to select the mode and run safely

        
        
# This bridge function matches the run_tool call expected by app.py
def run_tool(parent_frame):
    Tool(parent_frame)
