import tkinter as tk
import json, os

TASKS_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open (TASKS_FILE, "r") as file:
        return json.load(file)
    
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task():
    return

root = tk.Tk()
root.title("Tkinter Todos")
root.geometry("400x300")
root.configure(background="#333536")

root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

titlebar = tk.Frame(root, background="#333536")
titlebar.grid(row=0, column=0)

title = tk.Label(titlebar, text="Todos", font=("Arial", 24, "bold"), height=2, foreground="#f5f5f5", background="#333536")
title.pack(side="left")

button = tk.Button(titlebar, text="+", command=add_task, foreground="#f5f5f5", background="#333536", activeforeground="#f5f5f5", activebackground="#333536", bd=0, cursor="hand2", font=("Arial", 24, "bold"))
button.pack(side="right")

listFrame = tk.Frame(root, background="#333536",)
listFrame.grid(row=1, column=0, sticky="nsew")

scrollbar = tk.Scrollbar(listFrame, background="#333536")
scrollbar.pack(side="right", fill="y")

listbox = tk.Listbox(listFrame, yscrollcommand=scrollbar.set, foreground="#f5f5f5", background="#333536", bd=0)
listbox.pack(side="left", fill="both", expand=True)

scrollbar.config(command=listbox.yview)

for i in range(50):
    listbox.insert(tk.END, f"Item {i+1}")

root.mainloop()