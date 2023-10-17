import tkinter as tk
from tkinter import ttk

# Function to perform calculations
def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()
        
        if operation == "+":
            result.set(num1 + num2)
        elif operation == "-":
            result.set(num1 - num2)
        elif operation == "*":
            result.set(num1 * num2)
        elif operation == "/":
            if num2 == 0:
                result.set("Cannot divide by zero")
            else:
                result.set(num1 / num2)
    except ValueError:
        result.set("Invalid input")

# Create a tkinter window
window = tk.Tk()
window.title("Simple Calculator")
window.geometry("300x220")  # Set window size

# Create styles for widgets
style = ttk.Style()
style.configure("TButton", padding=5, font=("Helvetica", 12))
style.configure("TLabel", font=("Helvetica", 12))
style.configure("TEntry", font=("Helvetica", 12))

# Create entry fields for numbers
entry_num1 = ttk.Entry(window)
entry_num2 = ttk.Entry(window)

# Create a label for the result
result = tk.StringVar()
result.set("")
result_label = ttk.Label(window, textvariable=result)

# Create a dropdown for selecting the operation
operation_var = tk.StringVar()
operation_var.set("+")  # Default operation
operation_dropdown = ttk.Combobox(window, textvariable=operation_var, values=["+", "-", "*", "/"])
operation_dropdown['state'] = 'readonly'

# Create a "Calculate" button
calculate_button = ttk.Button(window, text="Calculate", command=calculate)

# Place widgets in the window
entry_num1.pack(pady=10)
operation_dropdown.pack(pady=10)
entry_num2.pack(pady=10)
calculate_button.pack(pady=10)
result_label.pack(pady=10)

# Start the main event loop
window.mainloop()
