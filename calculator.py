import tkinter as tk
from tkinter import messagebox

# Initialize the main window
root = tk.Tk()
root.title("🧮 Smart Calculator")
root.geometry("420x680")
root.configure(bg="#1e1e1e")
root.resizable(False, False)

# Global variable to store the expression
expression = ""

# --- Functions ---
def press(num):
    """Append pressed button to the expression."""
    global expression
    expression += str(num)
    equation.set(expression)

def clear():
    """Clear the input field."""
    global expression
    expression = ""
    equation.set("")

def backspace():
    """Delete the last character."""
    global expression
    expression = expression[:-1]
    equation.set(expression)

def equal():
    """Evaluate the final expression."""
    global expression
    try:
        result = str(eval(expression))
        equation.set(result)
        expression = result
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero")
        expression = ""
        equation.set("")
    except:
        messagebox.showerror("Error", "Invalid input")
        expression = ""
        equation.set("")

# --- UI Setup ---
equation = tk.StringVar()

# Entry field
entry_field = tk.Entry(root, textvariable=equation, font=('Arial', 24), bg="#2d2d2d", fg="white", bd=0, justify='right')
entry_field.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=25, padx=10, pady=10)

# Button styling
button_style = {
    "font": ('Arial', 18),
    "bd": 0,
    "fg": "white",
    "width": 4,
    "height": 2,
    "relief": "flat",
    "activebackground": "#4CAF50"
}

# Button layout
buttons = [
    ('C', 1, 0, '#ff5757', clear),
    ('⌫', 1, 1, '#ffb347', backspace),
    ('%', 1, 2, '#ffb347', lambda: press('%')),
    ('/', 1, 3, '#6a5acd', lambda: press('/')),

    ('7', 2, 0, '#333', lambda: press(7)),
    ('8', 2, 1, '#333', lambda: press(8)),
    ('9', 2, 2, '#333', lambda: press(9)),
    ('*', 2, 3, '#6a5acd', lambda: press('*')),

    ('4', 3, 0, '#333', lambda: press(4)),
    ('5', 3, 1, '#333', lambda: press(5)),
    ('6', 3, 2, '#333', lambda: press(6)),
    ('-', 3, 3, '#6a5acd', lambda: press('-')),

    ('1', 4, 0, '#333', lambda: press(1)),
    ('2', 4, 1, '#333', lambda: press(2)),
    ('3', 4, 2, '#333', lambda: press(3)),
    ('+', 4, 3, '#6a5acd', lambda: press('+')),

    ('0', 5, 0, '#333', lambda: press(0)),
    ('.', 5, 1, '#333', lambda: press('.')),
    ('=', 5, 2, '#4CAF50', equal),
]

# Add buttons to the window
for (text, row, col, color, command) in buttons:
    tk.Button(root, text=text, bg=color, command=command, **button_style).grid(row=row, column=col, padx=8, pady=8)

# Adjust the "=" button to span two columns
equal_button = tk.Button(root, text='=', bg='#4CAF50', command=equal, **button_style)
equal_button.grid(row=5, column=2, columnspan=2, padx=8, pady=8, sticky="nsew")

root.mainloop()