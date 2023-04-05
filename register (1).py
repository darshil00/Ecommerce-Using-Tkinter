from tkinter import *
import mysql.connector as my
from tkinter import messagebox

mysql = my.connect(host= 'localhost',
                  user= 'root',
                  passwd= '',
                  database= 'emp_info')

mycur = mysql.cursor()

mycur.execute("Create table if not exists record( name varchar(30),username varchar(10),password varchar(16), email text)")


#create window

win = Tk()
win.geometry('500x450')
win.title("Login Registration")
win.resizable(False, False)


fullname = StringVar()
username  =StringVar()
password = StringVar()
user1 = StringVar()
passw1 = StringVar()
email=StringVar()


#insert rows

def insert_record():
    count = 0
    warn = ''

    if fullname.get() == '':
        warn = "Name cannot be empty"
    else:
        count +=1

    if username.get() == '':
        warn = "UserName cannot be empty"
    else:
        count +=1

    if password.get() == '':
        warn = "passwords cannot be empty"
    else:
        count +=1

    if email.get() == '':
        warn = "Email cannot be empty"
    else:
        count +=1

    if count == 4:
        try:
            sql = "insert into record values('{}', '{}','{}', '{}')".format(fullname.get(),
                                                                            username.get(),
                                                                            password.get(),
                                                                            email.get())
                                                                            
            mycur.execute(sql)
            if mycur.rowcount >0:
                mysql.commit()
                print("Values have been inserted ")
            else:
                print("No value was inserted ")
                mysql.rollback()
        except Exception as e:
            messagebox.showerror('', e)
    else:
        messagebox.showerror("Error", warn)


def login_response():
    count = 0
    warn =''
    try:
        sql = "Select * from record"
        mycur.execute(sql)
        r = mycur.fetechall()
        for i in r:
            user = i[0]
            paswd = i[1]
    except Exception as e:
        print(e)
        
    if user1.get() =='':
        warn ="username cannot be empty"
    else:
        count+= 1

    if passw1.get() =='':
        warn ="password cannot be empty"
    else:
        count+= 1
    if count==2:
        if user == user1.get()and paswd == passw1.get():
            messagebox.showinfo("login Status","Login Successful")
        else:
            messagebox.showinfo("login Status","invalid username or password")

    else:
        messagebox.showinfo("" ,warn)

            

def registration():
    f = Frame(win, height= 450, width = 500)
    
    Label (f, text = "Full Name").place(x = 150, y = 120)
    Entry(f, textvariable = fullname).place(x = 150, y = 140)

    Label (f, text = "Username Name").place(x = 150, y = 170)
    Entry(f, textvariable = username).place(x = 150, y = 190)


    Label (f, text = "Password").place(x = 150, y = 220)
    Entry(f, textvariable = password).place(x = 150, y = 240)


    Label (f, text = "Email").place(x = 150, y = 270)
    Entry(f, textvariable = email).place(x = 150, y = 290)

    Button(f, text= "register", command = insert_record).place(x= 200, y = 330)
    f.place(x= 0, y= 0)

def login():
    f = Frame(win, height= 450, width = 500)

    Label(f, text ='Login').place(x = 150, y = 200)

    Label(f, text ='Username').place(x = 150, y = 200)
    user = Entry(f, textvariable = user1)
    user.place(x = 150, y = 220)
    
    Label(f, text ='password').place(x = 150, y = 250)
    user = Entry(f, textvariable = passw1)
    user.place(x = 150, y = 270)

    Button(f, text = "log in", command = login_response).place(x =220, y = 300)
    Button(f, text = "Don't have an account", command = registration).place(x =220, y = 350)
    f.place(x=0, y= 0)

login()
win.mainloop()





