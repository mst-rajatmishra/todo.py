from tkinter import *
from tkinter import messagebox
 
def addtask():
    task=entry.get()
    if task:
        listbox.insert(END,task)
        entry.delete(0,END)
    else:
        messagebox.showwarning("Warning","Please enter your task")
 
def removetask():
    selectedtaskindex=listbox.curselection()
    if selectedtaskindex:
        listbox.delete(selectedtaskindex)
        messagebox.showwarning('Warning',"Task deleted")
    else:
        messagebox.showwarning("Warning","Please select your task to remove")
 
def clearlist():
    listbox.delete(0,END)
    messagebox.showwarning('Warning',"List cleared")
 
root=Tk()
root.title("To-Do List")
root.geometry("600x600")
root.resizable(False,False)
root.configure(background="orange")

entry=Entry(root, width=25)

entry.pack(pady=10)
 
add_button=Button(root, text="Add Task", command=addtask)
add_button.pack(pady=10)
remove_button=Button(root, text="Delete Task", command=removetask)
remove_button.pack(pady=10)
 
clear_button=Button(root, text='Clear List', command=clearlist)
clear_button.pack(pady=10)
listbox=Listbox(root, width = 40, height= 50 )
listbox.pack(pady=10)
 
# entry.pack()
# add_button.pack()
 
# remove_button.pack()
# clear_button.pack()
# listbox.pack()
 
root.mainloop()
