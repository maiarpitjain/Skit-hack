def menu():
    from tkinter import Tk,Menu,mainloop
    import maps
    import predict_images

    import threading
    global thread1
    global thread2
    global thread3
    thread1=threading.Thread(target=predict_images.run_attendance)
    thread2=threading.Thread(target=customer_form)
    thread3=threading.Thread(target=employee_form)

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
    employeemenu.add_command(label='New employee',command=thread3.run)
    employeemenu.add_command(label='Update employee')
    employeemenu.add_command(label='Delete employee')

    customermenu = Menu(menu) 
    menu.add_cascade(label='Customer', menu=customermenu) 
    customermenu.add_command(label='New Customer',command=thread2.start)
    customermenu.add_command(label='Activated customers')
    customermenu.add_command(label='completed problems')



    mainloop() 


def customer_form():
    import tkinter as tk
    from tkinter import ttk

    def on_button():
        myValue = []
        #myValue.append(name.get())
        myValue.append(address.get())
        myValue.append(email.get())
        myValue.append(number.get())
        myValue.append(p_type.get())
        myValue.append(d_name.get())
        myValue.append(p_description.get())
        myValue.append(c_name.get())
        x=name.get()
        print(x)
        print(myValue)

    root = tk.Tk()
    w = tk.Frame(root)
    w.grid(row=0, columnspan=3)

    first_label = tk.Label(w, text="Customer: ")
    first_label.grid(row=0, column=1, padx=10, sticky=tk.W)

    first_label = tk.Label(w, text="name: ")
    first_label.grid(row=1, column=0, padx=10, sticky=tk.W)


    name = tk.StringVar()
    name_entry = ttk.Entry(w, textvariable=name)
    name_entry.grid(row=1, column=1, sticky=tk.W, padx=10)

    first_label = tk.Label(w, text="Address: ")
    first_label.grid(row=2, column=0, padx=10, sticky=tk.W)


    address = tk.StringVar()
    address_entry = ttk.Entry(w, textvariable=address)
    address_entry.grid(row=2, column=1, sticky=tk.W, padx=10)

    first_label = tk.Label(w, text="email: ")
    first_label.grid(row=3, column=0, padx=10, sticky=tk.W)


    email = tk.StringVar()
    email_entry = ttk.Entry(w, textvariable=email)
    email_entry.grid(row=3, column=1, sticky=tk.W, padx=10)

    first_label = tk.Label(w, text="Number: ")
    first_label.grid(row=4, column=0, padx=10, sticky=tk.W)


    number = tk.StringVar()
    number_entry = ttk.Entry(w, textvariable=number)
    number_entry.grid(row=4, column=1, sticky=tk.W, padx=10)

    first_label = tk.Label(w, text="p_type: ")
    first_label.grid(row=5, column=0, padx=10, sticky=tk.W)


    p_type = tk.StringVar()
    p_type_entry = ttk.Entry(w, textvariable=p_type)
    p_type_entry.grid(row=5, column=1, sticky=tk.W, padx=10)

    first_label = tk.Label(w, text="Device: ")
    first_label.grid(row=6, column=0, padx=10, sticky=tk.W)


    d_name = tk.StringVar()
    d_name_entry = ttk.Entry(w, textvariable=d_name)
    d_name_entry.grid(row=6, column=1, sticky=tk.W, padx=10)

    first_label = tk.Label(w, text="problem: ")
    first_label.grid(row=7, column=0, padx=10, sticky=tk.W)


    p_description = tk.StringVar()
    p_description_entry = ttk.Entry(w, textvariable=p_description)
    p_description_entry.grid(row=7, column=1, sticky=tk.W, padx=10)

    first_label = tk.Label(w, text="company: ")
    first_label.grid(row=8, column=0, padx=10, sticky=tk.W)


    c_name = tk.StringVar()
    c_name_entry = ttk.Entry(w, textvariable=c_name)
    c_name_entry.grid(row=8, column=1, sticky=tk.W, padx=10)


    button1 = tk.Button(w, text="Create", command=on_button)
    button1.grid(row=9, columnspan=1, sticky=tk.W)

    button2 = tk.Button(w, text="exit", command=exit)
    button2.grid(row=9, column=2,columnspan=3, sticky=tk.W)

    root.mainloop()


def employee_form():
    import tkinter as tk
    from tkinter import ttk

    def on_button():
        myValue = []
        #myValue.append(name.get())
        myValue.append(address.get())
        myValue.append(email.get())
        myValue.append(number.get())
        myValue.append(c_name.get())
        x=name.get()
        print(x)
        print(myValue)

    def on_exit():
        exit()
    root = tk.Tk()
    w = tk.Frame(root)
    w.grid(row=0, columnspan=3)

    first_label = tk.Label(w, text="Employee: ")
    first_label.grid(row=0, column=1, padx=10, sticky=tk.W)

    first_label = tk.Label(w, text="name: ")
    first_label.grid(row=1, column=0, padx=10, sticky=tk.W)


    name = tk.StringVar()
    name_entry = ttk.Entry(w, textvariable=name)
    name_entry.grid(row=1, column=1, sticky=tk.W, padx=10)

    first_label = tk.Label(w, text="Address: ")
    first_label.grid(row=2, column=0, padx=10, sticky=tk.W)


    address = tk.StringVar()
    address_entry = ttk.Entry(w, textvariable=address)
    address_entry.grid(row=2, column=1, sticky=tk.W, padx=10)

    first_label = tk.Label(w, text="email: ")
    first_label.grid(row=3, column=0, padx=10, sticky=tk.W)


    email = tk.StringVar()
    email_entry = ttk.Entry(w, textvariable=email)
    email_entry.grid(row=3, column=1, sticky=tk.W, padx=10)

    first_label = tk.Label(w, text="Number: ")
    first_label.grid(row=4, column=0, padx=10, sticky=tk.W)


    number = tk.StringVar()
    number_entry = ttk.Entry(w, textvariable=number)
    number_entry.grid(row=4, column=1, sticky=tk.W, padx=10)

   
    first_label = tk.Label(w, text="company: ")
    first_label.grid(row=8, column=0, padx=10, sticky=tk.W)


    c_name = tk.StringVar()
    c_name_entry = ttk.Entry(w, textvariable=c_name)
    c_name_entry.grid(row=8, column=1, sticky=tk.W, padx=10)


    button1 = tk.Button(w, text="Create", command=on_button)
    button1.grid(row=9, columnspan=1, sticky=tk.W)

    button2 = tk.Button(w, text="exit", command=on_exit)
    button2.grid(row=9, column=2,columnspan=3, sticky=tk.W)

    root.mainloop()




menu()