import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image,ImageTk
from colorthief import ColorThief
import os

root = Tk()
root.title("Color Identifier")
root.geometry("800x470+300+100")
root.configure(bg= "dodger blue")
root.resizable(False,False)

def showimage():
    global filename
    filename = filedialog.askopenfilename(initialdir = os.getcwd(),title = "Select Image File",filetype = (("PNG file","*.png"),
                                                                                                           ("JPG file","*.jpg"),
                                                                                                           ("All file","*.txt")))
    img = Image.open(filename)
    img = ImageTk.PhotoImage(img)
    lb1.configure(image=img,width=310,height=270)
    lb1.image = img

def Findcolor():
    ct = ColorThief(filename)
    palette = ct.get_palette(color_count = 11)

    rgb1 = palette[0]
    rgb2 = palette[1]
    rgb3 = palette[2]
    rgb4 = palette[3]
    rgb5 = palette[4]
    rgb6 = palette[5]
    rgb7 = palette[6]
    rgb8 = palette[7]
    rgb9 = palette[8]
    rgb10 = palette[9]

   

    color1 = f"#{rgb1[0]:02x}{rgb1[1]:02x}{rgb1[2]:02x}"
    color2 = f"#{rgb2[0]:02x}{rgb2[1]:02x}{rgb2[2]:02x}"
    color3 = f"#{rgb3[0]:02x}{rgb3[1]:02x}{rgb3[2]:02x}"
    color4 = f"#{rgb4[0]:02x}{rgb4[1]:02x}{rgb4[2]:02x}"
    color5 = f"#{rgb5[0]:02x}{rgb5[1]:02x}{rgb5[2]:02x}"
    color6 = f"#{rgb6[0]:02x}{rgb6[1]:02x}{rgb6[2]:02x}"
    color7 = f"#{rgb7[0]:02x}{rgb7[1]:02x}{rgb7[2]:02x}"
    color8 = f"#{rgb8[0]:02x}{rgb8[1]:02x}{rgb8[2]:02x}"
    color9 = f"#{rgb9[0]:02x}{rgb9[1]:02x}{rgb9[2]:02x}"
    color10 = f"#{rgb10[0]:02x}{rgb10[1]:02x}{rgb10[2]:02x}"


    colors.itemconfig(id1,fill=color1)
    colors.itemconfig(id2,fill=color2)
    colors.itemconfig(id3,fill=color3)
    colors.itemconfig(id4,fill=color4)
    colors.itemconfig(id5,fill=color5)
    
    colors2.itemconfig(id11,fill=color6)
    colors2.itemconfig(id21,fill=color7)
    colors2.itemconfig(id31,fill=color8)
    colors2.itemconfig(id41,fill=color9)
    colors2.itemconfig(id51,fill=color10)

    hex1.config(text=color1)
    hex2.config(text=color2)
    hex3.config(text=color3)
    hex4.config(text=color4)
    hex5.config(text=color5)
    
    hex11.config(text=color6)
    hex21.config(text=color7)
    hex31.config(text=color8)
    hex41.config(text=color9)
    hex51.config(text=color10)
    



#icon
image_icon = PhotoImage(file = "D:/color_identifier_image/drive-download-20250311T145507Z-001/icon.png")
root.iconphoto(False,image_icon)

Label(root,width=120,height=15,bg="brown1").pack()

#frame
frame = Frame(root,width=700,height=370,bg="#fff")
frame.place(x=50,y=50)

logo=PhotoImage(file = "D:/color_identifier_image/drive-download-20250311T145507Z-001/logo.png")
Label(frame,image=logo,bg="#fff").place(x=10,y=10)
Label(frame,text = "Color Identifier",font = "century 23 bold",bg = "white").place(x=97,y=22)

#color_1
colors = Canvas(frame,bg="#fff",width=150,height=265,bd=0,highlightbackground="brown4")
colors.place(x=20,y=90)

id1 = colors.create_rectangle((10,10,50,50),fill="#b8255f")
id2 = colors.create_rectangle((10,50,50,100),fill="#db4035")
id3 = colors.create_rectangle((10,100,50,150),fill="#ff9933")
id4 = colors.create_rectangle((10,150,50,200),fill="#fad000")
id5 = colors.create_rectangle((10,200,50,250),fill="#afb83b")


hex1=Label(colors,text="#b8255f",fg="#000",font="arial 12 bold",bg="white")
hex1.place(x=60,y=15)

hex2=Label(colors,text="#db4035",fg="#000",font="arial 12 bold",bg="white")
hex2.place(x=60,y=65)

hex3=Label(colors,text="#ff9933",fg="#000",font="arial 12 bold",bg="white")
hex3.place(x=60,y=115)

hex4=Label(colors,text="#fad000",fg="#000",font="arial 12 bold",bg="white")
hex4.place(x=60,y=165)

hex5=Label(colors,text="#afb83b",fg="#000",font="arial 12 bold",bg="white")
hex5.place(x=60,y=215)


#color_2
colors2 = Canvas(frame,bg="#fff",width=150,height=265,bd=0,highlightbackground="brown4")
colors2.place(x=180,y=90)

id11 = colors2.create_rectangle((10,10,50,50),fill="#7ecc49")
id21 = colors2.create_rectangle((10,50,50,100),fill="#299438")
id31 = colors2.create_rectangle((10,100,50,150),fill="#6accbc")
id41 = colors2.create_rectangle((10,150,50,200),fill="#158fad")
id51 = colors2.create_rectangle((10,200,50,250),fill="#14aaf5")


hex11=Label(colors2,text="#7ecc49",fg="#000",font="arial 12 bold",bg="white")
hex11.place(x=60,y=15)

hex21=Label(colors2,text="#299438",fg="#000",font="arial 12 bold",bg="white")
hex21.place(x=60,y=65)

hex31=Label(colors2,text="#6accbc",fg="#000",font="arial 12 bold",bg="white")
hex31.place(x=60,y=115)

hex41=Label(colors2,text="##158fad",fg="#000",font="arial 12 bold",bg="white")
hex41.place(x=60,y=165)

hex51=Label(colors2,text="#14aaf5",fg="#000",font="arial 12 bold",bg="white")
hex51.place(x=60,y=215)

#select_image
selectimage = Frame(frame,width=340,height=350,bg="thistle4")
selectimage.place(x=350,y=10)

f = Frame(selectimage,bd=3,bg="black",width=320,height=280,relief=GROOVE)
f.place(x=10,y=10)

lb1 = Label(f,bg="black")
lb1.place(x=0,y=0)

Button(selectimage,text="Select Image",bg="dodger blue",width=12,height=1,font="arial 14 bold",command = showimage).place(x=10,y=300)
Button(selectimage,text="Find Colors",bg="brown2",width=12,height=1,font="arial 14 bold",command = Findcolor).place(x=176,y=300)





root.mainloop()
