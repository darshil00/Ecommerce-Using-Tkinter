from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image
from tkinter import font as tkFont
from tkinter import ttk
from tkinter import messagebox as mb
import iphone11 as ip11
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

        self.left_frame = Frame(self.root, bg="#27241D")
        self.left_frame.grid(row=1, column=0, sticky="nsew")
        self.right_frame = Frame(self.root, bg="#A39E93")
        self.right_frame.grid(row=1, column=2, sticky="nsew")
        self.frame_top()
        self.right_menu()
        self.login_page()

    def frame_top(self):
        self.title_lbl = Label(self.top_frame, text="Mobile Store",font=('Arial', 24, 'bold'), bg="#A39E93", fg="#FAF9F7").place(relx=0.45, rely=0.2,relwidth=0.18)

    def login_page(self):
        for child in self.right_frame.winfo_children():
            if child==self.logout_menu:
                for child in self.logout_menu.winfo_children():
                    child.configure(state='disable')
            else:
                child.configure(state='disable')
        for child in self.widget_frame.winfo_children():
            child.destroy()
        self.lbl_email=Label(self.widget_frame,text="Enter your name: ",font=('Arial',14,'bold'),bg="#A39E93",fg="#FAF9F7").place(relx=0.1,rely=0.2,relwidth=0.33)
        self.entry_name_signin=Entry(self.widget_frame,font=('Arial',14,'bold'),bg="#A39E93",fg="#FAF9F7")
        self.entry_name_signin.place(relx=0.53,rely=0.2,relwidth=0.25)
        self.lbl_pass=Label(self.widget_frame,text="Enter your pass: ",font=('Arial',14,'bold'),bg="#A39E93",fg="#FAF9F7").place(relx=0.1,rely=0.3,relwidth=0.33)
        self.entry_pass_signin=Entry(self.widget_frame,font=('Arial',14,'bold'),bg="#A39E93",fg="#FAF9F7",show='*')
        self.entry_pass_signin.place(relx=0.53,rely=0.3,relwidth=0.25)
        self.button_login = Button(self.widget_frame,text='Log in',borderwidth=5, relief=GROOVE,font=('Arial',14,'bold'),bg="#A39E93",fg="#FAF9F7", command=self.logging_in)
        self.button_login.place(relx=0.2,rely=0.63)
        self.button_newacc = Button(self.widget_frame,text='Create new Account',borderwidth=5, relief=GROOVE,font=('Arial',14,'bold'),bg="#A39E93",fg="#FAF9F7", command=self.create_account)
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
            if self.outputvalue==self.companies[0]:
                pass
            elif self.outputvalue==self.companies[1]:
                button_phone_6 = Button(self.search_frame, text="Iphone 11\n₹40999", command=lambda: self.on_click_company(6),font=('Arial', 20, 'bold'), bg="#A39E93", fg="#FAF9F7",anchor=E,borderwidth=10,relief=GROOVE)
                button_phone_6.place(relx=0.01, rely=0,relwidth=0.98,relheight=0.17)
                button_phone_7 = Button(self.search_frame, text="Iphone 12\n₹40999", command=lambda: self.on_click_company(7),font=('Arial', 20, 'bold'), bg="#A39E93", fg="#FAF9F7",anchor=E,borderwidth=10,relief=GROOVE)
                button_phone_7.place(relx=0.01, rely=0.2,relwidth=0.98,relheight=0.17)
                button_phone_8 = Button(self.search_frame, text="Iphone 13\n₹40999",
                                        command=lambda: self.on_click_company(8),
                                        font=('Arial', 20, 'bold'), bg="#A39E93", fg="#FAF9F7",anchor=E, borderwidth=10, relief=GROOVE)
                button_phone_8.place(relx=0.01, rely=0.4,relwidth=0.98,relheight=0.17)
                button_phone_9 = Button(self.search_frame, text="Iphone 13 Pro\n₹40999",
                                        command=lambda: self.on_click_company(9),
                                        font=('Arial', 20, 'bold'), bg="#A39E93", fg="#FAF9F7",anchor=E, borderwidth=10, relief=GROOVE)
                button_phone_9.place(relx=0.01, rely=0.6,relwidth=0.98,relheight=0.17)
                button_phone_10 = Button(self.search_frame, text="Iphone 13 SE\n₹40999",
                                        command=lambda: self.on_click_company(10),
                                        font=('Arial', 20, 'bold'), bg="#A39E93", fg="#FAF9F7",anchor=E, borderwidth=10, relief=GROOVE)
                button_phone_10.place(relx=0.01, rely=0.8,relwidth=0.98,relheight=0.17)

            elif self.outputvalue==self.companies[2]:
                #Oppo
                pass
            elif self.outputvalue==self.companies[3]:
                #One Plus
                pass
    def on_click_company(self,Phone_id):
        self.phone_id=Phone_id
        for child in self.search_frame.winfo_children():
            child.destroy()
        if self.phone_id==1:
            ip11.class_call(self.widget_frame)
        elif self.phone_id==2:
            ip11.class_call(self.widget_frame)
        elif self.phone_id ==3:
            ip11.class_call(self.widget_frame)
        elif self.phone_id==4:
            ip11.class_call(self.widget_frame)
        elif self.phone_id==5:
            ip11.class_call(self.widget_frame)
        elif self.phone_id==6:
            ip11.class_call(self.widget_frame)
        elif self.phone_id==7:
            ip11.class_call(self.widget_frame)
        elif self.phone_id==8:
            ip11.class_call(self.widget_frame)
        elif self.phone_id==9:
            ip11.class_call(self.widget_frame)
        elif self.phone_id==10:
            ip11.class_call(self.widget_frame)
        elif self.phone_id==11:
            ip11.class_call(self.widget_frame)
        elif self.phone_id==12:
            ip11.class_call(self.widget_frame)
        elif self.phone_id==13:
            ip11.class_call(self.widget_frame)
        elif self.phone_id==14:
            ip11.class_call(self.widget_frame)
        elif self.phone_id==15:
            ip11.class_call(self.widget_frame)
        elif self.phone_id==16:
            ip11.class_call(self.widget_frame)
        elif self.phone_id==17:
            ip11.class_call(self.widget_frame)
        elif self.phone_id==18:
            ip11.class_call(self.widget_frame)
        elif self.phone_id==19:
            ip11.class_call(self.widget_frame)
        elif self.phone_id==20:
            ip11.class_call(self.widget_frame)

    def right_menu(self):
        self.logout_menu = Frame(self.right_frame,relief=SUNKEN, bg="#A39E93")
        self.logout_menu.place(relx=0,rely=0,relwidth=1,relheight=0.1)
        self.logout_menu.columnconfigure(0, weight=1)
        self.logout_menu.rowconfigure(0, weight=1)
        self.button_logout=Button(self.logout_menu, text="Log out",borderwidth=5, relief=GROOVE, command=self.login_page,font=('Arial', 14, 'bold'), bg="#A39E93", fg="#FAF9F7")
        self.button_logout.place(relx=0.7,rely=0.18)

        self.button_check_purchase = Button(self.logout_menu, text="Main menu", borderwidth=5, relief=GROOVE,
                                            command=self.company_selection, font=('Arial', 14, 'bold'), bg="#A39E93",
                                            fg="#FAF9F7")
        self.button_check_purchase.place(relx=0.1, rely=0.18)

        self.button_check_cart = Button(self.right_frame, text="Check Cart",borderwidth=5, relief=GROOVE, command=self.open_cart,font=('Arial', 14, 'bold'), bg="#A39E93", fg="#FAF9F7")
        self.button_check_cart.place(relx=0.1,rely=0.2)

        self.button_change_details = Button(self.right_frame, text="Change Info",borderwidth=5, relief=GROOVE, command=self.edit_details,font=('Arial', 14, 'bold'), bg="#A39E93", fg="#FAF9F7")
        self.button_change_details.place(relx=0.1, rely=0.4)

    def open_cart(self):
        for child in self.widget_frame.winfo_children():
            child.destroy()
        self.list_check_cart=[]
        try:
            sql = "Select *from Cart"
            self.mycur.execute(sql)
            records = self.mycur.fetchall()
            for r in records:
                self.list_check_cart.append(r)
        except Exception as e:
            mb.showerror("Error",e)
        self.total_rows_cart = len(self.list_check_cart)
        self.total_columns_cart = len(self.list_check_cart[0])
        self.count_y = 0
        # code for creating table
        self.e = Label(self.widget_frame, font=("Arial", 14, 'bold'), text="Model", borderwidth=3, relief=GROOVE,bg="#A39E93",fg="#FAF9F7")
        self.e.place(relx=0.05, rely=0, relwidth=0.38, relheight=0.07)
        self.e = Label(self.widget_frame, font=("Arial", 14), text="Colour", borderwidth=3, relief=GROOVE,bg="#A39E93",fg="#FAF9F7")
        self.e.place(relx=0.45, rely=0, relwidth=0.38, relheight=0.07)
        self.e = Label(self.widget_frame, font=("Arial", 14), text="Price", borderwidth=3,
                           relief=GROOVE,bg="#A39E93",fg="#FAF9F7")
        self.e.place(relx=0.85, rely=0,relwidth=0.14, relheight=0.07)

        for i in range(0, 11):
            for j in range(self.total_columns_cart):
                if j == 0:
                    self.e = Label(self.widget_frame, font=("Arial", 14, 'bold'), text=self.list_check_cart[i][j], borderwidth=3, relief=GROOVE,bg="#A39E93",fg="#FAF9F7")
                    self.e.place(relx=0.05, rely=self.count_y + 0.07, relwidth=0.38, relheight=0.07)
                elif j == 1:
                    self.e = Label(self.widget_frame, font=("Arial", 14), text=self.list_check_cart[i][j], borderwidth=3, relief=GROOVE,bg="#A39E93",fg="#FAF9F7")
                    self.e.place(relx=0.45, rely=self.count_y + 0.07, relwidth=0.38, relheight=0.07)
                elif j == 2:
                    self.e = Label(self.widget_frame, font=("Arial", 14), text=f"₹ {self.list_check_cart[i][j]}", borderwidth=3, relief=GROOVE,bg="#A39E93",fg="#FAF9F7")
                    self.e.place(relx=0.85, rely=self.count_y + 0.07,relwidth=0.14, relheight=0.07)
                    self.count_y += 0.07
        self.lbl_delete_cart=Label(self.widget_frame,font=("Arial", 14), text="Enter Item Id", borderwidth=3, relief=GROOVE,bg="#A39E93",fg="#FAF9F7")
        self.enrty_item_id=Entry(self.widget_frame,font=("Arial", 14), borderwidth=3, relief=GROOVE,bg="#A39E93",fg="#FAF9F7")
        self.delete_item=Button(self.widget_frame,font=("Arial", 14), borderwidth=3, relief=GROOVE,bg="#A39E93",fg="#FAF9F7")

        

    def edit_details(self):
        for child in self.widget_frame.winfo_children():
            child.destroy()

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