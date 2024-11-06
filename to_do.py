import tkinter as tk
from tkinter import messagebox, font

# Create main window
root = tk.Tk()
root.title("To-Do List App")
root.geometry("500x500")
root.config(bg="#2d2d2d")  


custom_font = font.Font(family="Helvetica", size=12)


top_frame = tk.Frame(root, bg="#3a3a3a", pady=10)
top_frame.pack(fill="x")


task_entry = tk.Entry(top_frame, width=40, font=custom_font, relief="flat", bg="#444", fg="#e0e0e0", insertbackground="white")
task_entry.grid(row=0, column=0, padx=10, pady=5)


def add_task():
    task = task_entry.get().strip()
    if task:
        task_listbox.insert(tk.END, f"• {task}")
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")


def delete_task():
    selected_tasks = task_listbox.curselection()
    if selected_tasks:
        task_listbox.delete(selected_tasks[0])
    else:
        messagebox.showwarning("Warning", "Please select a task to delete!")


def mark_done():
    selected_task = task_listbox.curselection()
    if selected_task:
        task = task_listbox.get(selected_task[0])
        task_listbox.delete(selected_task[0])
        task_listbox.insert(tk.END, f"{task} ✔")
    else:
        messagebox.showwarning("Warning", "Please select a task to mark as done!")


def on_enter(e):
    e.widget.config(bg="#45a049")

def on_leave(e):
    e.widget.config(bg="#5cb85c")

add_button = tk.Button(top_frame, text="Add Task", command=add_task, bg="#5cb85c", fg="white", font=custom_font, relief="flat", cursor="hand2", borderwidth=2)
add_button.grid(row=0, column=1, padx=5)
add_button.bind("<Enter>", on_enter)
add_button.bind("<Leave>", on_leave)


middle_frame = tk.Frame(root, bg="#2d2d2d", pady=10)
middle_frame.pack(fill="both", expand=True)


task_listbox = tk.Listbox(middle_frame, width=45, height=15, font=custom_font, bg="#333", fg="#e0e0e0", selectbackground="#5cb85c", selectforeground="white", borderwidth=0, highlightthickness=0)
task_listbox.pack(pady=10)


bottom_frame = tk.Frame(root, bg="#2d2d2d")
bottom_frame.pack(fill="x")


def delete_hover_enter(e):
    e.widget.config(bg="#c9302c")

def delete_hover_leave(e):
    e.widget.config(bg="#d9534f")

def done_hover_enter(e):
    e.widget.config(bg="#31b0d5")

def done_hover_leave(e):
    e.widget.config(bg="#5bc0de")

delete_button = tk.Button(bottom_frame, text="Delete Task", command=delete_task, bg="#d9534f", fg="white", font=custom_font, relief="flat", cursor="hand2", borderwidth=2)
delete_button.pack(side="left", padx=10, pady=5)
delete_button.bind("<Enter>", delete_hover_enter)
delete_button.bind("<Leave>", delete_hover_leave)

done_button = tk.Button(bottom_frame, text="Mark as Done", command=mark_done, bg="#5bc0de", fg="white", font=custom_font, relief="flat", cursor="hand2", borderwidth=2)
done_button.pack(side="right", padx=10, pady=5)
done_button.bind("<Enter>", done_hover_enter)
done_button.bind("<Leave>", done_hover_leave)


root.mainloop()
