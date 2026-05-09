import tkinter as tk
from tkinter import messagebox
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

def save():
    listBoxTasks = list(listbox.get(0, tk.END))
    tasks = []
    for listBoxTask in listBoxTasks:
        done = listBoxTask[0] == "☑"
        text = listBoxTask[2:]
        tasks.append({"done": done, "text": text})

    save_tasks(tasks)

def add_task():
    task_name = name_var.get()
    if task_name:
        addName.delete(0, tk.END)
        listbox.insert(tk.END, f"☐ {task_name}")
        listbox.focus()
        save()

def toggle_completed_task():
    try:
        if root.focus_get() == addName:
            return
        listboxIndex = listbox.curselection()[0]
        itemText = listbox.get(listboxIndex)
        itemText = ("☑" if itemText[0] == "☐" else "☐") + itemText[1:]
        listbox.delete(listboxIndex)
        listbox.insert(listboxIndex, itemText)
        listbox.selection_set(listboxIndex)
        save()
    except:
        return

def delete_task():
    try:
        if root.focus_get() == addName:
            return
        listboxIndex = listbox.curselection()[0]
        confirmDeletion = messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete the task: \"{listbox.get(listboxIndex)[2:]}\"?")
        if confirmDeletion:
            listbox.delete(listboxIndex)
            save()
    except:
        return
    
def clear_tasks():
    try:
        if root.focus_get() == addName:
            return
        confirmClear = messagebox.askyesno("Confirm Clear", f"Are you sure you want to clear all tasks?")
        if confirmClear:
            listbox.delete(0, tk.END)
            save()
    except:
        return
    
def initializeTasks():
    tasks = load_tasks()
    for task in tasks:
        listbox.insert(tk.END, ("☑ " if task["done"] else "☐ ") + task["text"])

root = tk.Tk()
root.title("Tkinter Todos")
root.geometry("400x300")
root.configure(background="#333536")

root.columnconfigure(0, weight=1)
root.rowconfigure(2, weight=1)

name_var = tk.StringVar()

root.bind("<Return>", lambda x: add_task())
root.bind("T", lambda x: toggle_completed_task())
root.bind("t", lambda x: toggle_completed_task())
root.bind("X", lambda x: delete_task())
root.bind("x", lambda x: delete_task())
root.bind("C", lambda x: clear_tasks())
root.bind("c", lambda x: clear_tasks())

root.bind("a", lambda x: addName.focus())
root.bind("A", lambda x: addName.focus())

root.bind("<Escape>", lambda x: root.destroy())

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

actionsFrame = tk.Frame(root, background="#333536")
actionsFrame.grid(row=3, column=0, sticky="ew")

actionsFrame.columnconfigure(0, weight=1)
actionsFrame.columnconfigure(1, weight=1)
actionsFrame.columnconfigure(2, weight=1)

completeButton = tk.Button(actionsFrame, text="[T] Toggle", command=toggle_completed_task, foreground="#f5f5f5", background="#333536", activeforeground="#f5f5f5", activebackground="#333536", bd=0, cursor="hand2", font=("Arial", 16, "bold"))
completeButton.grid(row=0, column=0)

deleteButton = tk.Button(actionsFrame, text="[X] Delete", command=delete_task, foreground="#f5f5f5", background="#333536", activeforeground="#f5f5f5", activebackground="#333536", bd=0, cursor="hand2", font=("Arial", 16, "bold"))
deleteButton.grid(row=0, column=1)

completeButton = tk.Button(actionsFrame, text="[C] Clear", command=clear_tasks, foreground="#f5f5f5", background="#333536", activeforeground="#f5f5f5", activebackground="#333536", bd=0, cursor="hand2", font=("Arial", 16, "bold"))
completeButton.grid(row=0, column=2)

initializeTasks()

root.mainloop()