import tkinter as tk
from tkinter import messagebox
root=tk.Tk()
def password_checker():
    user_pass=entry_box.get()
    if(user_pass=="secert321"):
        messagebox.showinfo("Result","Access Granted")
label_01=tk.Label(root,text="Enter Password:")
entry_box=tk.Entry(root)
button=tk.Button(root,text="Submit",command=password_checker)
label_01.pack()
entry_box.pack()
button.pack()
root.mainloop()
