from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
from tkinter import font as tkFont
import get_conn as g
import tkinter as tk
from tkinter import messagebox as mb

class main():
    def __init__(self,root):
        self.root=root
        self.window = Toplevel()
        self.window.attributes('-fullscreen', True)
        self.window.geometry("800x800")
        self.window.title("IPHONE 11")
        self.window.columnconfigure(0, weight=1)
        self.window.columnconfigure(1, weight=1)
        self.window.rowconfigure(0, weight=5)
        self.window.rowconfigure(1, weight=2)
        self.root_1 = Frame(self.window, bg="#27241D")
        self.root_1.grid(row=0, column=0, sticky="nsew")
        self.frame_bottom = Frame(self.window, bg="#27241D")
        self.frame_bottom.grid(row=1, column=0, sticky="nsew")
        self.frame_right = Frame(self.window, bg="#27241D")
        self.frame_right.grid(row=0, column=1, sticky="nsew", rowspan=2)
        self.Arial_font = tkFont.Font(family='Arial', size=14, weight='bold')
        self.lst = [('Brand', 'Apple'),
               ('Model', 'Iphone 11'),
               ('Dimensions (mm)', '150.9 x 75.7 x 8.3'),
               ('Weight (g)', '194.00'),
               ('Battery capacity (mAh)', '3110'),
               ('Fast charging', 'Fast charging 18W'),
               ('Colours ', 'Green, Yellow, Red'),
               ('Screen size (inches)', '6.1'),
               ('Resolution', '828 x 1792 pixels'),
               ('Processor', 'hexa-core'),
               ('Processor make', 'Apple A13 Bionic'),
               ('RAM', '4GB'),
               ('Internal storage', '128GB'),
               ('Expandable storage', 'No'),
               ('Expandable storage type', '-'),
               ('Rear camera', '12+12 megapixels'),
               ('No. of Rear Cameras', '2'),
               ('Rear autofocus', 'Yes'),
               ('Rear flash', 'Yes'),
               ('Front camera', '12-megapixel'),
               ('No. of Front Cameras', '1'),
               ('Pop-Up Camera', 'No')]
        # find total number of rows and
        # columns in list

        self.total_rows = len(self.lst)
        self.total_columns = len(self.lst[0])
        self.Model = "Iphone 11"
        self.Colour = ["Green", "Red", "Yellow"]
        self.Price = [40999, 41999, 42999]
        self.Arial_font = tkFont.Font(family='Arial', size=14, weight='bold')
        self.options = StringVar(self.window)
        self.options.set(self.Colour[0])
        self.colour_Options = OptionMenu(self.frame_bottom, self.options, *self.Colour, command=self.on_option_change)
        self.colour_Options.config(font=self.Arial_font, bg="#A39E93", fg="#FAF9F7")
        self.menu = self.root_1.nametowidget(self.colour_Options.menuname)
        self.menu.config(font=self.Arial_font, bg="#A39E93", fg="#FAF9F7")
        self.colour_Options.place(relx=0.65, rely=0.2)
        self.colour_lbl = Label(self.frame_bottom, text=f"₹. {self.Price[0]}", font=('Arial', 20, 'bold'), bg="#A39E93", fg="#FAF9F7")
        self.colour_lbl.place(relx=0.65, rely=0.5)
        self.img_1 = ImageTk.PhotoImage(Image.open("Iphone11_1.png").resize((300, 500)))  # width,height
        self.img_2 = ImageTk.PhotoImage(Image.open("Iphone11_2.png").resize((300, 500)))
        self.img_3 = ImageTk.PhotoImage(Image.open("Iphone11_3.png").resize((300, 500)))
        self.img_4 = ImageTk.PhotoImage(Image.open("Iphone11_4.png").resize((300, 500)))
        self.img_5 = ImageTk.PhotoImage(Image.open("Iphone11_5.png").resize((300, 500)))

        self.image_list = [self.img_1, self.img_2, self.img_3, self.img_4, self.img_5]

        self.staus = Label(self.root_1, text=f"Image 1 of {len(self.image_list)}", bd=1, relief=SUNKEN, anchor=E,
                      font=('Arial', 14, 'bold'), bg="#A39E93", fg="#FAF9F7")

        self.my_label = Label(self.root_1, image=self.img_1)
        self.my_label.place(relx=0.25, rely=0.008)

        self.button_back = Button(self.root_1, text="<<", command=self.back, state=DISABLED, font=('Arial', 14, 'bold'), bg="#A39E93",
                             fg="#FAF9F7")
        self.button_forward = Button(self.root_1, text=">>", command=lambda: self.forward(2), font=('Arial', 14, 'bold'), bg="#A39E93",
                                fg="#FAF9F7")
        self.button_back.place(relx=0.25, rely=0.94, relwidth=0.04, relheight=0.05)
        self.button_forward.place(relx=0.655, rely=0.94, relwidth=0.04, relheight=0.05)

        self.staus.place(relx=0.29, rely=0.94, relwidth=0.365, relheight=0.05)

        self.img_cart = ImageTk.PhotoImage(Image.open("add_cart.png").resize((100, 100)))
        self.button_cart = Button(self.frame_bottom, text="Add to Cart!", command=lambda: self.add_Cart(), image=self.img_cart,
                             font=('Arial', 14, 'bold'), bg="#A39E93", fg="#FAF9F7")
        self.button_cart.place(relx=0.45, rely=0.2)

        self.img_menu = ImageTk.PhotoImage(Image.open("main_menu.png").resize((100, 100)))
        self.button_cart = Button(self.frame_bottom, text="Add to Cart!", command=self.window.destroy, image=self.img_menu,
                             font=('Arial', 14, 'bold'), bg="#A39E93", fg="#FAF9F7")
        self.button_cart.place(relx=0.2, rely=0.2)
        self.init(self.frame_right)

        self.window.mainloop()
    def init(self, a):
        self.count_y=0.05
        # code for creating table
        self.e = Label(a,font=('Arial',14,'bold'),bg="#A39E93",fg="#FAF9F7", text=self.lst[0][0], borderwidth=5, relief=GROOVE)
        self.e.place(relx=0.15, rely=0.05, relwidth=0.38,relheight=0.04)
        self.e = Label(a,font=('Arial',14,'bold'),bg="#A39E93",fg="#FAF9F7", text=self.lst[0][1], borderwidth=5, relief=GROOVE)
        self.e.place(relx=0.50, rely=0.05, relwidth=0.38,relheight=0.04)
        for i in range(1,self.total_rows):
            for j in range(self.total_columns):
                '''self.e = Entry(a, width=20, fg='blue',
                               font=('Arial', 16, 'bold'))'''
                if j==0:
                    self.e = Label(a,font=('Arial',14,'bold'),bg="#A39E93",fg="#FAF9F7", text=self.lst[i][j], borderwidth=5, relief=GROOVE,anchor=W)
                    self.e.place(relx=0.15, rely=self.count_y+0.04, relwidth=0.43, relheight=0.04)
                elif j==1:
                    self.e = Label(a,font=('Arial',14),bg="#A39E93",fg="#FAF9F7", text=self.lst[i][j], borderwidth=5, relief=GROOVE)
                    self.e.place(relx=0.5, rely=self.count_y + 0.04, relwidth=0.38, relheight=0.04)
                    self.count_y+=0.04

    def add_Cart(self):
        try:
            f = open("pqr.txt", 'r')
            f.seek(0)
            s = f.read()
            mysql = g.get_conn(s)
            mycur = mysql.cursor()

            sql = "insert into cart values ('{}', '{}',{})".format(self.Model, self.Colour[self.temp], self.Price[self.temp])
            mycur.execute(sql)
            if mycur.rowcount > 0:
                mysql.commit()
                mb.showinfo("Cart","Items have been successfully added to cart.")
                self.window.destroy()
            else:
                mb.showerror("Error","There was a problem in adding this item to cart.")
            mysql.rollback()
        except Exception as e:
            mb.showerror("Error", e)

    def forward(self,image_number):
        self.image_number=image_number
        self.my_label.place_forget()

        self.my_label = Label(self.root_1, image=self.image_list[self.image_number - 1])
        self.button_forward = Button(self.root_1, text=">>", command=lambda: self.forward(self.image_number + 1),
                                font=('Arial', 14, 'bold'), bg="#A39E93", fg="#FAF9F7")
        self.button_back = Button(self.root_1, text="<<", command=lambda: self.back(self.image_number - 1), font=('Arial', 14, 'bold'),
                             bg="#A39E93", fg="#FAF9F7")
        if self.image_number == len(self.image_list):
            self.button_forward = Button(self.root_1, text=">>", state=DISABLED, font=('Arial', 14, 'bold'), bg="#A39E93",
                                    fg="#FAF9F7")
        self.my_label.place(relx=0.25, rely=0.012)
        self.button_back.place(relx=0.25, rely=0.942, relwidth=0.04, relheight=0.05)
        self.button_forward.place(relx=0.655, rely=0.942, relwidth=0.04, relheight=0.05)

        self.staus = Label(self.root_1, text=f"Image {self.image_number} of {len(self.image_list)}", bd=1, relief=SUNKEN, anchor=E,
                      font=('Arial', 14, 'bold'), bg="#A39E93", fg="#FAF9F7")
        self.staus.place(relx=0.29, rely=0.942, relwidth=0.365, relheight=0.05)

    def back(self,image_number):
        self.image_number = image_number
        self.my_label.place_forget()

        self.my_label = Label(self.root_1, image=self.image_list[self.image_number - 1])
        self.button_forward = Button(self.root_1, text=">>", command=lambda: self.forward(self.image_number + 1),
                                     font=('Arial', 14, 'bold'), bg="#A39E93", fg="#FAF9F7")
        self.button_back = Button(self.root_1, text="<<", command=lambda: self.back(self.image_number - 1),
                                  font=('Arial', 14, 'bold'),
                                  bg="#A39E93", fg="#FAF9F7")
        if self.image_number == 1:
            self.button_forward = Button(self.root_1, text="<<", state=DISABLED, font=('Arial', 14, 'bold'), bg="#A39E93",
                                    fg="#FAF9F7")

        self.my_label.place(relx=0.25, rely=0.012)
        self.button_back.place(relx=0.25, rely=0.942, relwidth=0.04, relheight=0.05)
        self.button_forward.place(relx=0.655, rely=0.942, relwidth=0.04, relheight=0.05)

        self.staus = Label(self.root_1, text=f"Image {self.image_number} of {len(self.image_list)}", bd=1,
                           relief=SUNKEN, anchor=E,
                           font=('Arial', 14, 'bold'), bg="#A39E93", fg="#FAF9F7")
        self.staus.place(relx=0.29, rely=0.942, relwidth=0.365, relheight=0.05)

    def on_option_change(self,event):
        self.price_option = self.options.get()
        self.colour_lbl.destroy()
        if self.price_option == self.Colour[0]:
            self.colour_lbl = Label(self.frame_bottom, text=f"₹. {self.Price[0]}", font=('Arial', 20, 'bold'), bg="#A39E93",
                               fg="#FAF9F7")
            self.colour_lbl.place(relx=0.65, rely=0.5)
            self.temp = 0
        elif self.price_option == self.Colour[1]:
            self.colour_lbl = Label(self.frame_bottom, text=f"₹. {self.Price[1]}", font=('Arial', 20, 'bold'), bg="#A39E93",
                               fg="#FAF9F7")
            self.colour_lbl.place(relx=0.65, rely=0.5)
            self.temp = 1
        elif self.price_option == self.Colour[2]:
            self.colour_lbl = Label(self.frame_bottom, text=f"₹. {self.Price[2]}", font=('Arial', 20, 'bold'), bg="#A39E93",
                               fg="#FAF9F7")
            self.colour_lbl.place(relx=0.65, rely=0.5)
            self.temp = 2

def hello(time):
    t=main(time)

