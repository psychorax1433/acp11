import tkinter as tk
from tkinter import messagebox

def check_strength():
    password = password_var.get()
    length = len(password)
    
    if length == 0:
        messagebox.showwarning("Input Required", "Please enter a password.")
    elif length < 6:
        strength_var.set("Strength: Weak 😟")
    elif 6 <= length <= 9:
        strength_var.set("Strength: Medium 🙂")
    else:
        strength_var.set("Strength: Strong 💪")

# ── GUI setup ──
root = tk.Tk()
root.title("Password Strength Checker")

password_var = tk.StringVar()
strength_var = tk.StringVar()

# Labels and Entry
tk.Label(root, text="Enter Password:").grid(row=0, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=password_var, show='*', width=25).grid(row=0, column=1, padx=10, pady=10)

tk.Button(root, text="Check Strength", command=check_strength).grid(row=1, column=0, columnspan=2, pady=10)

tk.Label(root, textvariable=strength_var, font=("Arial", 12, "bold")).grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
