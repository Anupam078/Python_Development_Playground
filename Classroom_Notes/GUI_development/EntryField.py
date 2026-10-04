import tkinter as tk
from tkinter import messagebox  # We have to import this separately!

# 1. Create the callback function
def greet_user():
    # Get the text from the entry widget
    typed_name = name_entry.get() 
    # Show a pop-up dialog
    messagebox.showinfo("Greeting", f"Hello, {typed_name}!")

def check_password():
    password=password_entry.get()
    if password == "secret123":
        messagebox.showinfo("Result" , "Access Granted")

root = tk.Tk()
root.title("Greeting App")
password_entry=tk.Entry(root)
password_entry.pack()
# 2. Create and pack an Entry widget
name_entry = tk.Entry(root)
name_entry.pack()



# 3. Create and pack a Button, linking it to our function
# Notice: command=greet_user (NO parentheses!)
greet_button = tk.Button(root, text="Say Hello", command=greet_user)
greet_button.pack()

root.mainloop()

