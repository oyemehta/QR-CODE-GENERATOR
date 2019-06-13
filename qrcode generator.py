from tkinter import *
from tkinter import filedialog
import tkinter.messagebox

import pyqrcode

windows=Tk()
windows.title('QR CODE GENERATOR')
windows.configure(background='snow')
windows.geometry('1280x720')

def clear():
    entry1.delete(first=0,last=100)


def about_us():
    tkinter.messagebox.showinfo('DEVELOPER', 'This is a music player build using Python Tkinter by @YASH MEHTA')

def select_folder():
    global filename
    global folder_path
    filename=filedialog.askdirectory()
    folder_path.set(filename)

def get_QR():
    URL=entry1.get()
    PATH=entry2.get()
    ur = pyqrcode.create(URL)
    ur.png('abc.png')
    import os

    os.system('abc.png')
    print('your QR code created')

folder_path = StringVar()

lbl1=Label(windows,text='QR CODE GENERATOR', width='25',fg='snow',bg='black',font=('times',25,'bold'))
lbl1.place(x=400,y=80)
lbl2=Label(windows,text='LINK', width='15',fg='black',bg='orange',font=('times',15,'bold'))
lbl2.place(x=100,y=200)
lbl3=Label(windows,text='Select PATH', width='15',fg='black',bg='orange',font=('times',15,'bold'))
lbl3.place(x=100,y=300)


entry1=Entry(windows,width='50',fg='black',bg='papaya whip',font=('times',15,'italic'))
entry1.place(x=400,y=200)
entry2=Entry(windows,width='50',textvariable = folder_path,fg='black',bg='papaya whip',font=('times',15,'italic'))
entry2.place(x=400,y=300)

btn1=Button(windows,text='Clear',command=clear,width='15',fg='black',bg='sky blue',activebackground='snow')
btn1.place(x=1000,y=200)
btn3=Button(windows,text='Browse',width='15',fg='black',bg='sky blue',command = select_folder,activebackground='snow')
btn3.place(x=1000,y=300)
btn2=Button(windows,text='CREATE QR CODE',width='25',fg='black',bg='sky blue',activebackground='snow',command  = get_QR)
btn2.place(x=550,y=450)
btn5=Button(windows,text='ABOUT US',width='25',fg='black',bg='sky blue',activebackground='snow',command  =about_us)
btn5.place(x=0,y=0)


windows.mainloop()