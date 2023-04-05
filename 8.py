from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
win=Tk()
win.attributes('-fullscreen', True)
win.title("Mobile Specs")

class Table:
    def init(self, a):
        global count_y
        count_y=0.05
        # code for creating table
        self.e = ttk.Label(a, font=("Arial", 14, 'bold'), text=lst[0][0], borderwidth=20, relief=GROOVE)
        self.e.place(relx=0.15, rely=0.05, relwidth=0.38,relheight=0.04)
        self.e = ttk.Label(a, font=("Arial", 14), text=lst[0][1], borderwidth=20, relief=GROOVE)
        self.e.place(relx=0.50, rely=0.05, relwidth=0.38,relheight=0.04)
        for i in range(1,total_rows):
            for j in range(total_columns):
                '''self.e = Entry(a, width=20, fg='blue',
                               font=('Arial', 16, 'bold'))'''
                if j==0:
                    self.e = ttk.Label(a, font=("Arial", 14, 'bold'), text=lst[i][j], borderwidth=20, relief=GROOVE)
                    self.e.place(relx=0.15, rely=count_y+0.04, relwidth=0.38, relheight=0.04)
                elif j==1:
                    self.e = ttk.Label(a, font=("Arial", 14), text=lst[i][j], borderwidth=20, relief=GROOVE)
                    self.e.place(relx=0.5, rely=count_y + 0.04, relwidth=0.38, relheight=0.04)
                    count_y+=0.04
                #self.e.insert(END, lst[i][j])
# take the data
lst = [('Brand','Oneplus'),
('Model',	'CE'),
('Dimensions (mm)'	,'160 x 74.2 x 8.7'),
('Weight (g)',	'192.00'),
('Battery capacity (mAh)',	'4500'),
('Fast charging'	,'Proprietary'),
('Colours	Winter Mist ',', Arctic Sky, Astral Black'),
       ('Screen size (inches)', '6.55'),
       ('Resolution', '1080x2400 pixels'),
       ('Processor', 'octa-core'),
       ('Processor make', 'Qualcomm Snapdragon 888'),
       ('RAM', '12GB'),
       ('Internal storage', '128GB'),
       ('Expandable storage', 'Yes'),
       ('Expandable storage type', 'microSD'),
('Rear camera',	'64-megapixel'),
('No. of Rear Cameras'	,'3'),
('Rear autofocus'	,'Yes'),
('Rear flash'	,'Yes'),
('Front camera',	'16-megapixel'),
('No. of Front Cameras'	,'1'),
('Pop-Up Camera',	'No')]
# find total number of rows and
# columns in list
total_rows = len(lst)
total_columns = len(lst[0])

# create root window
t = Table()

win.columnconfigure(0,weight=1)
win.columnconfigure(1,weight=1)
win.rowconfigure(0,weight=5)
win.rowconfigure(1,weight=2)

root=Frame(win,bg="black")
root.grid(row=0,column=0,sticky="nsew")
frame_bottom=Frame(win,bg="grey")
frame_bottom.grid(row=1,column=0,sticky="nsew")
frame_right=Frame(win,bg="yellow")
frame_right.grid(row=0,column=1,sticky="nsew",rowspan=2)

t.init(frame_right)

img_1 = ImageTk.PhotoImage( Image.open("Janna.png").resize((300, 500)))#width,height
img_2=ImageTk.PhotoImage(Image.open("Janna_2.png").resize((300, 500)))
img_3=ImageTk.PhotoImage(Image.open("Janna_3.png").resize((300, 500)))
img_4=ImageTk.PhotoImage(Image.open("Janna_4.png").resize((300, 500)))
img_5=ImageTk.PhotoImage(Image.open("Janna_5.png").resize((300, 500)))

image_list=[img_1,img_2,img_3,img_4,img_5]

staus=Label(root,text=f"Image 1 of {len(image_list)}",bd=1,relief=SUNKEN,anchor=E,font=('Arial',15))

my_label=Label(root,image=img_1)
my_label.place(relx=0.25,rely=0.008)
def add_Cart():
    pass

def forward(image_number):
    global my_label
    global button_forward
    global button_back
    my_label.place_forget()

    my_label=Label(root,image=image_list[image_number-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))
    if image_number==len(image_list):
        button_forward = Button(root, text=">>", state=DISABLED)
    my_label.place(relx=0.25,rely=0.012)
    button_back.place(relx=0.25, rely=0.942, relwidth=0.04, relheight=0.05)
    button_forward.place(relx=0.655, rely=0.942, relwidth=0.04, relheight=0.05)

    staus=Label(root, text=f"Image {image_number} of {len(image_list)}", bd=1, relief=SUNKEN, anchor=E,font=('Arial',15))
    staus.place(relx=0.29,rely=0.942,relwidth=0.365,relheight=0.05)

def back(image_number):
    global my_label
    global button_forward
    global button_back
    my_label.place_forget()

    my_label = Label(image=image_list[image_number - 1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))

    if image_number==1:
        button_back = Button(root, text="<<", state=DISABLED)

    my_label.place(relx=0.125,rely=0.01)
    button_back.place(relx=0.25, rely=0.94, relwidth=0.04, relheight=0.05)
    button_forward.place(relx=0.655, rely=0.94, relwidth=0.04, relheight=0.05)

    staus = Label(root, text=f"Image {image_number} of {len(image_list)}", bd=1, relief=SUNKEN, anchor=E,font=('Arial', 15))
    staus.place(relx=0.29, rely=0.94, relwidth=0.365, relheight=0.05)


button_back=Button(root,text="<<",command=back,state=DISABLED)
button_forward=Button(root,text=">>",command=lambda: forward(2))
button_back.place(relx=0.25, rely=0.94, relwidth=0.04, relheight=0.05)
button_forward.place(relx=0.655, rely=0.94, relwidth=0.04, relheight=0.05)

staus.place(relx=0.29, rely=0.94, relwidth=0.365, relheight=0.05)

img_cart=ImageTk.PhotoImage(Image.open("add_cart.png").resize((100,100)))
button_cart=Button(frame_bottom,text="Add to Cart!",command=lambda:add_Cart(),image=img_cart)
button_cart.place(relx=0.65,rely=0.3)

img_menu=ImageTk.PhotoImage(Image.open("main_menu.png").resize((100,100)))
button_cart=Button(frame_bottom,text="Add to Cart!",command=win.quit,image=img_menu)
button_cart.place(relx=0.2,rely=0.3)

win.mainloop()