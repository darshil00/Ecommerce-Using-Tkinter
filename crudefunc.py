import get_conn as g
class details:

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


'''b = details()
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
