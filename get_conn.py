import mysql.connector as my
def get_con():
    mysql = my.connect(host= 'localhost',
                       user= 'root',
                       passwd ='')
    return mysql


def get_conn(name):
    mysql = my.connect(host= 'localhost',
                       user= 'root',
                       passwd ='',
                       database =name)
    return mysql