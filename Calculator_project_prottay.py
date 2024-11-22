import tkinter as tk
from tkinter import ttk
import math

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def insert(char):
    entry.insert(tk.END, char)

def clear():
    entry.delete(0, tk.END)

def backspace():
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text[:-1])

def sqrt():
    try:
        value = float(entry.get())
        result = math.sqrt(value)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

root = tk.Tk()
root.title("Basic Calculator")
root.geometry("350x450")
root.resizable(False, False)
root.configure(bg="#D3E3FC")  # Light blue background

entry = tk.Entry(root, font=("Arial", 20), justify='right', bg="#EAEAEA", fg="#333333", bd=5)
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8, padx=10, pady=10, sticky="nsew")

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0), ('⌫', 5, 1), ('%', 5, 2), ('√', 5, 3)
]

for (text, row, col) in buttons:
    if text == '=':
        ttk.Button(root, text=text, command=calculate).grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
    elif text == 'C':
        ttk.Button(root, text=text, command=clear).grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
    elif text == '⌫':
        ttk.Button(root, text=text, command=backspace).grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
    elif text == '√':
        ttk.Button(root, text=text, command=sqrt).grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
    else:
        ttk.Button(root, text=text, command=lambda t=text: insert(t)).grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

for i in range(6):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i % 4, weight=1)

root.mainloop()
