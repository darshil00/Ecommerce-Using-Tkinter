from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image
from tkinter import font as tkFont
from tkinter import ttk
from tkinter import messagebox as mb
import samsung_m31
import samsung_m52
import samsung_s21
import samsung_fe
import samsung_n20
import iphone_se
import iphone11
import iphone_12
import iphone_13
import iphone_13pro
import oppo_a55
import oppo_f19
import oppo_findx2
import oppo_reno5
import oppo_reno6
import Oneplus_9R
import Oneplus_Nord2
import Oneplus_CE
import Oneplus_9
import Oneplus_N10
import get_conn as g
import re

mysql=g.get_con()
mycursor_1=mysql.cursor()
class main():
    def __init__(self,root):
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

        self.left_frame = Frame(self.root, bg="#423D33")
        self.left_frame.grid(row=1, column=0, sticky="nsew")
        self.right_frame = Frame(self.root, bg="#423D33")
        self.right_frame.grid(row=1, column=2, sticky="nsew")
        self.frame_left_slideshow()
        self.frame_top()
        self.right_menu()
        self.login_page()
    def frame_left_slideshow(self):
        self.img_Company_1 = ImageTk.PhotoImage(Image.open("Samsung_logo.png").resize((300, 300)))  # width,height
        self.img_Company_2 = ImageTk.PhotoImage(Image.open("Apple_Logo.png").resize((300, 300)))
        self.img_Company_3 = ImageTk.PhotoImage(Image.open("Oppo_logo.png").resize((300, 300)))
        self.img_Company_4 = ImageTk.PhotoImage(Image.open("Oneplus_logo.png").resize((300, 300)))
        self.image_list = [self.img_Company_1, self.img_Company_2, self.img_Company_3, self.img_Company_4]
        self.i = 0
        self.slide_image = Label(self.left_frame, image=self.image_list[self.i])
        self.slide_image.place(relx=0.05, rely=0.2)
        self.start()
    def start(self):
        if self.i >= (len(self.image_list) - 1):
            self.i = 0
            self.slide_image.config(image=self.image_list[self.i])
        else:
            self.i = self.i + 1
            self.slide_image.configure(image=self.image_list[self.i])
        self.show = self.slide_image.after(5000, self.start)
    def frame_top(self):
        self.title_lbl = Label(self.top_frame, text="Mobile Store",font=('Arial', 24, 'bold'),borderwidth=5, relief=GROOVE, bg="#A39E93", fg="#FAF9F7").place(relx=0.42, rely=0.2,relwidth=0.18)
        self.img_quit = ImageTk.PhotoImage(Image.open("Logout.png").resize((50, 50)))
        self.quit_buttn=Button(self.top_frame, text="Quit",command=self.root.quit,font=('Arial', 24, 'bold'),image=self.img_quit,borderwidth=5, relief=GROOVE, bg="#A39E93", fg="#FAF9F7")
        self.quit_buttn.place(relx=0.95,rely=0)
    def login_page(self):
        for child in self.right_frame.winfo_children():
            if child==self.logout_menu:
                for child in self.logout_menu.winfo_children():
                    child.configure(state='disable')
            else:
                child.configure(state='disable')
        for child in self.widget_frame.winfo_children():
            child.destroy()
        self.lbl_email=Label(self.widget_frame,text="Enter your name: ",font=('Arial',14,'bold'),borderwidth=5, relief=GROOVE,bg="#A39E93",fg="#FAF9F7").place(relx=0.1,rely=0.2,relwidth=0.33)
        self.entry_name_signin=Entry(self.widget_frame,font=('Arial',14,'bold'),borderwidth=5, relief=GROOVE,bg="#A39E93",fg="#FAF9F7")
        self.entry_name_signin.place(relx=0.53,rely=0.2,relwidth=0.25)
        self.lbl_pass=Label(self.widget_frame,text="Enter your pass: ",font=('Arial',14,'bold'),borderwidth=5, relief=GROOVE,bg="#A39E93",fg="#FAF9F7").place(relx=0.1,rely=0.3,relwidth=0.33)
        self.entry_pass_signin=Entry(self.widget_frame,font=('Arial',14,'bold'),borderwidth=5, relief=GROOVE,bg="#A39E93",fg="#FAF9F7",show='*')
        self.entry_pass_signin.place(relx=0.53,rely=0.3,relwidth=0.25)
        self.button_login = Button(self.widget_frame,text='Log in',font=('Arial',14,'bold'),borderwidth=5, relief=GROOVE,bg="#A39E93",fg="#FAF9F7", command=self.logging_in)
        self.button_login.place(relx=0.2,rely=0.63)
        self.button_newacc = Button(self.widget_frame,text='Create new Account',font=('Arial',14,'bold'),borderwidth=5, relief=GROOVE,bg="#A39E93",fg="#FAF9F7", command=self.create_account)
        self.button_newacc.place(relx=0.2,rely=0.73)

    def create_account(self):
        for child in self.widget_frame.winfo_children():
            child.destroy()
        self.lbl_name = Label(self.widget_frame, text="Enter your name: ", font=('Arial', 14, 'bold'),borderwidth=5, relief=GROOVE,
                              bg="#A39E93", fg="#FAF9F7").place(relx=0.1, rely=0.1, relwidth=0.39)
        self.entry_name = Entry(self.widget_frame, font=('Arial', 14, 'bold'),borderwidth=5, relief=GROOVE, bg="#A39E93", fg="#FAF9F7")
        self.entry_name.place(relx=0.53, rely=0.1, relwidth=0.25)
        self.lbl_email = Label(self.widget_frame, text="Enter your email: ", font=('Arial', 14, 'bold'),borderwidth=5, relief=GROOVE,
                               bg="#A39E93", fg="#FAF9F7").place(relx=0.1, rely=0.2, relwidth=0.39)
        self.entry_email = Entry(self.widget_frame, font=('Arial', 14, 'bold'),borderwidth=5, relief=GROOVE, bg="#A39E93", fg="#FAF9F7")
        self.entry_email.place(relx=0.53, rely=0.2, relwidth=0.25)
        self.lbl_address = Label(self.widget_frame, text="Enter your address: ", font=('Arial', 14, 'bold'),borderwidth=5, relief=GROOVE,
                                 bg="#A39E93", fg="#FAF9F7").place(relx=0.1, rely=0.3, relwidth=0.39)
        self.entry_add = Entry(self.widget_frame, font=('Arial', 14, 'bold'),borderwidth=5, relief=GROOVE, bg="#A39E93", fg="#FAF9F7")
        self.entry_add.place(relx=0.53, rely=0.3, relwidth=0.25)
        self.lbl_phone = Label(self.widget_frame, text="Enter your phone number: ", font=('Arial', 14, 'bold'),borderwidth=5, relief=GROOVE,
                               bg="#A39E93", fg="#FAF9F7").place(relx=0.1, rely=0.4, relwidth=0.39)
        self.entry_phone = Entry(self.widget_frame, font=('Arial', 14, 'bold'),borderwidth=5, relief=GROOVE, bg="#A39E93", fg="#FAF9F7")
        self.entry_phone.place(relx=0.53, rely=0.4, relwidth=0.25)
        self.lbl_pass = Label(self.widget_frame, text="Enter your password: ", font=('Arial', 14, 'bold'),borderwidth=5, relief=GROOVE,
                              bg="#A39E93", fg="#FAF9F7").place(relx=0.1, rely=0.5, relwidth=0.39)
        self.entry_pass = Entry(self.widget_frame,show='*',font=('Arial', 14, 'bold'),borderwidth=5, relief=GROOVE, bg="#A39E93", fg="#FAF9F7")
        self.entry_pass.place(relx=0.53, rely=0.5, relwidth=0.25)
        self.lbl_passconf = Label(self.widget_frame, text="Confirm your password: ", font=('Arial', 14, 'bold'),borderwidth=5, relief=GROOVE,
                                  bg="#A39E93", fg="#FAF9F7").place(relx=0.1, rely=0.6, relwidth=0.39)
        self.entry_passconf = Entry(self.widget_frame,show='*', font=('Arial', 14, 'bold'),borderwidth=5, relief=GROOVE, bg="#A39E93", fg="#FAF9F7")
        self.entry_passconf.place(relx=0.53, rely=0.6, relwidth=0.25)
        self.create_acc_btn = Button(self.widget_frame, text='Create Account', font=('Arial', 14, 'bold'), bg="#A39E93",borderwidth=5, relief=GROOVE,
                                   fg="#FAF9F7", command=self.validate_info)
        self.create_acc_btn.place(relx=0.2, rely=0.8)
        self.back_btn = Button(self.widget_frame, text='Back', font=('Arial', 14, 'bold'), bg="#A39E93",
                                     borderwidth=5, relief=GROOVE,
                                     fg="#FAF9F7", command=self.login_page)
        self.back_btn.place(relx=0.5, rely=0.8)

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

    def new_database(self):
        try:
            mycursor_1.execute(f"CREATE DATABASE IF NOT EXISTS {self.validate_name}")
        except Exception as e:
            mb.showerror("Error", f"{e}")
        self.mysql = g.get_conn(self.validate_name)
        self.mycursor = self.mysql.cursor()
        try:
            self.mycursor.execute("Create table details(Name varchar(20),Email_id varchar(20),password varchar(20),address varchar(20),contact_number int)")
        except Exception as e:
            mb.showerror("Error", f"{e}")
        try:
            self.mycursor.execute("Create table Cart(Serial_num int,Model_name varchar(20),colour varchar(20),Price int)")
        except Exception as e:
            mb.showerror("Error", f"{e}")
        mb.showinfo("Account Created","Congratulations! your account has been successfully created. ")
        self.log_details()
    def log_details(self):
        self.mysql = g.get_conn(self.validate_name)
        self.mycur = self.mysql.cursor()
        try:
            self.sql = "insert into details values ('{}','{}','{}','{}',{})".format(self.validate_name,self.email_validate,self.password_validate,self.address_validate,self.phone_validate)
            self.mycur.execute(self.sql)
            if self.mycur.rowcount > 0:
                self.mysql.commit()
                print("Values have been inserted ")
            else:
                print("No value was inserted ")
                self.mysql.rollback()
        except Exception as e:
            print(e)
        self.login_page()
    def logging_in(self):
        self.name_signin_validate = self.entry_name_signin.get()
        self.password_signin_validate = self.entry_pass_signin.get()
        for child in self.widget_frame.winfo_children():
            child.destroy()
        self.mysql=g.get_conn(self.name_signin_validate)
        self.mycur=self.mysql.cursor()
        if self.name_signin_validate=="":
            mb.showerror("Error","Please enter a name")
            self.login_page()
        elif self.password_signin_validate=="":
            mb.showerror("Error", "Please enter a password")
            self.login_page()
        else:
            if mysql:
                pass
            else:
                mb.showerror("Try Again",f"{self.name_signin_validate} This user doesn't own an account!")
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
        for child in self.right_frame.winfo_children():
            if child == self.logout_menu:
                for child in self.logout_menu.winfo_children():
                    child.configure(state='normal')
            else:
                child.configure(state='normal')
        f = open("pqr.txt", 'w')
        f.write(self.name_signin_validate)
        f.close()
        self.company_selection()
    def company_selection(self):
        for child in self.widget_frame.winfo_children():
            child.destroy()
        for child in self.right_frame.winfo_children():
            if child == self.logout_menu:
                for child in self.logout_menu.winfo_children():
                    child.configure(state='normal')
            else:
                child.configure(state='normal')
        self.Arial_font = tkFont.Font(family='Arial', size=14, weight='bold')
        self.options = tk.StringVar(self.root)
        self.companies=["Samsung", "Apple", "Oppo", "One Plus"]
        self.options.set("Company")
        self.company_Options = OptionMenu(self.widget_frame, self.options,*self.companies)

        self.company_Options.config(font=self.Arial_font, bg="#A39E93", fg="#FAF9F7", state=NORMAL)

        self.menu = self.root.nametowidget(self.company_Options.menuname)

        self.menu.config(font=self.Arial_font, bg="#A39E93", fg="#FAF9F7")
        self.company_Options.place(relx=0.53, rely=0.05, relwidth=0.2)

        self.company_lbl = Label(self.widget_frame, text="Select the company:",
                                 font=('Arial', 20, 'bold'), bg="#A39E93", fg="#FAF9F7").place(relx=0.05, rely=0.05,
                                                                                               relwidth=0.42)
        self.button_search = Button(self.widget_frame, text='Search', font=('Arial', 14, 'bold'), bg="#A39E93",
                                    fg="#FAF9F7", borderwidth=5, relief=GROOVE, state=NORMAL,
                                    command=self.selected_Company)
        self.button_search.place(relx=0.80, rely=0.05, relwidth=0.12, relheight=0.068)
        self.search_frame = Frame(self.widget_frame, bg="#423D33")
        self.search_frame.grid(row=1, column=0, sticky="nsew")
    def selected_Company(self):
        self.outputvalue=(self.options.get())
        for child in self.right_frame.winfo_children():
            if child == self.logout_menu:
                for child in self.logout_menu.winfo_children():
                    child.configure(state='normal')
            else:
                child.configure(state='disable')
        if self.outputvalue=='Company':
            mb.showerror("Error","Please select a company before proceeding")
        else:
            if self.outputvalue == self.companies[0]:
                button_phone_1 = Button(self.search_frame, text="Samsung M31\n₹16999",
                                        command=lambda: self.on_click_company(1), font=('Arial', 20, 'bold'),
                                        bg="#A39E93", fg="#FAF9F7", anchor=E, borderwidth=10, relief=GROOVE)
                button_phone_1.place(relx=0.01, rely=0, relwidth=0.98, relheight=0.17)
                button_phone_2 = Button(self.search_frame, text="Samsung M52\n₹25999",
                                        command=lambda: self.on_click_company(2), font=('Arial', 20, 'bold'),
                                        bg="#A39E93", fg="#FAF9F7", anchor=E, borderwidth=10, relief=GROOVE)
                button_phone_2.place(relx=0.01, rely=0.2, relwidth=0.98, relheight=0.17)
                button_phone_3 = Button(self.search_frame, text="Samsung S21\n₹54999",
                                        command=lambda: self.on_click_company(3), font=('Arial', 20, 'bold'),
                                        bg="#A39E93", fg="#FAF9F7", anchor=E, borderwidth=10, relief=GROOVE)
                button_phone_3.place(relx=0.01, rely=0.4, relwidth=0.98, relheight=0.17)
                button_phone_4 = Button(self.search_frame, text="Samsung S20 FE\n₹21999",
                                        command=lambda: self.on_click_company(4), font=('Arial', 20, 'bold'),
                                        bg="#A39E93", fg="#FAF9F7", anchor=E, borderwidth=10, relief=GROOVE)
                button_phone_4.place(relx=0.01, rely=0.6, relwidth=0.98, relheight=0.17)
                button_phone_5 = Button(self.search_frame, text="Samsung Note20 Ultra\n₹104999",
                                        command=lambda: self.on_click_company(5), font=('Arial', 20, 'bold'),
                                        bg="#A39E93", fg="#FAF9F7", anchor=E, borderwidth=10, relief=GROOVE)
                button_phone_5.place(relx=0.01, rely=0.8, relwidth=0.98, relheight=0.17)

            elif self.outputvalue == self.companies[1]:
                button_phone_6 = Button(self.search_frame, text="Iphone SE\n₹30999",
                                        command=lambda: self.on_click_company(6), font=('Arial', 20, 'bold'),
                                        bg="#A39E93", fg="#FAF9F7", anchor=E, borderwidth=10, relief=GROOVE)
                button_phone_6.place(relx=0.01, rely=0, relwidth=0.98, relheight=0.17)
                button_phone_7 = Button(self.search_frame, text="Iphone 11\n₹40999",
                                        command=lambda: self.on_click_company(7), font=('Arial', 20, 'bold'),
                                        bg="#A39E93", fg="#FAF9F7", anchor=E, borderwidth=10, relief=GROOVE)
                button_phone_7.place(relx=0.01, rely=0.2, relwidth=0.98, relheight=0.17)
                button_phone_8 = Button(self.search_frame, text="Iphone 12\n₹70999",
                                        command=lambda: self.on_click_company(8), font=('Arial', 20, 'bold'),
                                        bg="#A39E93", fg="#FAF9F7", anchor=E, borderwidth=10, relief=GROOVE)
                button_phone_8.place(relx=0.01, rely=0.4, relwidth=0.98, relheight=0.17)
                button_phone_9 = Button(self.search_frame, text="Iphone 13\n₹70999",
                                        command=lambda: self.on_click_company(9), font=('Arial', 20, 'bold'),
                                        bg="#A39E93", fg="#FAF9F7", anchor=E, borderwidth=10, relief=GROOVE)
                button_phone_9.place(relx=0.01, rely=0.6, relwidth=0.98, relheight=0.17)
                button_phone_10 = Button(self.search_frame, text="Iphone 13 Pro\n₹149999",
                                         command=lambda: self.on_click_company(10), font=('Arial', 20, 'bold'),
                                         bg="#A39E93", fg="#FAF9F7", anchor=E, borderwidth=10, relief=GROOVE)
                button_phone_10.place(relx=0.01, rely=0.8, relwidth=0.98, relheight=0.17)

            elif self.outputvalue == self.companies[2]:
                button_phone_11 = Button(self.search_frame, text="OPPO A55\n₹15999",
                                         command=lambda: self.on_click_company(11), font=('Arial', 20, 'bold'),
                                         bg="#A39E93", fg="#FAF9F7", anchor=E, borderwidth=10, relief=GROOVE)
                button_phone_11.place(relx=0.01, rely=0, relwidth=0.98, relheight=0.17)
                button_phone_12 = Button(self.search_frame, text="OPPO f19 Pro\n₹19999",
                                         command=lambda: self.on_click_company(12), font=('Arial', 20, 'bold'),
                                         bg="#A39E93", fg="#FAF9F7", anchor=E, borderwidth=10, relief=GROOVE)
                button_phone_12.place(relx=0.01, rely=0.2, relwidth=0.98, relheight=0.17)
                button_phone_13 = Button(self.search_frame, text="OPPO Find X2\n₹40999",
                                         command=lambda: self.on_click_company(13), font=('Arial', 20, 'bold'),
                                         bg="#A39E93", fg="#FAF9F7", anchor=E, borderwidth=10, relief=GROOVE)
                button_phone_13.place(relx=0.01, rely=0.4, relwidth=0.98, relheight=0.17)
                button_phone_14 = Button(self.search_frame, text="OPPO Reno5\n₹21999",
                                         command=lambda: self.on_click_company(14), font=('Arial', 20, 'bold'),
                                         bg="#A39E93", fg="#FAF9F7", anchor=E, borderwidth=10, relief=GROOVE)
                button_phone_14.place(relx=0.01, rely=0.6, relwidth=0.98, relheight=0.17)
                button_phone_15 = Button(self.search_frame, text="OPPO Reno6\n₹28999",
                                         command=lambda: self.on_click_company(15), font=('Arial', 20, 'bold'),
                                         bg="#A39E93", fg="#FAF9F7", anchor=E, borderwidth=10, relief=GROOVE)
                button_phone_15.place(relx=0.01, rely=0.8, relwidth=0.98, relheight=0.17)
            elif self.outputvalue == self.companies[3]:
                button_phone_16 = Button(self.search_frame, text="Oneplus 9R\n₹39999",
                                         command=lambda: self.on_click_company(16),
                                         font=('Arial', 20, 'bold'), bg="#A39E93", fg="#FAF9F7", anchor=E,
                                         borderwidth=10, relief=GROOVE)
                button_phone_16.place(relx=0.01, rely=0, relwidth=0.98, relheight=0.17)
                button_phone_17 = Button(self.search_frame, text="Oneplus Nord 2\n₹27999",
                                         command=lambda: self.on_click_company(17),
                                         font=('Arial', 20, 'bold'), bg="#A39E93", fg="#FAF9F7", anchor=E,
                                         borderwidth=10, relief=GROOVE)
                button_phone_17.place(relx=0.01, rely=0.2, relwidth=0.98, relheight=0.17)
                button_phone_18 = Button(self.search_frame, text="Oneplus CE\n₹24999",
                                         command=lambda: self.on_click_company(18),
                                         font=('Arial', 20, 'bold'), bg="#A39E93", fg="#FAF9F7", anchor=E,
                                         borderwidth=10, relief=GROOVE)
                button_phone_18.place(relx=0.01, rely=0.4, relwidth=0.98, relheight=0.17)
                button_phone_19 = Button(self.search_frame, text="Oneplus 9\n₹51999",
                                         command=lambda: self.on_click_company(19),
                                         font=('Arial', 20, 'bold'), bg="#A39E93", fg="#FAF9F7", anchor=E,
                                         borderwidth=10, relief=GROOVE)
                button_phone_19.place(relx=0.01, rely=0.6, relwidth=0.98, relheight=0.17)
                button_phone_20 = Button(self.search_frame, text="One Plus N10\n₹32000",
                                         command=lambda: self.on_click_company(20),
                                         font=('Arial', 20, 'bold'), bg="#A39E93", fg="#FAF9F7", anchor=E,
                                         borderwidth=10,
                                         relief=GROOVE)
                button_phone_20.place(relx=0.01, rely=0.8, relwidth=0.98, relheight=0.17)
    def on_click_company(self,Phone_id):
        self.phone_id=Phone_id
        for child in self.search_frame.winfo_children():
            child.destroy()
        if self.phone_id == 1:
            samsung_m31.class_call(self.widget_frame)
        elif self.phone_id == 2:
            samsung_m52.class_call(self.widget_frame)
        elif self.phone_id == 3:
            samsung_s21.class_call(self.widget_frame)
        elif self.phone_id == 4:
            samsung_fe.class_call(self.widget_frame)
        elif self.phone_id == 5:
            samsung_n20.class_call(self.widget_frame)
        elif self.phone_id == 6:
            iphone_se.class_call(self.widget_frame)
        elif self.phone_id == 7:
            iphone11.class_call(self.widget_frame)
        elif self.phone_id == 8:
            iphone_12.class_call(self.widget_frame)
        elif self.phone_id == 9:
            iphone_13.class_call(self.widget_frame)
        elif self.phone_id == 10:
            iphone_13pro.class_call(self.widget_frame)
        elif self.phone_id == 11:
            oppo_a55.class_call(self.widget_frame)
        elif self.phone_id == 12:
            oppo_f19.class_call(self.widget_frame)
        elif self.phone_id == 13:
            oppo_findx2.class_call(self.widget_frame)
        elif self.phone_id == 14:
            oppo_reno5.class_call(self.widget_frame)
        elif self.phone_id == 15:
            oppo_reno6.class_call(self.widget_frame)
        elif self.phone_id == 16:
            Oneplus_9R.class_call(self.widget_frame)
        elif self.phone_id == 17:
            Oneplus_Nord2.class_call(self.widget_frame)
        elif self.phone_id == 18:
            Oneplus_CE.class_call(self.widget_frame)
        elif self.phone_id == 19:
            Oneplus_9.class_call(self.widget_frame)
        elif self.phone_id == 20:
            Oneplus_N10.class_call(self.widget_frame)

    def right_menu(self):
        self.logout_menu = Frame(self.right_frame,relief=SUNKEN, bg="#423D33")
        self.logout_menu.place(relx=0,rely=0,relwidth=1,relheight=0.1)
        self.logout_menu.columnconfigure(0, weight=1)
        self.logout_menu.rowconfigure(0, weight=1)
        self.button_logout=Button(self.logout_menu, text="Log out",borderwidth=5, relief=GROOVE, command=self.login_page,font=('Arial', 14, 'bold'), bg="#A39E93", fg="#FAF9F7")
        self.button_logout.place(relx=0.7,rely=0.18)

        self.button_back_menu = Button(self.logout_menu, text="Main menu", borderwidth=5, relief=GROOVE,
                                            command=self.company_selection, font=('Arial', 14, 'bold'), bg="#A39E93",
                                            fg="#FAF9F7")
        self.button_back_menu.place(relx=0.1, rely=0.18)

        self.button_check_cart = Button(self.right_frame, text="Check Cart",borderwidth=5, relief=GROOVE, command=self.open_cart,font=('Arial', 14, 'bold'), bg="#A39E93", fg="#FAF9F7")
        self.button_check_cart.place(relx=0.1,rely=0.15)

        self.button_change_details = Button(self.right_frame, text="Change Info",borderwidth=5, relief=GROOVE, command=self.edit_details,font=('Arial', 14, 'bold'), bg="#A39E93", fg="#FAF9F7")
        self.button_change_details.place(relx=0.1, rely=0.25)
        self.img_logo_store = ImageTk.PhotoImage(Image.open("Mobile_Store_logo.png").resize((300, 300)))
        self.my_label = Label(self.right_frame, image=self.img_logo_store)
        self.my_label.place(relx=0.05, rely=0.4)

    def open_cart(self):
        for child in self.widget_frame.winfo_children():
            child.destroy()
        for child in self.right_frame.winfo_children():
            if child == self.logout_menu:
                for child in self.logout_menu.winfo_children():
                    child.configure(state='normal')
            else:
                child.configure(state='disable')
        self.mysql_4 = g.get_conn(self.name_signin_validate)
        self.mycursor_4 = self.mysql_4.cursor()
        self.list_check_cart=[]
        self.list_check_cart.clear()
        try:
            sql = "Select *from Cart"
            self.mycursor_4.execute(sql)
            self.records = self.mycursor_4.fetchall()
            for r in self.records:
                self.list_check_cart.append(r)
        except Exception as e:
            mb.showerror("Error",e)
        self.total_rows_cart = len(self.list_check_cart)
        self.total_columns_cart = len(self.list_check_cart[0])
        self.count_y = 0
        # code for creating table
        self.e = Label(self.widget_frame, font=("Arial", 14, 'bold'), text="Item Id", borderwidth=3, relief=GROOVE,
                       bg="#A39E93", fg="#FAF9F7")
        self.e.place(relx=0.05, rely=0, relwidth=0.2, relheight=0.07)
        self.e = Label(self.widget_frame, font=("Arial", 14, 'bold'), text="Model", borderwidth=3, relief=GROOVE,bg="#A39E93",fg="#FAF9F7")
        self.e.place(relx=0.25, rely=0, relwidth=0.25, relheight=0.07)
        self.e = Label(self.widget_frame, font=("Arial", 14), text="Colour", borderwidth=3, relief=GROOVE,bg="#A39E93",fg="#FAF9F7")
        self.e.place(relx=0.5, rely=0, relwidth=0.25, relheight=0.07)
        self.e = Label(self.widget_frame, font=("Arial", 14), text="Price", borderwidth=3,
                           relief=GROOVE,bg="#A39E93",fg="#FAF9F7")
        self.e.place(relx=0.75, rely=0,relwidth=0.2, relheight=0.07)
        if self.total_rows_cart<11:
            pass
        elif self.total_rows_cart>=11:
            self.total_rows_cart=11
        self.mysql = g.get_conn(self.name_signin_validate)
        self.mycursor = self.mysql.cursor()
        for i in range(0, self.total_rows_cart):
            for j in range(self.total_columns_cart):
                if j == 0:
                    self.e = Label(self.widget_frame, font=("Arial", 14, 'bold'), text=self.list_check_cart[i][j], borderwidth=3, relief=GROOVE,bg="#A39E93",fg="#FAF9F7")
                    self.e.place(relx=0.05, rely=self.count_y + 0.07, relwidth=0.2, relheight=0.07)
                elif j == 1:
                    self.e = Label(self.widget_frame, font=("Arial", 14), text=self.list_check_cart[i][j], borderwidth=3, relief=GROOVE,bg="#A39E93",fg="#FAF9F7")
                    self.e.place(relx=0.25, rely=self.count_y + 0.07, relwidth=0.25, relheight=0.07)
                elif j == 2:
                    self.e = Label(self.widget_frame, font=("Arial", 14), text=f"{self.list_check_cart[i][j]}", borderwidth=3, relief=GROOVE,bg="#A39E93",fg="#FAF9F7")
                    self.e.place(relx=0.5, rely=self.count_y + 0.07,relwidth=0.25, relheight=0.07)
                elif j==3:
                    self.e = Label(self.widget_frame, font=("Arial", 14), text=f"₹ {self.list_check_cart[i][j]}",
                                   borderwidth=3, relief=GROOVE, bg="#A39E93", fg="#FAF9F7")
                    self.e.place(relx=0.75, rely=self.count_y + 0.07, relwidth=0.2, relheight=0.07)
                    self.count_y += 0.07
        self.lbl_delete_cart=Label(self.widget_frame,font=("Arial", 14), text="Enter Item Id", borderwidth=5, relief=GROOVE,bg="#A39E93",fg="#FAF9F7")
        self.entry_item_id=Entry(self.widget_frame,font=("Arial", 14), borderwidth=7, relief=GROOVE,bg="#A39E93",fg="#FAF9F7")
        self.delete_item=Button(self.widget_frame,font=("Arial", 14),text="Delete Item",command=self.deleting_item, borderwidth=5, relief=GROOVE,bg="#A39E93",fg="#FAF9F7")
        self.check_out = Button(self.widget_frame, font=("Arial", 14), text="Checkout",command=self.check_out, borderwidth=5,
                                  relief=GROOVE, bg="#A39E93", fg="#FAF9F7")
        self.lbl_delete_cart.place(relx=0.05,rely=0.9,relwidth=0.2,relheight=0.07)
        self.entry_item_id.place(relx=0.28, rely=0.9, relwidth=0.2, relheight=0.07)
        self.delete_item.place(relx=0.51, rely=0.9, relwidth=0.2, relheight=0.07)
        self.check_out.place(relx=0.74, rely=0.9, relwidth=0.2, relheight=0.07)
        self.lbl_totalcost = Label(self.widget_frame, font=("Arial", 24,'bold'), text="Total Cost: ", borderwidth=5,
                                     relief=GROOVE, bg="#A39E93", fg="#FAF9F7")
        self.total_cost=0
        for i in range(0, self.total_rows_cart):
            for j in range(self.total_columns_cart):
                if j == 3:
                    self.total_cost += int(self.list_check_cart[i][j])
        self.lbl_total_cost = Label(self.widget_frame, font=("Arial", 24,'bold'), text=f"₹{str(self.total_cost)}", borderwidth=5,relief=GROOVE, bg="#A39E93", fg="#FAF9F7")
        self.lbl_totalcost.place(relx=0.05, rely=0.8, relwidth=0.5, relheight=0.07)
        self.lbl_total_cost.place(relx=0.5, rely=0.8, relwidth=0.45, relheight=0.07)
    def deleting_item(self):
        self.mysql_5= g.get_conn(self.name_signin_validate)
        self.mycursor_5 = self.mysql_5.cursor()
        try:
            self.item_id = self.entry_item_id.get()
            sql = "delete from cart where Serial_num = {}".format(int(self.item_id))
            self.mycursor_5.execute(sql)
            if self.mycursor_5.rowcount > 0:
                self.mysql_5.commit()
                mb.showinfo("Deleted","item has been deleted")
            else:
                mb.showerror("Error","item was not deleted")
                self.mysql.rollback()
        except Exception as e:
            print(e)
        self.company_selection()
    def check_out(self):
        mb.showinfo("Purchase Successful", f"Your purchase was successful, \n total cost of the purchase was ₹{self.total_cost}.\nThank You!")
        self.mysql_3 = g.get_conn(self.name_signin_validate)
        self.mycursor_3 = self.mysql_3.cursor()
        for i in range(0, self.total_rows_cart):
            for j in range(self.total_columns_cart):
                if j == 0:
                    try:
                        sql = "delete from cart where Serial_num = {}".format(int(self.list_check_cart[i][j]))
                        self.mycursor_3.execute(sql)
                        if self.mycursor_3.rowcount > 0:
                            self.mysql_3.commit()
                        else:
                            self.mysql.rollback()
                    except Exception as e:
                        print(e)
        self.company_selection()
    def edit_details(self):
        for child in self.widget_frame.winfo_children():
            child.destroy()
        for child in self.right_frame.winfo_children():
            if child == self.logout_menu:
                for child in self.logout_menu.winfo_children():
                    child.configure(state='normal')
            else:
                child.configure(state='disable')
        try:
            sql = "Select *from details"
            self.mycur.execute(sql)
            records = self.mycur.fetchall()
            for r in records:
                self.list_details_edit=list(r)
        except Exception as e:
            mb.showerror("Error", e)

        self.lbl_name = Label(self.widget_frame, text="Enter your name: ", font=('Arial', 14, 'bold'), borderwidth=5,
                              relief=GROOVE,
                              bg="#A39E93", fg="#FAF9F7").place(relx=0.1, rely=0.1, relwidth=0.39)
        self.name_edit = StringVar(self.widget_frame, value=self.list_details_edit[0])
        self.entry_name = Entry(self.widget_frame, font=('Arial', 14, 'bold'),textvariable=self.name_edit, borderwidth=5, relief=GROOVE,
                                bg="#A39E93", fg="#FAF9F7")
        self.entry_name.place(relx=0.53, rely=0.1, relwidth=0.25)
        self.lbl_email = Label(self.widget_frame, text="Enter your email: ", font=('Arial', 14, 'bold'), borderwidth=5,
                               relief=GROOVE,
                               bg="#A39E93", fg="#FAF9F7").place(relx=0.1, rely=0.2, relwidth=0.39)
        self.email_edit = StringVar(self.widget_frame, value=self.list_details_edit[1])
        self.entry_email = Entry(self.widget_frame, font=('Arial', 14, 'bold'),textvariable=self.email_edit, borderwidth=5, relief=GROOVE,
                                 bg="#A39E93", fg="#FAF9F7")
        self.entry_email.place(relx=0.53, rely=0.2, relwidth=0.25)
        self.lbl_address = Label(self.widget_frame, text="Enter your address: ", font=('Arial', 14, 'bold'),
                                 borderwidth=5, relief=GROOVE,
                                 bg="#A39E93", fg="#FAF9F7").place(relx=0.1, rely=0.3, relwidth=0.39)
        self.add_edit = StringVar(self.widget_frame, value=self.list_details_edit[3])
        self.entry_add = Entry(self.widget_frame, font=('Arial', 14, 'bold'),textvariable=self.add_edit, borderwidth=5, relief=GROOVE,
                               bg="#A39E93", fg="#FAF9F7")
        self.entry_add.place(relx=0.53, rely=0.3, relwidth=0.25)
        self.lbl_phone = Label(self.widget_frame, text="Enter your phone number: ", font=('Arial', 14, 'bold'),
                               borderwidth=5, relief=GROOVE,
                               bg="#A39E93", fg="#FAF9F7").place(relx=0.1, rely=0.4, relwidth=0.39)
        self.phone_edit = StringVar(self.widget_frame, value=self.list_details_edit[4])
        self.entry_phone = Entry(self.widget_frame, font=('Arial', 14, 'bold'),textvariable=self.phone_edit, borderwidth=5, relief=GROOVE,
                                 bg="#A39E93", fg="#FAF9F7")
        self.entry_phone.place(relx=0.53, rely=0.4, relwidth=0.25)
        self.lbl_pass = Label(self.widget_frame, text="Enter your password: ", font=('Arial', 14, 'bold'),
                              borderwidth=5, relief=GROOVE,
                              bg="#A39E93", fg="#FAF9F7").place(relx=0.1, rely=0.5, relwidth=0.39)
        self.pass_edit = StringVar(self.widget_frame, value=self.list_details_edit[2])
        self.entry_pass = Entry(self.widget_frame, show='*', font=('Arial', 14, 'bold'),textvariable=self.pass_edit, borderwidth=5, relief=GROOVE,
                                bg="#A39E93", fg="#FAF9F7")
        self.entry_pass.place(relx=0.53, rely=0.5, relwidth=0.25)
        self.create_acc_btn = Button(self.widget_frame, text='Update details', font=('Arial', 14, 'bold'), bg="#A39E93",
                                     borderwidth=5, relief=GROOVE,
                                     fg="#FAF9F7", command=self.update_details)
        self.create_acc_btn.place(relx=0.2, rely=0.8)
    def update_details(self):
        self.update_name=str(self.entry_name.get())
        self.update_email =str(self.entry_email.get())
        self.update_pass =str(self.entry_pass.get())
        self.update_add =str(self.entry_add.get())
        self.update_phone =int(self.entry_phone.get())

        try:
            self.sql="update details set Name='{}' where Name='{}'".format(self.update_name,self.list_details_edit[0])
            self.mycur.execute(self.sql)
            if self.mycur.rowcount > 0:
                self.mysql.commit()
                mb.showinfo("Updated","Details have been updated")
            else:
                self.mysql.rollback()
            self.sql = "update details set Email_id='{}' where Email_id='{}'".format(self.update_email,self.list_details_edit[1])
            self.mycur.execute(self.sql)
            if self.mycur.rowcount > 0:
                self.mysql.commit()
                mb.showinfo("Updated", "Details have been updated")
            else:
                self.mysql.rollback()
            self.sql = "update details set password='{}' where password='{}'".format(self.update_pass,
                                                                                     self.list_details_edit[2])
            self.mycur.execute(self.sql)
            if self.mycur.rowcount > 0:
                self.mysql.commit()
                mb.showinfo("Updated", "Details have been updated")
            else:
                self.mysql.rollback()
            self.sql = "update details set address='{}' where address='{}'".format(self.update_add,
                                                                                     self.list_details_edit[3])
            self.mycur.execute(self.sql)
            if self.mycur.rowcount > 0:
                self.mysql.commit()
                mb.showinfo("Updated", "Details have been updated")
            else:
                self.mysql.rollback()
            self.sql = "update details set contact_number='{}' where contact_number='{}'".format(self.update_phone,
                                                                                   self.list_details_edit[4])
            self.mycur.execute(self.sql)
            if self.mycur.rowcount > 0:
                self.mysql.commit()
                mb.showinfo("Updated", "Details have been updated")
            else:
                self.mysql.rollback()
            self.logged_in()
        except Exception as e:
            print(e)
win= tk.Tk()
win.attributes('-fullscreen', True)
win.title("MOBILE MANAGEMENT SYSTEM")
win.columnconfigure(0, weight=2)
win.columnconfigure(1, weight=4)
win.columnconfigure(2, weight=2)
win.rowconfigure(0, weight=1)
win.rowconfigure(1, weight=4)
m = main(win)
win.mainloop()