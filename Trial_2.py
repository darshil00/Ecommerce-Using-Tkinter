from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image
'''from tkinter import scrolledtext'''
from tkinter import font as tkFont
from tkinter import messagebox as mb
import get_conn as g
import re


mysql=g.get_con()
mycursor_1=mysql.cursor()

class main(tk.Frame):
    def _init_(self,root):
        Frame._init_(self,root)
        self.root=root
        self.top_frame = Frame(self.root, bg="#423D33")
        self.top_frame.grid(row=0, column=0, columnspan=3, sticky="nsew")

        self.center_frame = Frame(self.root, bg="#423D33")
        self.center_frame.grid(row=1, column=1, sticky="nsew")

        self.center_frame.columnconfigure(0, weight=1)
        self.center_frame.rowconfigure(0, weight=1)

        self.widget_frame = Frame(self.center_frame, bg="#423D33")
        self.widget_frame.grid(row=0, column=0, sticky="nsew")

        self.widget_frame.columnconfigure(0, weight=2)
        self.widget_frame.rowconfigure(0, weight=1)
        self.widget_frame.rowconfigure(1, weight=5)

        self.left_frame = Frame(self.root, bg="#27241D")
        self.left_frame.grid(row=1, column=0, sticky="nsew")
        self.right_frame = Frame(self.root, bg="#27241D")
        self.right_frame.grid(row=1, column=2, sticky="nsew")
        self.frame_top()
        self.login_page()

    def frame_top(self):
        self.title_lbl = Label(self.top_frame, text="Mobile Store",font=('Arial', 24, 'bold'), bg="#A39E93", fg="#FAF9F7").place(relx=0.45, rely=0.2,relwidth=0.18)
    def company_selection(self):
        self.Arial_font = tkFont.Font(family='Arial', size=14, weight='bold')
        self.options = tk.StringVar(self.root)
        self.companies=["Samsung", "Apple", "Oppo", "Redmi"]
        self.options.set("Company")
        self.company_Options = OptionMenu(self.widget_frame, self.options,*self.companies)

        self.company_Options.config(font=self.Arial_font, bg="#A39E93", fg="#FAF9F7", state=NORMAL)

        self.menu = self.root.nametowidget(self.company_Options.menuname)

        self.menu.config(font=self.Arial_font, bg="#A39E93", fg="#FAF9F7")
        self.company_Options.place(relx=0.5, rely=0.05, relwidth=0.2)

        self.company_lbl = Label(self.widget_frame, text="Select the company:",
                                 font=('Arial', 20, 'bold'), bg="#A39E93", fg="#FAF9F7").place(relx=0.05, rely=0.05,
                                                                                               relwidth=0.38)
        self.button_search = Button(self.widget_frame, text='Search', font=('Arial', 14, 'bold'), bg="#A39E93",
                                    fg="#FAF9F7", borderwidth=5, relief=GROOVE, state=NORMAL,
                                    command=self.selected_Company)
        self.button_search.place(relx=0.80, rely=0.05, relwidth=0.12, relheight=0.068)
        self.search_frame = Frame(self.widget_frame, bg="#423D33")
        self.search_frame.grid(row=1, column=0, sticky="nsew")


    def selected_Company(self):
        self.outputvalue=(self.options.get())
        if self.outputvalue=='Company':
            mb.showerror("Error","Please select a company before proceeding")
        else:
            if self.outputvalue==self.companies[1]:
                self.company_lbl = Button(self.search_frame, text="Select the company:",font=('Arial', 20, 'bold'), bg="#A39E93", fg="#FAF9F7").place(relx=0.05,rely=0.05,relwidth=0.38)
                self.scroll_option=Scrollbar(self.search_frame, orient="vertical")
                self.scroll_option.place(relx=0.97,relheight=1)
                button_phone_1 = Button(self.search_frame, text="Phone1", command=self.on_click_company,font=('Arial', 14, 'bold'), bg="#A39E93", fg="#FAF9F7")
                button_phone_1.place(relx=0.2, rely=0.2)
    def on_click_company(self):
        import Trial_5 as T5
        T5.bye_1()


    def login_page(self):
        for child in self.widget_frame.winfo_children():
            child.destroy()
        self.lbl_email=Label(self.widget_frame,text="Enter your name: ",font=('Arial',14,'bold'),bg="#A39E93",fg="#FAF9F7").place(relx=0.1,rely=0.2,relwidth=0.33)
        self.entry_name_signin=Entry(self.widget_frame,font=('Arial',14,'bold'),bg="#A39E93",fg="#FAF9F7")
        self.entry_name_signin.place(relx=0.53,rely=0.2,relwidth=0.25)
        self.lbl_pass=Label(self.widget_frame,text="Enter your pass: ",font=('Arial',14,'bold'),bg="#A39E93",fg="#FAF9F7").place(relx=0.1,rely=0.3,relwidth=0.33)
        self.entry_pass_signin=Entry(self.widget_frame,font=('Arial',14,'bold'),bg="#A39E93",fg="#FAF9F7",show='*')
        self.entry_pass_signin.place(relx=0.53,rely=0.3,relwidth=0.25)
        self.button_login = Button(self.widget_frame,text='Log in',font=('Arial',14,'bold'),bg="#A39E93",fg="#FAF9F7",relief=RAISED, command=self.logging_in)
        self.button_login.place(relx=0.2,rely=0.63)
        self.button_newacc = Button(self.widget_frame,text='Create new Account',font=('Arial',14,'bold'),bg="#A39E93",fg="#FAF9F7",relief=RAISED, command=self.create_account)
        self.button_newacc.place(relx=0.2,rely=0.73)

    def create_account(self):
        for child in self.widget_frame.winfo_children():
            child.destroy()
        self.lbl_name = Label(self.widget_frame, text="Enter your name: ", font=('Arial', 14, 'bold'),
                              bg="#A39E93", fg="#FAF9F7").place(relx=0.1, rely=0.1, relwidth=0.33)
        self.entry_name = Entry(self.widget_frame, font=('Arial', 14, 'bold'), bg="#A39E93", fg="#FAF9F7")
        self.entry_name.place(relx=0.53, rely=0.1, relwidth=0.25)
        self.lbl_email = Label(self.widget_frame, text="Enter your email: ", font=('Arial', 14, 'bold'),
                               bg="#A39E93", fg="#FAF9F7").place(relx=0.1, rely=0.2, relwidth=0.33)
        self.entry_email = Entry(self.widget_frame, font=('Arial', 14, 'bold'), bg="#A39E93", fg="#FAF9F7")
        self.entry_email.place(relx=0.53, rely=0.2, relwidth=0.25)
        self.lbl_address = Label(self.widget_frame, text="Enter your address: ", font=('Arial', 14, 'bold'),
                                 bg="#A39E93", fg="#FAF9F7").place(relx=0.1, rely=0.3, relwidth=0.33)
        self.entry_add = Entry(self.widget_frame, font=('Arial', 14, 'bold'), bg="#A39E93", fg="#FAF9F7")
        self.entry_add.place(relx=0.53, rely=0.3, relwidth=0.25)
        self.lbl_phone = Label(self.widget_frame, text="Enter your phone number: ", font=('Arial', 14, 'bold'),
                               bg="#A39E93", fg="#FAF9F7").place(relx=0.1, rely=0.4, relwidth=0.33)
        self.entry_phone = Entry(self.widget_frame, font=('Arial', 14, 'bold'), bg="#A39E93", fg="#FAF9F7")
        self.entry_phone.place(relx=0.53, rely=0.4, relwidth=0.25)
        self.lbl_pass = Label(self.widget_frame, text="Enter your password: ", font=('Arial', 14, 'bold'),
                              bg="#A39E93", fg="#FAF9F7").place(relx=0.1, rely=0.5, relwidth=0.33)
        self.entry_pass = Entry(self.widget_frame,show='*',font=('Arial', 14, 'bold'), bg="#A39E93", fg="#FAF9F7")
        self.entry_pass.place(relx=0.53, rely=0.5, relwidth=0.25)
        self.lbl_passconf = Label(self.widget_frame, text="Confirm your password: ", font=('Arial', 14, 'bold'),
                                  bg="#A39E93", fg="#FAF9F7").place(relx=0.1, rely=0.6, relwidth=0.33)
        self.entry_passconf = Entry(self.widget_frame,show='*', font=('Arial', 14, 'bold'), bg="#A39E93", fg="#FAF9F7")
        self.entry_passconf.place(relx=0.53, rely=0.6, relwidth=0.25)
        self.create_acc_btn = Button(self.widget_frame, text='Create Account', font=('Arial', 14, 'bold'), bg="#A39E93",
                                   fg="#FAF9F7", relief=RAISED, command=self.validate_info)
        self.create_acc_btn.place(relx=0.2, rely=0.8)

    def validate_info(self):
        temp=0
        self.validate_name=self.entry_name.get()
        self.email_validate=self.entry_email.get()
        self.regex_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        self.password_validate = self.entry_pass.get()
        self.password_conf_validate = self.entry_passconf.get()
        self.phone_validate = self.entry_phone.get()
        self.address_validate = self.entry_add.get()
        for child in self.widget_frame.winfo_children():
            child.destroy()
        if (re.fullmatch(self.regex_email, self.email_validate)):
            temp+=1
        else:
            mb.showerror("Error", "Please enter a valid Email address")
            self.create_account()
        if self.password_validate!=self.password_conf_validate:
            mb.showerror("Error","Password doesn't match!")
            self.create_account()
        if len(self.password_validate) < 6:
            mb.showerror("Error", "Please enter at least 6 characters in password")
            self.create_account()
        if not re.search("[A-Z]", self.password_validate):
            mb.showerror("Error", "Please enter at least one uppercase character in password")
            self.create_account()
        if not re.search("[a-z]", self.password_validate):
            mb.showerror("Error", "Please enter at least one lowercase character in password")
            self.create_account()
        if not re.search("[0-9]", self.password_validate):
            mb.showerror("Error", "Please enter at least one digit in password")
        if not re.search("[!@#$%^&*()]", self.password_validate):
            mb.showerror("Error","Please enter at least one special character in password")
            self.create_account()
        if re.search("\s", self.password_validate):
            mb.showerror("Error", "No Spaces Allowed in password")
            self.create_account()
        else:
            temp+=1
        if len(str(self.phone_validate))<10:
            mb.showerror("Error", "Please enter a valid phone number")
            self.create_account()
        elif len(str(self.phone_validate))>10:
            mb.showerror("Error", "Please enter a valid phone number")
            self.create_account()
        else:
            temp+=1
        if temp==3:
            self.new_database()

    def logging_in(self):

        self.name_signin_validate = self.entry_name_signin.get()
        self.password_signin_validate = self.entry_pass_signin.get()
        for child in self.widget_frame.winfo_children():
            child.destroy()
        self.mysql=g.get_conn(self.name_signin_validate)
        self.mycur=self.mysql.cursor()
        if mysql:
            pass
        else:
            mb.showerror("Try Again",f"{self.name_signin_validate} Email Id is not registered!")
        try:
            sql = "Select *from details"
            self.mycur.execute(sql)
            records = self.mycur.fetchall()
            for r in records:
                self.detail_list=list(r)
        except Exception as e:
            mb.showerror("Error",e)
        if self.detail_list[2]==self.password_signin_validate:
            self.logged_in()
        else:
            print(self.detail_list[2])
            mb.showerror("Login error","Invalid Password or name, Please try again.")
            self.login_page()

    def logged_in(self):
        for child in self.widget_frame.winfo_children():
            child.destroy()
        self.company_selection()


    def new_database(self):

        try:
            mycursor_1.execute(f"CREATE DATABASE IF NOT EXISTS {self.validate_name}")
        except Exception as e:
            mb.showerror("Error", f"{e}")
        self.mysql = g.get_conn(self.validate_name)
        self.mycursor = self.mysql.cursor()
        try:
            self.mycursor.execute("Create table details(Name varchar(20),Email_id varchar(20),password varchar(20),address varchar(20),contact_number varchar(20))")
        except Exception as e:
            mb.showerror("Error", f"{e}")
        try:
            self.mycursor.execute("Create table Cart(Model_name varchar(20),colour varchar(20),Price int)")
        except Exception as e:
            mb.showerror("Error", f"{e}")
        try:
            self.mycursor.execute("Create table orders(order_Pending varchar(20),order_completed varchar(20))")
        except Exception as e:
            mb.showerror("Error", f"{e}")
        mb.showinfo("Account Created","Congratulations! your account has been successfully created. ")
        self.login_page()

if _name_ == "_main_":
    win= tk.Tk()
    win.attributes('-fullscreen', True)
    win.title("MOBILE MANAGEMENT SYSTEM")
    win.columnconfigure(0, weight=2)
    win.columnconfigure(1, weight=4)
    win.columnconfigure(2, weight=1)
    win.rowconfigure(0, weight=1)
    win.rowconfigure(1, weight=4)
    m = main(win).grid(row=0,column=0,sticky="nsew")
    win.mainloop()