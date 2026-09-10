# import tkinter as tk

# root=tk.Tk()
# root.title("My Tkinter App")

# label=tk.Button(root,text="Welcome to the Tkinter App")
# label.pack()

# button=tk.Button(root,text="Click Here")
# button.pack()

# root.mainloop()





# import tkinter as tk
# def say_hello():
#     print("Hello")

# root=tk.Tk()
# button=tk.Button(root,text="Click Here",command=say_hello)
# button.pack()
# root.mainloop()



# import tkinter as tk

# def take_input_from_user():
#     print(entry.get())


# root=tk.Tk()
# entry=tk.Entry(root)
# entry.pack()

# create_button=tk.Button(root,text="Submit",command=take_input_from_user)
# create_button.pack()

# root.mainloop()



# OBJECT-ORIENTED PROGRAMMING---  IMPORTANT FOR PROJECT USE

# import tkinter as tk
# from tkinter import messagebox
# from tkinter import dialog
# from  tkinter import ttk


# class App:
#     def __init__(self,root):
#         self.root=root
#         self.root.title("OOP GUI")
#         self.entry=tk.Entry(root)
#         self.entry.pack()

#         self.create_button=tk.Button(root,text="Click Here",command=self.show)
#         self.create_button.pack()
        

#     def show(self):
#         print(self.entry.get())

# root=tk.Tk()
# app=App(root)

# root.mainloop()



# import tkinter as tk
# from tkinter import ttk

# root=tk.Tk()
# root.title("My App")

# label=tk.Label(root,text="Show text")
# label.pack()

# create_button=ttk.Button(root,text="Style Bold")
# create_button.pack()

# root.mainloop()



import tkinter as tk

def click(event):

    current=entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current+str(event.widget["text"]))

def clear():
    entry.delete(0, tk.END)

def equal():

    try:
        result=eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)

    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

root=tk.Tk()

root.title("Calculator")
 
entry=tk.Entry(root, width=20, font=("Arial",20))
entry.grid(row=0, column=0, columnspan=4)

buttons=[
    "7","8","9","/",
    "4","5","6","*",
    "1","2","3","-",
    "0","C","=","+"
]

row=1
col=0

for b in buttons:
    btn=tk.Button(root, text=b, width=5, height=2)
    btn.grid(row=row, column=col)

    if b== "=":
        btn.config(command=equal)

    elif b== "C":
        btn.config(command=clear)
    
    else:
        btn.bind("<Button-1>", click)

    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()































































