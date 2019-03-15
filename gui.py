def menu():
    from tkinter import *
    import maps
    import predict_images

    import threading

    thread1=threading.Thread(target=predict_images.run_attendance)

    root = Tk() 
    root.geometry("500x500")
    menu = Menu(root) 
    root.config(menu=menu) 
    filemenu = Menu(menu) 
    menu.add_cascade(label='Attendence', menu=filemenu) 
    filemenu.add_command(label='Start',command=thread1.start) 
    filemenu.add_command(label='End') 
    filemenu.add_separator() 
    filemenu.add_command(label='Exit', command=root.quit) 
    employeemenu = Menu(menu) 
    menu.add_cascade(label='Employee', menu=employeemenu) 
    employeemenu.add_command(label='New employee')
    employeemenu.add_command(label='Update employee')
    employeemenu.add_command(label='Delete employee')

    customermenu = Menu(menu) 
    menu.add_cascade(label='Customer', menu=customermenu) 
    customermenu.add_command(label='New Customer')
    customermenu.add_command(label='Activated customers')
    customermenu.add_command(label='completed problems')



    mainloop() 


def employee_form():
    import tkinter as tk
    from tkinter import ttk

    def on_button():
        myValue = myEntry.get()
        print(myValue)

    root = tk.Tk()

    w = tk.Frame(root)
    w.grid(row=0, columnspan=3)

    first_label = tk.Label(w, text="myEntry: ")
    first_label.grid(row=0, column=0, padx=10, sticky=tk.W)

    myEntry = tk.StringVar()
    myEntry_entry = ttk.Entry(w, textvariable=myEntry)
    myEntry_entry.grid(row=0, column=1, sticky=tk.W, padx=10)

    button1 = tk.Button(w, text="Print in Console", command=on_button)
    button1.grid(row=4, columnspan=1, sticky=tk.W)

    root.mainloop()

employee_form()