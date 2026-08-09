import tkinter as tk
from tkinter import ttk

class Tool:
    def __init__(self, parent):
        self.frame = tk.Frame(parent)
        self.frame.pack(fill="both", expand=True)

        tk.Label(
            self.frame,
            text="Random Number Generator",
            font=("Arial", 14, "bold")
        ).pack(pady=10)

        
# This bridge function matches the run_tool call expected by app.py
def run_tool(parent_frame):
    Tool(parent_frame)
