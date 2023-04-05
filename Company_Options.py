from tkinter import *
import tkinter as tk
root= tk.Tk()
menu=Menu(root)
def company():
    options=tk.StringVar(root)
    options.set("Company")

    company_Options =OptionMenu(root,options,"Samsung","Apple", "Oppo", "Redmi")
    company_Options.grid(row=2,column=2)

    b1 = Button(root,  text='Search', command=lambda: selected_Company() )
    b1.grid(row=2,column=3)

    str_out=tk.StringVar(root)

    l2 = tk.Label(root,  textvariable=str_out, width=10 )
    l2.grid(row=2,column=4)

    def selected_Company():
        outputvalue=(options.get())
        print(outputvalue)
root.mainloop()