import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to Generate Password
def generate_password():
    try:
        length = int(length_entry.get())

        if length <= 0:
            messagebox.showerror("Error", "Password length must be greater than 0!")
            return

        # Characters to use
        characters = string.ascii_letters + string.digits + string.punctuation

        # Generate Password
        password = "".join(random.choice(characters) for _ in range(length))

        # Output Window
        output_window = tk.Toplevel(root)
        output_window.title("Generated Password")
        output_window.geometry("500x300")
        output_window.configure(bg="#1E3A5F")

        # Title
        title = tk.Label(
            output_window,
            text="🔐 Password Generated Successfully",
            font=("Arial", 18, "bold"),
            bg="#1E3A5F",
            fg="white"
        )
        title.pack(pady=20)

        # Password Label
        password_label = tk.Label(
            output_window,
            text=password,
            font=("Consolas", 16, "bold"),
            bg="white",
            fg="#006400",
            width=30,
            relief="solid",
            padx=10,
            pady=10
        )
        password_label.pack(pady=20)

        # Close Button
        close_btn = tk.Button(
            output_window,
            text="Close",
            font=("Arial", 12, "bold"),
            bg="#F44336",
            fg="white",
            width=12,
            command=output_window.destroy
        )
        close_btn.pack(pady=15)

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid password length!")

# Main Window
root = tk.Tk()
root.title("Password Generator")
root.geometry("500x350")
root.configure(bg="#1E3A5F")

# Heading
heading = tk.Label(
    root,
    text="🔐 Password Generator",
    font=("Arial", 22, "bold"),
    bg="#1E3A5F",
    fg="white"
)
heading.pack(pady=20)

# Instruction
label = tk.Label(
    root,
    text="Enter Password Length",
    font=("Arial", 14),
    bg="#1E3A5F",
    fg="white"
)
label.pack()

# Entry
length_entry = tk.Entry(
    root,
    font=("Arial", 14),
    width=15,
    justify="center"
)
length_entry.pack(pady=10)

# Generate Button
generate_btn = tk.Button(
    root,
    text="Generate Password",
    font=("Arial", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    width=20,
    command=generate_password
)
generate_btn.pack(pady=20)

# Exit Button
exit_btn = tk.Button(
    root,
    text="Exit",
    font=("Arial", 12, "bold"),
    bg="#F44336",
    fg="white",
    width=12,
    command=root.destroy
)
exit_btn.pack()

# Run Application
root.mainloop()