import tkinter as tk
from tkinter import ttk, messagebox
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def on_generate_button_click():
    try:
        length = int(entry_length.get())
        if length < 1:
            raise ValueError("Length must be positive.")
        password = generate_password(length)
        entry_password.delete(0, tk.END)
        entry_password.insert(0, password)
    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x200")

style = ttk.Style()
style.configure("TLabel", font=("Arial", 12))
style.configure("TEntry", font=("Arial", 12))
style.configure("TButton", font=("Arial", 12))

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E))

ttk.Label(frame, text="Desired Length of Password:").grid(row=0, column=0, pady=5, sticky=tk.W)
entry_length = ttk.Entry(frame, width=20)
entry_length.grid(row=0, column=1, pady=5, sticky=tk.W)

ttk.Button(frame, text="Generate Password", command=on_generate_button_click).grid(row=1, column=0, columnspan=2, pady=10)

ttk.Label(frame, text="Generated Password:").grid(row=2, column=0, pady=5, sticky=tk.W)
entry_password = ttk.Entry(frame, width=40)
entry_password.grid(row=2, column=1, pady=5, sticky=tk.W)

root.mainloop()
