from tkinter import *

root = Tk()
root.title("To-Do List")
root.geometry("400x500")

task_entry = Entry(
    root,
    font=("Arial", 15),
    width=25,
    bg="pink",
    fg="black"
)

task_entry.pack(pady=10)


task_list = Listbox(
    root,
    width=30,
    height=10,
    font=("Arial", 14),
    bg="pink"
)

task_list.pack(pady=10)

def add_task():
    task = task_entry.get()

    if task != "":
        task_list.insert(END, task)
        task_entry.delete(0, END)
root.bind("<Return>", lambda event: add_task())

add_btn = Button(
    root,
    text="Add Task",
    command=add_task,
    bg="deeppink",
    fg="black",
    font=("Arial", 12, "bold")
)

add_btn.pack(pady=10)

def delete_task():
    selected = task_list.curselection()

    if selected:
        task_list.delete(selected[0])

delete_btn = Button(
    root,
    text="Delete Task",
    command=delete_task
)

delete_btn.pack(pady=10)




root.mainloop()
