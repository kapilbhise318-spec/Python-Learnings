# # import tkinter as tk
# # from tkinter import messagebox

# # # Function to handle the button click event
# # def show_message():
# #     messagebox.showinfo("Message", "Hello, GUI!") #

# # # 1. Create the main application window
# # root = tk.Tk()
# # root.title("My GUI App") #
# # root.geometry("300x200") # Set the window size (width x height)

# # # 2. Add a widget (a button)
# # btn_hello = tk.Button(root, text="Click Me!", command=show_message) #

# # # 3. Position the widget using a geometry manager
# # btn_hello.pack(pady=50) # Add vertical padding

# # # 4. Start the main event loop
# # root.mainloop()
# # import tkinter as tk
# # from tkinter import messagebox

# # # Function to handle the button click event
# # def show_message():
# #     messagebox.showinfo("Message", "Hello, GUI!") #

# # # 1. Create the main application window
# # root = tk.Tk()
# # root.title("My GUI App") #
# # root.geometry("300x200") # Set the window size (width x height)

# # # 2. Add a widget (a button)
# # btn_hello = tk.Button(root, text="Click Me!", command=show_message) #

# # # 3. Position the widget using a geometry manager
# # btn_hello.pack(pady=50) # Add vertical padding

# # # 4. Start the main event loop
# # root.mainloop()



# import tkinter as tk
# root=tk.Tk()
# root.title("Tkinter project")
# # root.geometry("600 x 400")
# root.geometry("1800x2000")

# #Add labels
# # 
# label=tk.Label(root,text="WelcomeGUI", font=("Arial",25)) 
# label.pack()

# entry=tk.Entry(root)
# entry.pack()

# def greet():
#     name=entry.get()
#     # f" Hello greet function! {name}"
#     result=label.config(text=f" Hello greet function! {name}")

# button=tk.Button(root,text="Gonna be!",command=greet,font=("Arial",25))
# button.pack()

# result_label=tk.Label(root,text=" ")
# result_label.pack()

# root.mainloop()











# Mini project


import tkinter as tk

def click(event):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(event.widget["text"]))

def clear():
    entry.delete(0, tk.END)

def equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=20, font=("Arial", 20))
entry.grid(row=0, column=0, columnspan=4)

buttons = ["7","8","9","/",
           "4","5","6","*",
           "1","2","3","-",
           "0","C","=","+"]

row = 1
col = 0

for b in buttons:
    btn = tk.Button(root, text=b, width=5, height=2)
    btn.grid(row=row, column=col)

    if b == "=":
        btn.config(command=equal)
    elif b == "C":
        btn.config(command=clear)
    else:
        btn.bind("<Button-1>", click)

    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()