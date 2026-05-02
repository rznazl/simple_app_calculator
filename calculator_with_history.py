import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple App Calculator")
        self.root.geometry("300x400")

        self.label = tk.Label(root, text="Select Operation:", font=("Arial", 10, "bold"))
        self.label.pack(pady=10)

        self.operation = tk.StringVar(value="Addition")
        operations = ["Addition", "Subtraction", "Multiplication", "Division"]
        self.dropdown = tk.OptionMenu(root, self.operation, *operations)
        self.dropdown.pack(pady=5)