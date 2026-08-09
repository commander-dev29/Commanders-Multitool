import os
import importlib
import tkinter as tk
import numpy as np

class MultiTool:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("MultiTool")
        self.root.geometry("600x300")
        self.root.resizable(False, False)
        self.current_tool_frame = None  # Tracks and clears active tool UIs

    def create_widgets(self): # Create the main layout of the application
        sidebar = tk.Frame(self.root, relief=tk.GROOVE, borderwidth="3", width="200", bg="lightgray") # Select tools
        sidebar.pack(side="left", fill="y", padx=(10, 5), pady=10)
        sidebar.pack_propagate(False)

        scrollbar = tk.Scrollbar(sidebar, orient="vertical")
        scrollbar.pack(side="right", fill="y")

        # Pack canvas SECOND so it fills whatever space remains in the sidebar.
        canvas = tk.Canvas(sidebar, highlightthickness=0, bg="lightgray")
        canvas.pack(side="left", fill="both", expand=True)
        
        def _on_mousewheel(event):
            canvas.yview_scroll(-int(event.delta / 120), "units")

        sidebar.bind("<Enter>", lambda e: canvas.bind_all("<MouseWheel>", _on_mousewheel))
        sidebar.bind("<Leave>", lambda e: canvas.unbind_all("<MouseWheel>"))

        scrollbar.config(command=canvas.yview)
        canvas.config(yscrollcommand=scrollbar.set)

        button_frame = tk.Frame(canvas)

        window = canvas.create_window((0,0), window=button_frame, anchor="nw")

        # Match tool frame width to the sidebar canvas
        canvas.bind(
            "<Configure>",
            lambda e: canvas.itemconfig(window, width=e.width)
        )

        # Updates the canvas dimensions so the scroll region stays accurate
        button_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        # CHANGED: Moved below the bindings so widgets trigger configuration updates automatically
        self.load_tools(button_frame)

        self.page = tk.Frame(self.root, relief=tk.RIDGE, borderwidth="3") # Place to show tools 
        self.page.pack(side="left", fill="both", expand=True, padx=(5, 10), pady=10)

    def load_tools(self, sidebar):
        for filename in os.listdir("Tools"):
            if filename.endswith(".py") and not filename.startswith("__"):
                tk.Button(
                    sidebar, 
                    text=filename[:-3],
                    command=lambda name=filename[:-3]: self.switch_tool(name)
                ).pack(fill="x")

    def switch_tool(self, tool_name):
        if self.current_tool_frame:
            self.current_tool_frame.destroy()

        self.current_tool_frame = tk.Frame(self.page)
        self.current_tool_frame.pack(fill="both", expand=True)

        try:
            # Dynamically import module from Tools directory
            module = importlib.import_module(f"Tools.{tool_name}")
            importlib.reload(module) # Reloads changes if files edit during runtime
            
            # Look for a standard layout function inside the tool file
            if hasattr(module, "run_tool"):
                module.run_tool(self.current_tool_frame)
            else:
                tk.Label(self.current_tool_frame, text=f"Error: run_tool() not found in {tool_name}").pack(pady=20)
        except Exception as e:
            tk.Label(self.current_tool_frame, text=f"Failed to load tool:\n{str(e)}", fg="red").pack(pady=20)
            
    def run(self):
        self.root.mainloop()

    

if __name__ == "__main__": # Runs the application
    app = MultiTool()
    app.create_widgets()
    app.run()