import tkinter as tk

def on_button_click(event):
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create an entry widget
entry = tk.Entry(root, font=('arial', 20, 'bold'), bd=8, insertwidth=4, width=15, justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Button labels
button_labels = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

# Create buttons
for (label, row, col) in button_labels:
    button = tk.Button(root, text=label, padx=20, pady=20, font=('arial', 20, 'bold'))
    button.grid(row=row, column=col)
    button.bind("<Button-1>", on_button_click)

# Start the main event loop
root.mainloop()
