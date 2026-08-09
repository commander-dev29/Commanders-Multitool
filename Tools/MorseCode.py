import tkinter as tk
from tkinter import ttk

class Tool:
    def __init__(self, parent):
        self.frame = tk.Frame(parent)
        self.frame.pack(fill="both", expand=True)

        self.grid_frame = tk.Frame(self.frame)
        self.grid_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # CHANGED: Added vertical spacers and forced a single master column layout
        self.grid_frame.columnconfigure(0, weight=1)
        self.grid_frame.rowconfigure(0, weight=1) # Top invisible vertical spring
        self.grid_frame.rowconfigure(3, weight=1) # Bottom invisible vertical spring

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
        
        dropdown = ttk.Combobox(
            options_container,
            values=["Encode", "Decode"],
            state="readonly"
        )
        dropdown.set("Encode")
        dropdown.grid(row=0, column=1, sticky="w", padx=10, pady=5)


        
# This bridge function matches the run_tool call expected by app.py
def run_tool(parent_frame):
    Tool(parent_frame)
