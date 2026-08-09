import tkinter as tk
import random

class Tool:
    def __init__(self, parent):
        self.frame = tk.Frame(parent)
        self.frame.pack(fill="both", expand=True)

        # Title Label
        tk.Label(
            self.frame,
            text="Random Number Generator",
            font=("Arial", 14, "bold")
        ).pack(pady=10)

        self.grid_frame = tk.Frame(self.frame)
        self.grid_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.grid_frame.columnconfigure(0, weight=1)
        self.grid_frame.columnconfigure(1, weight=1)

        tk.Label(self.grid_frame, text="Min:").grid(row=1, column=0, sticky="e", padx=5)
        self.min_entry = tk.Entry(self.grid_frame, width=10)
        self.min_entry.insert(0, "1")
        self.min_entry.grid(row=1, column=1, sticky="w", padx=5)

        tk.Label(self.grid_frame, text="Max:").grid(row=2, column=0, sticky="e", padx=5)
        self.max_entry = tk.Entry(self.grid_frame, width=10)
        self.max_entry.insert(0, "100")
        self.max_entry.grid(row=2, column=1, sticky="w", padx=5)

        self.result_label = tk.Label(self.grid_frame, text="-", font=("Arial", 18))
        self.result_label.grid(row=3, column=0, columnspan=2, pady=10)

        # Action button
        tk.Button(
            self.grid_frame,
            text="Generate",
            command=self.generate_number
        ).grid(row=4, column=0, columnspan=2, pady=5)

    def generate_number(self):
        try:
            min = int(self.min_entry.get())
            max = int(self.max_entry.get())
            if min > max:
                self.result_label.config(text="Error: Min > Max", fg="red")
            else:
                number = random.randint(min, max)
                self.result_label.config(text=str(number))
        except ValueError:
            self.result_label.config(text="Error: Invalid input", fg="red")

        
# This bridge function matches the run_tool call expected by app.py
def run_tool(parent_frame):
    Tool(parent_frame)
