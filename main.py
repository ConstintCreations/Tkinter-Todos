import tkinter as tk

root = tk.Tk()
root.title("Tkinter Todos")
root.geometry("400x300")
root.configure(background="#333536")

title = tk.Label(root, text="Todos", font=("Arial", 24, "bold"), height=2, foreground="#f5f5f5", background="#333536")
title.pack()



root.mainloop()