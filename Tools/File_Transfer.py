import tkinter as tk
from tkinter import filedialog, ttk, messagebox
from pathlib import Path


class Tool:
    def __init__(self, parent):
        self.frame = tk.Frame(parent)
        self.frame.pack(fill="both", expand=True)

        # Title
        tk.Label(
            self.frame,
            text="File Transfer",
            font=("Arial", 14, "bold")
        ).pack(pady=(10, 0))

        # =========================
        # Paths
        # =========================

        self.path_frame = ttk.LabelFrame(
            self.frame,
            text="Directories"
        )
        self.path_frame.pack(
            fill="x",
            padx=10,
            pady=5
        )

        self.path_frame.columnconfigure(1, weight=1)

        # Source
        ttk.Label(
            self.path_frame,
            text="Source:"
        ).grid(
            row=0,
            column=0,
            padx=8,
            pady=8
        )

        self.src_entry = ttk.Entry(self.path_frame)
        self.src_entry.grid(
            row=0,
            column=1,
            sticky="ew",
            padx=5,
            pady=8
        )

        ttk.Button(
            self.path_frame,
            text="Browse",
            command=self.select_src
        ).grid(
            row=0,
            column=2,
            padx=8,
            pady=8
        )

        # Destination
        ttk.Label(
            self.path_frame,
            text="Destination:"
        ).grid(
            row=1,
            column=0,
            padx=8,
            pady=8
        )

        self.dest_entry = ttk.Entry(self.path_frame)
        self.dest_entry.grid(
            row=1,
            column=1,
            sticky="ew",
            padx=5,
            pady=8
        )

        ttk.Button(
            self.path_frame,
            text="Browse",
            command=self.select_dest
        ).grid(
            row=1,
            column=2,
            padx=8,
            pady=8
        )

        # =========================
        # Options
        # =========================

        self.options_frame = ttk.LabelFrame(
            self.frame,
            text="Options"
        )
        self.options_frame.pack(
            fill="x",
            padx=10,
            pady=5
        )

        self.options_frame.columnconfigure(1, weight=1)
        self.options_frame.columnconfigure(3, weight=1)

        # Operation
        ttk.Label(
            self.options_frame,
            text="Operation:"
        ).grid(
            row=0,
            column=0,
            padx=8,
            pady=8
        )

        self.op_box = ttk.Combobox(
            self.options_frame,
            values=["Move", "Copy"],
            state="readonly"
        )
        self.op_box.grid(
            row=0,
            column=1,
            sticky="ew",
            padx=5,
            pady=8
        )
        self.op_box.current(1)

        # Duplicates
        ttk.Label(
            self.options_frame,
            text="Duplicates:"
        ).grid(
            row=0,
            column=2,
            padx=8,
            pady=8
        )

        self.duplicate_box = ttk.Combobox(
            self.options_frame,
            values=["Skip", "Overwrite"],
            state="readonly"
        )
        self.duplicate_box.grid(
            row=0,
            column=3,
            sticky="ew",
            padx=5,
            pady=8
        )
        self.duplicate_box.current(0)

        # =========================
        # Checkboxes
        # =========================

        self.copy_folder = tk.BooleanVar(value=False)

        self.folder_box = ttk.Checkbutton(
            self.options_frame,
            text="Transfer Folder Itself",
            variable=self.copy_folder
        )
        self.folder_box.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky="w",
            padx=8,
            pady=(3, 4)
        )

        self.inc_sub_folder = tk.BooleanVar(value=False)

        self.inc_sub_box = ttk.Checkbutton(
            self.options_frame,
            text="Include Subfolders",
            variable=self.inc_sub_folder
        )
        self.inc_sub_box.grid(
            row=1,
            column=2,
            columnspan=2,
            sticky="w",
            padx=8,
            pady=(3, 4)
        )

        # =========================
        # Transfer Button
        # =========================

        self.transfer_button = ttk.Button(
            self.options_frame,
            text="Transfer Files",
            command=self.transfer_files
        )
        self.transfer_button.grid(
            row=2,
            column=0,
            columnspan=4,
            sticky="ew",
            padx=50,
            pady=8
        )

    def select_src(self):
        directory = filedialog.askdirectory()

        if directory:
            self.src_entry.delete(0, tk.END)
            self.src_entry.insert(0, directory)

    def select_dest(self):
        directory = filedialog.askdirectory()

        if directory:
            self.dest_entry.delete(0, tk.END)
            self.dest_entry.insert(0, directory)

    def transfer_files(self):
        if self.src_entry.get().strip() and self.dest_entry.get().strip():
            # Get parameters
            source = Path(self.src_entry.get())
            destination = Path(self.dest_entry.get())

            operation = self.op_box.get()
            dup_handle = self.duplicate_box.get()
            folder = self.copy_folder.get()
            inc_sub = self.inc_sub_folder.get()

            print("Source:", source)
            print("Destination:", destination)
            print("Operation:", operation)
            print("Duplicate handling:", dup_handle)
            print("Transfer folder:", folder)
            print("Include subfolders:", inc_sub)
            if (
                source.exists()
                and source.is_dir()
                and destination.exists()
                and destination.is_dir()
            ):
                # Both are valid directories
                print("Both directories are valid")
            else:
                messagebox.showerror(
                    "Invalid Directories",
                    "Path(s) to either the source or destination "
                    "directory are invalid."
                )
                return
        else:
            messagebox.showerror(
                "Required Input Missing",
                "Please provide both source and destination paths."
            )
            return


def run_tool(parent_frame):
    Tool(parent_frame)