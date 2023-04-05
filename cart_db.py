import get_conn as g
from crudefunc import details
#from crudefunc import Cart_crude
global name
name=input("enter ur namwe :")
mysql =g.get_con()
mycursor=mysql.cursor()
try:
    mycursor.execute("CREATE DATABASE IF NOT EXISTS %s" %name)
except Exception as e:
    print(e)

mysql =g.get_conn(name)
mycursor=mysql.cursor()

try:
    mycursor.execute("Create table Cart(Model_name varchar(20),colour varchar(20),Price int)")
except Exception as e:
    print(e)

try:
    mycursor.execute("Create table orders(order_Pending varchar(20),order_completed varchar(20))")
except Exception as e:
    print(e)

try:
    mycursor.execute("Create table details(Name varchar(20),Email_id varchar(20),password varchar(20),address varchar(20),contact_number varchar(20))")
except Exception as e:
    print(e)


class Cart_crude:

    def __init__(self) -> None:
        self.mysql = g.get_conn(name)
        self.mycur = self.mysql.cursor()

    def insert_value(self):
        while True:
            try:
                mod = input("enter model name :")
                col=input("Enter the colour")
                price=int(input("Enter price"))
                try:
                    sql = "insert into cart values ('{}', '{}',{})".format(mod ,col,price)
                    self.mycur.execute(sql)
                    if self.mycur.rowcount > 0:
                        self.mysql.commit()
                        print("Values have been inserted ")
                    else:
                        print("No value was inserted ")
                    self.mysql.rollback()
                except Exception as e:
                    print(e)
            except:
                print("Please retry to enter values ")
            ch = input("Do you wish to continue ?[y/n] ")
            if ch in ['y', 'Y']:
                continue
            else:
                print("Terminated")
                break

    def __Del__(self):
        try:
            deldet = input("enter the model name :")
            sql = "delete from Cart where Model_name = '{}'".format(deldet)
            self.mycur.execute(sql)
            if self.mycur.rowcount > 0:
                self.mysql.commit()
                print("Values have been deleted")
            else:
                print("No value was deleted ")
                self.mysql.rollback()
        except Exception as e:
            print(e)

    '''def update_details(self):
        try:
            e = input("Enter the model name :")
            e_d = input("Enter the status:")

            sql = "update Banking set password = '{}' where Email_id = '{}'".format(e_d, e)
            self.mycur.execute(sql)
            if self.mycur.rowcount > 0:
                self.mysql.commit()
                print("Values have been updated")
            else:
                print("No value was updated ")
                self.mysql.rollback()
        except Exception as e:
            print(e)'''

    def display(self):
        try:
            sql = "Select *from Cart"
            self.mycur.execute(sql)
            records = self.mycur.fetchall()
            for r in records:
                print(r)
        except Exception as e:
            print(e)
b=Cart_crude()
while True:
    print("Welcome to cart")
    print("\n1.Add \n2.delete \n3.display \n4.exit")
    ch=input("enter choice ")
    if ch=='1':
        b.insert_value()
        pass
    elif ch=='2':
        b.__Del__()
        pass
    elif ch=='3':
        b.display()
        pass
    elif ch=='4':
        print("Added to cart")
        break
    else:
        print("invalid option")

'''import get_conn as g

class details:
    def __init__(self) -> None:
        self.mysql = g.get_conn(name)
        self.mycur = self.mysql.cursor()
    def Insert_value(self):
        while True:
            try:
                name = input("enter the name :")
                e_id = input("Enter your Email_id :")
                pas = input("Enter your password")
                add = input("enter the address :")
                pan=int(input("enter the contact number"))
                try:
                    sql = "insert into details values ('{}', '{}','{}', '{}',{})".format(name,
                                                                                         e_id,
                                                                                         pas,
                                                                                         add,
                                                                                         pan)
                    self.mycur.execute(sql)
                    if self.mycur.rowcount > 0:
                        self.mysql.commit()
                        print("Values have been inserted ")
                    else:
                        print("No value was inserted ")
                        self.mysql.rollback()
                except Exception as e:
                    print(e)
            except:
                print("Please retry to enter values ")
            ch = input("Do you wish to continue ?[y/n] ")
            if ch in ['y', 'Y']:
                continue
            else:
                print("Terminated")
                break

    def __Del__(self):
        try:
            e_d = input("enter your Email_id :")
            pa = input("enter ur password")
            #sql = "delete from details where name = '{}'".format(deldet)
            sql = "delete from details where Email_id = '{}' and password = '{}'".format(e_d,pa)
            self.mycur.execute(sql)
            if self.mycur.rowcount > 0:
                self.mysql.commit()
                print("Values have been deleted")
            else:
                print("No value was deleted ")
                self.mysql.rollback()

        except Exception as e:
            print(e)

    def Update_details(self):
        try:
            e = input("Enter the Email Id :")
            pa = input("enter ur recent password")
            e_d = input("Enter the password which u want to reset:")

            sql = "update details set password = '{}' where Email_id = '{}' and password = '{}'".format(e_d,e,pa)
            self.mycur.execute(sql)
            if self.mycur.rowcount > 0:
                self.mysql.commit()
                print("Values have been updated")
            else:
                print("No value was updated ")
                self.mysql.rollback()
        except Exception as e:
            print(e)

    def Display(self):
        try:
            sql = "Select *from details"
            self.mycur.execute(sql)
            records = self.mycur.fetchall()
            for r in records:
                print(r)
        except Exception as e:
            print(e)

b = details()
while True:
    print("choose :")
    print("\n1.new acc \n2.delete acc\n3.view acc info \n4.update personal \n5.exit")
    ch = input("enter choice ")
    if ch == '1':
        b.Insert_value()
        pass
    elif ch == '2':
        b.__Del__()
        pass
    elif ch == '3':
        b.Display()
        pass
    elif ch == '4':
        b.Update_details()
        pass
    elif ch == '5':
        break
    else:
        print("invalid option")'''



