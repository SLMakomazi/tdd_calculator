import tkinter as tk
from tkinter import ttk, messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.resizable(False, False)  # Lock window size
        
        # Calculator state
        self.expression = ""
        self.last_was_operator = False
        self.history = []
        
        # Style
        style = ttk.Style()
        style.configure("Calculator.TButton", padding=10, font=('Arial', 12))
        style.configure("Display.TLabel", 
                       background="white", 
                       font=('Arial', 20),
                       padding=10,
                       anchor="e")
        
        # Main Frame
        main_frame = ttk.Frame(root, padding="10")
        main_frame.grid(row=0, column=0, sticky="nsew")
        
        # Display
        self.display = ttk.Label(main_frame, text="0", style="Display.TLabel", width=20)
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)
        
        # Button layout
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]
        
        # Create buttons
        for (text, row, col) in buttons:
            self.create_button(main_frame, text, row, col)
            
        # Clear button
        self.create_button(main_frame, 'C', 0, 4, command=self.clear)
        
        # Bind keyboard events
        self.root.bind('<Return>', lambda e: self.calculate())
        self.root.bind('<Escape>', lambda e: self.clear())
        for key in '0123456789.+-*/':
            self.root.bind(key, lambda e, key=key: self.append(key))

    def create_button(self, parent, text, row, col, command=None):
        if command is None:
            command = lambda: self.append(text) if text != '=' else self.calculate()
        btn = ttk.Button(parent, text=text, style="Calculator.TButton", command=command)
        btn.grid(row=row, column=col, padx=2, pady=2, sticky="nsew")
        return btn

    def append(self, text):
        if text in '+-*/' and self.last_was_operator:
            return
        if text in '+-*/' and not self.expression:
            return
        self.expression += text
        self.last_was_operator = text in '+-*/'
        self.display.configure(text=self.expression)

    def clear(self, *args):
        self.expression = ""
        self.last_was_operator = False
        self.display.configure(text="0")

    def calculate(self, *args):
        if not self.expression:
            return
        try:
            result = str(eval(self.expression))
            self.display.configure(text=result)
            self.expression = result
            self.last_was_operator = False
        except Exception as e:
            messagebox.showerror("Error", "Invalid expression")
            self.clear()

def main():
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
