from tkinter import *
window = Tk()

window.geometry("500x400+30+20")
window.title("Welcome to Python Programming")

#adding Button widget

btn = Button(window, text="Click to add name", fg="blue")
btn.place(x=80, y=100)

#adding Label widget

lbl1 = Label(window, text="Student Personal Information", fg="orange", bg="#4863A0",font=16)
lbl1.place(relx=.5,y=80,anchor='center')

lbl2 = Label(window, text="Gender", fg="white", bg="#728FCE")
lbl2.place(x=80,y=150)

lbl3 = Label(window, text="Sports", fg="white", bg="#728FCE")
lbl3.place(x=80,y=225)

lbl4 = Label(window, text="Subjects", fg="white", bg = "#728FCE")
lbl4.place(x=80,y=290)

#adding text field widget

txtfld = Entry(window, bd=3, font=("calibri",16))
txtfld.place(x=195, y=100)

#adding radio button

v1 = StringVar()
v2 = StringVar()
v1.set(1)
r1 = Radiobutton(window,text="Male",value=v1)
r1.place(x=80,y=180)

r2 = Radiobutton(window,text="Female", value=v2)
r2.place(x=150,y=180)


#adding check box

v3 = IntVar()
v4 = IntVar()
v5 = IntVar()
chkbox1 = Checkbutton(window,text="basketball", variable=v3)
chkbox2 = Checkbutton(window,text="tennis", variable=v4)
chkbox3 = Checkbutton(window,text="swimming", variable=v5)

chkbox1.place(x=80,y=250)
chkbox2.place(x=180,y=250)
chkbox3.place(x=280,y=250)

#adding listbox

var = StringVar()
var.set("arithmetic")
data1 = "arithmetic"
data2 = "reading"
data3 = "writing"
lstbox = Listbox(height=4,selectmode='multiple')
lstbox.insert(END,data1,data2,data3)
lstbox.place(x=80,y=320)

window.mainloop()