import random
import string
import tkinter as tk

# FINISHED

class Tool:
    def __init__(self, parent):
        self.frame = tk.Frame(parent)
        self.frame.pack(fill="both", expand=True)

        # Title Label
        tk.Label(
            self.frame,
            text="Password Generator",
            font=("Arial", 14, "bold")
        ).pack(pady=10)

        self.grid_frame = tk.Frame(self.frame)
        self.grid_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # CHANGED: Added vertical spacers and forced a single master column
        self.grid_frame.columnconfigure(0, weight=1)
        self.grid_frame.rowconfigure(0, weight=1) 
        self.grid_frame.rowconfigure(4, weight=1) 

        # CHANGED: Inner sub-frame to keep options locked in the center
        options_container = tk.Frame(self.grid_frame)
        options_container.grid(row=1, column=0, pady=5)

        # Password Length (Now inside options_container with sticky controls)
        tk.Label(options_container, text="Password Length:").grid(row=0, column=0, sticky="e", padx=10, pady=2)
        self.length_entry = tk.Entry(options_container, width=10)
        self.length_entry.insert(0, "12")
        self.length_entry.grid(row=0, column=1, sticky="w", padx=10, pady=2)

        # Include Numerals Checkbox
        tk.Label(options_container, text="Include Numerals:").grid(row=1, column=0, sticky="e", padx=10, pady=2)
        self.num_var = tk.IntVar(value=1)
        self.include_numerals = tk.Checkbutton(options_container, variable=self.num_var)
        self.include_numerals.grid(row=1, column=1, sticky="w", padx=10, pady=2)

        # Include Uppercase Checkbox
        tk.Label(options_container, text="Include Uppercase:").grid(row=2, column=0, sticky="e", padx=10, pady=2)
        self.upper_var = tk.IntVar(value=1)
        self.include_uppercase = tk.Checkbutton(options_container, variable=self.upper_var)
        self.include_uppercase.grid(row=2, column=1, sticky="w", padx=10, pady=2)

        # Include Symbols Checkbox
        tk.Label(options_container, text="Include Symbols:").grid(row=3, column=0, sticky="e", padx=10, pady=2)
        self.sym_var = tk.IntVar(value=1)
        self.include_symbols = tk.Checkbutton(options_container, variable=self.sym_var)
        self.include_symbols.grid(row=3, column=1, sticky="w", padx=10, pady=2)

        # Result Display Box (Shifted row indices to match master frame layout)
        self.result_label = tk.Label(self.grid_frame, text="-", font=("Arial", 10), wraplength=350)
        self.result_label.grid(row=2, column=0, pady=5)
        
        # Action Trigger Button
        self.generate_button = tk.Button(
            self.grid_frame,
            text="Generate Password",
            command=self.generate_password
        )
        self.generate_button.grid(row=3, column=0, pady=10)

        
    # FIXED: Indented correctly so it sits inside the Tool class namespace
    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length < 5 or length > 128:
                self.result_label.config(text="Error: Length must be between 5 and 128", fg="red")
                return
        except ValueError:
            self.result_label.config(text="Error: Invalid length", fg="red")
            return

        chars = string.ascii_lowercase
        
        # Pull integer states safely from our variable tracking instances
        use_numerals = self.num_var.get()
        use_uppercase = self.upper_var.get()
        use_symbols = self.sym_var.get()

        if use_numerals:
            chars += string.digits
        if use_uppercase:
            chars += string.ascii_uppercase
        if use_symbols:
            chars += string.punctuation

        # NEW: Safety check to ensure the character pool is not completely empty
        if not chars:
            self.result_label.config(text="Error: Select at least one option", fg="red")
            return

        password = ''.join(random.choice(chars) for _ in range(length))
        self.result_label.config(text=password, fg="black")


# This bridge function matches the run_tool call expected by app.py
def run_tool(parent_frame):
    Tool(parent_frame)
