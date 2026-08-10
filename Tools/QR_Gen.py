import tkinter as tk
from tkinter import ttk, messagebox
import qrcode

class Tool:
    def __init__(self, parent):
        self.frame = tk.Frame(parent)
        self.frame.pack(fill="both", expand=True)

        tk.Label(
            self.frame,
            text="QR Code Generator",
            font=("Arial", 14, "bold")
        ).pack(pady=10)
        self.input_entry = tk.Entry(self.frame, width=40)
        self.input_entry.pack(pady=5)
        
        self.scale = tk.Spinbox(
            self.frame,
            from_=1,
            to=20,
            width=5,
            font=("Arial", 12)
        )
        self.scale.pack(pady=5)

        self.generate_button = tk.Button(
            self.frame,
            text="Generate QR Code",
            command=self.generate_qr
        )
        self.generate_button.pack(pady=5)

    def generate_qr(self):
        data = self.input_entry.get()
        if data:
            try:
                size = round(float(self.scale.get()))
                qr = qrcode.QRCode(
                    version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=size,
                    border=4,
                )
                qr.add_data(data)
                qr.make(fit=True)

                img = qr.make_image(fill_color="black", back_color="white")
                img.show()
            except Exception as e:
                tk.messagebox.showerror("Generation Error", f"Failed to generate QR code:\n{str(e)}")
        else:
            tk.messagebox.showwarning("Input Error", "Please enter some data to generate a QR code.")


# This bridge function matches the run_tool call expected by app.py
def run_tool(parent_frame):
    Tool(parent_frame)
