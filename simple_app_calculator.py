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

        tk.Label(root, text="Enter First Number: ").pack()
        self.entry1 = tk.Entry(root)
        self.entry1.pack(pady=5)

        tk.Label(root, text="Enter Second Number: ").pack()
        self.entry2 = tk.Entry(root)
        self.entry2.pack(pady=5)

        self.calculator_button = tk.Button(root, text="Calculate", command=self.perform_calculation, bg="#4CAF50", fg="white")
        self.calculator_button.pack(pady=20)

        self.result_label = tk.Label(root, text="Result: ", font=("Arial", 12))
        self.result_label.pack(pady=10)

    def perform_calculation(self):
        try:
            num1 = float(self.entry1.get())
            num2 = float(self.entry2.get())
            op = self.operation.get()

            if op == "Addition":
                res = num1 + num2
            elif op == "Subtraction":
                res = num1 - num2
            elif op == "Multiplication":
                res = num1 * num2
            elif op == "Division":
                if num2 == 0:
                    raise ZeroDivisionError("Cannot divide by zero")
                res = num1 / num2

            self.result_label.config(text=f"Result: {res}")
            
            if not messagebox.askyesno("Try Again", "Do you want to do another calculation?"):
                messagebox.showinfo("Exit", "Thank You!")
                self.root.quit()
            else:
                self.clear_fields()
                
        except ValueError:
            messagebox.showerror("Runtime Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {e}")
    def clear_fields(self):
        self.entry1.delete(0, tk.END)
        self.entry2.delete(0, tk.END)
        self.result_label.config(text="Result: ")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
