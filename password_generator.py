import tkinter as tk
from tkinter import messagebox
import random

def generate():
    try:
        password_length = int(length_entry.get())
    except ValueError:
        messagebox.showerror("ERROR", "Please enter a valid number")
        return

    if password_length < 8:
        messagebox.showwarning('WARNING', 'LENGTH SHOULD BE GREATER THAN 8!')
    elif password_length > 20:
        messagebox.showwarning('WARNING', 'LENGTH CANNOT EXCEED 20 CHARACTERS!')
    else:
        lowercase = 'abcdefghijklmnopqrstuvwxyz'
        uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        numbers = '0123456789'
        symbols = '@#$%^&*(){}[]|?/<>,.;:' + '"' + '`~-_+'
        all_characters = lowercase + uppercase + numbers + symbols
        generated_password = ''.join(random.choice(all_characters) for _ in range(password_length))
        result_label.config(text=generated_password)

root = tk.Tk()
root.title('PASSWORD GENERATOR')
root.geometry('220x150')
root.resizable(False, False)

# Entry Widget
length_entry = tk.Entry(root, width=25,  fg='darkgreen', font=('Arial', 12))
length_entry.insert(0, 'Enter Password Length...')
length_entry.bind("<FocusIn>", lambda event: length_entry.delete("0", "end"))
length_entry.grid(row=1, pady=10)

# Label Widget
result_label = tk.Label(root, width=20, height=1, text="GENERATED PASSWORD", font=('Arial', 10))
result_label.grid(row=3, pady=10)

# Button Widget
generate_button = tk.Button(root, text="Generate Password", command=generate, bg='green', fg='white', font=('Arial', 12))
generate_button.grid(row=4, pady=10)

root.mainloop()
