import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    selected_task_index = tasks_listbox.curselection()
    if selected_task_index:
        tasks_listbox.delete(selected_task_index)
    else:
        messagebox.showwarning("Warning", "Please select a task to remove.")

def clear_tasks():
    tasks_listbox.delete(0, tk.END)

# GUI setup
app = tk.Tk()
app.title("To-Do List")

# Task Entry and Buttons
task_entry = tk.Entry(app, width=40)
task_entry.grid(row=0, column=0, padx=30, pady=30, columnspan=5)

add_button = tk.Button(app, text="Add Task", command=add_task)
add_button.grid(row=0, column=2, padx=10, pady=30)

remove_button = tk.Button(app, text="Remove Task", command=remove_task)
remove_button.grid(row=1, column=0, padx=10, pady=10)

clear_button = tk.Button(app, text="Clear All", command=clear_tasks)
clear_button.grid(row=1, column=1, padx=10, pady=10)

# Task Listbox
tasks_listbox = tk.Listbox(app, selectmode=tk.SINGLE, height=10, width=50)
tasks_listbox.grid(row=2, column=0, padx=10, pady=10, columnspan=3)

app.mainloop()
