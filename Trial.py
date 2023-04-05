from tkinter import *
from tkinter import ttk
class Table:
    def _init_(self, a):
        global count_y
        count_y=0
        # code for creating table
        self.e = ttk.Label(a, font=("Arial", 13, 'bold'), text=lst[0][0], borderwidth=20, relief=GROOVE)
        self.e.place(relx=0, rely=0, relwidth=0.2,relheight=0.04)
        self.e = ttk.Label(a, font=("Arial", 13), text=lst[0][1], borderwidth=20, relief=GROOVE)
        self.e.place(relx=0.17, rely=0, relwidth=0.23,relheight=0.04)
        for i in range(1,total_rows):
            for j in range(total_columns):
                '''self.e = Entry(a, width=20, fg='blue',
                               font=('Arial', 16, 'bold'))'''
                if j==0:
                    self.e = ttk.Label(a, font=("Arial", 13, 'bold'), text=lst[i][j], borderwidth=20, relief=GROOVE)
                    self.e.place(relx=0, rely=count_y+0.04, relwidth=0.2, relheight=0.04)
                elif j==1:
                    self.e = ttk.Label(a, font=("Arial", 13), text=lst[i][j], borderwidth=20, relief=GROOVE)
                    self.e.place(relx=0.17, rely=count_y + 0.04, relwidth=0.23, relheight=0.04)
                    count_y+=0.04
                #self.e.insert(END, lst[i][j])
# take the data
lst = [('Brand','Oppo'),
('Model',	'A74'),
('Dimensions (mm)'	,'160.30 x 73.80 x 7.95'),
('Weight (g)',	'175.00'),
('Battery capacity (mAh)',	'5000'),
('Fast charging'	,'Proprietary'),
('Colours	Midnight ',' Blue, Prism Black'),
       ('Screen size (inches)', '6.43'),
       ('Resolution', '1080x2400 pixels'),
       ('Processor', 'octa-core'),
       ('Processor make', 'Qualcomm Snapdragon 662'),
       ('RAM', '6GB'),
       ('Internal storage', '128GB'),
       ('Expandable storage', 'Yes'),
       ('Expandable storage type', 'microSD'),
('Rear camera',	'48-megapixel'),
('No. of Rear Cameras'	,'3'),
('Rear autofocus'	,'Yes'),
('Rear flash'	,'Yes'),
('Front camera',	'16-megapixel'),
('No. of Front Cameras'	,'1'),
('Pop-Up Camera',	'No')]

print(lst[0][0])
# find total number of rows and
# columns in list
total_rows = len(lst)
total_columns = len(lst[0])

# create root window

root = Tk()
root.attributes('-fullscreen', True)
t = Table()
t._init_(root)
root.mainloop()