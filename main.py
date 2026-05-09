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

root = tk.Tk()
root.title("Tkinter Todos")
root.geometry("400x300")
root.configure(background="#333536")

title = tk.Label(root, text="Todos", font=("Arial", 24, "bold"), height=2, foreground="#f5f5f5", background="#333536")
title.pack()



root.mainloop()