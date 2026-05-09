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
    print(name_var.get())
    return

def toggle_completed_task():
    try:
        listboxIndex = listbox.curselection()[0]
        itemText = listbox.get(listboxIndex)
        itemText = ("☑" if itemText[0] == "☐" else "☐") + itemText[1:]
        listbox.delete(listboxIndex)
        listbox.insert(listboxIndex, itemText)
        listbox.selection_set(listboxIndex)
    except:
        return

def delete_task():
    
    return

root = tk.Tk()
root.title("Tkinter Todos")
root.geometry("400x300")
root.configure(background="#333536")

root.columnconfigure(0, weight=1)
root.rowconfigure(2, weight=1)

name_var = tk.StringVar()

addFrame = tk.Frame(root, background="#333536")
addFrame.grid(row=1, column=0, sticky="ew")

title = tk.Label(root, text="Todos", font=("Arial", 24, "bold"), height=2, foreground="#f5f5f5", background="#333536")
title.grid(row=0, column=0)

addName = tk.Entry(addFrame, foreground="#f5f5f5", background="#484B4D", insertbackground="#f5f5f5", font=("Arial", 14, "bold"), textvariable=name_var)
addName.pack(side="left", fill="x", expand=True, padx=(10, 0))

addButton = tk.Button(addFrame, text="+", command=add_task, foreground="#f5f5f5", background="#333536", activeforeground="#f5f5f5", activebackground="#333536", bd=0, cursor="hand2", font=("Arial", 30, "bold"))
addButton.pack(side="right")

listFrame = tk.Frame(root, background="#333536",)
listFrame.grid(row=2, column=0, sticky="nsew")

scrollbar = tk.Scrollbar(listFrame, background="#333536")
scrollbar.pack(side="right", fill="y")

listbox = tk.Listbox(listFrame, yscrollcommand=scrollbar.set, foreground="#f5f5f5", background="#333536", bd=0, font=("Arial", 12, "bold"))
listbox.pack(side="left", fill="both", expand=True)

scrollbar.config(command=listbox.yview)

for i in range(50):
    listbox.insert(tk.END, f"☐ Item {i+1}") # ☐ ☑

actionsFrame = tk.Frame(root, background="#333536")
actionsFrame.grid(row=3, column=0)

completeButton = tk.Button(actionsFrame, text="Toggle", command=toggle_completed_task, foreground="#f5f5f5", background="#333536", activeforeground="#f5f5f5", activebackground="#333536", bd=0, cursor="hand2", font=("Arial", 16, "bold"))
completeButton.pack(side="left", padx=(0, 50))

deleteButton = tk.Button(actionsFrame, text="Delete", command=delete_task, foreground="#f5f5f5", background="#333536", activeforeground="#f5f5f5", activebackground="#333536", bd=0, cursor="hand2", font=("Arial", 16, "bold"))
deleteButton.pack(side="right", padx=(50, 0))

root.mainloop()