import tkinter as tk

def on_button_click(value):
    current = entry_var.get()
    entry_var.set(current + str(value))

def clear_entry():
    entry_var.set("")

def calculate_result():
    try:
        result = eval(entry_var.get())
        entry_var.set(result)
    except Exception as e:
        entry_var.set("Error")

window = tk.Tk()
window.title("Simple Calculator")

entry_var = tk.StringVar()
entry = tk.Entry(window, textvariable=entry_var, font=('Arial', 14), bd=10, insertwidth=4, width=14, justify='right')
entry.grid(row=0, column=0, columnspan=4, sticky='nsew')

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0
for button in buttons:
    tk.Button(window, text=button, padx=20, pady=20, font=('Arial', 14),
              command=lambda btn=button: on_button_click(btn) if btn != '=' else calculate_result()).grid(row=row_val, column=col_val, sticky='nsew')
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

tk.Button(window, text='C', padx=20, pady=20, font=('Arial', 14), command=clear_entry).grid(row=row_val, column=col_val, columnspan=2, sticky='nsew')

for i in range(5):
    window.grid_rowconfigure(i, weight=1)
    window.grid_columnconfigure(i, weight=1)

def on_key_press(event):
    key = event.char
    if key in "0123456789./*-+":
        on_button_click(key)
    elif key == "\r":
        calculate_result()
    elif key == "\x08":
        clear_entry()

window.bind("<Key>", on_key_press)

window.mainloop()
