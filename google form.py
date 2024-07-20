import mysql.connector as ts
import tkinter as st

data=ts.connect(host="localhost",port="3306",database="form",user="root",
                password="#290801")


def registration(event):
    fn=e.get()
    ln=e1.get()
    cn=e4.get()
    add=e3.get()
    g=s3.get()
    cur=data.cursor()
    q1="insert into registration values(%s,%s,%s,%s,%s)"
    val=(fn,ln,cn,add,g)
    cur.execute(q1,val)
    data.commit()
    







win=st.Tk()
win.geometry("600x600+200+10")
win.title("Registration Form")
win.config(bg="lawngreen")

l=st.Label(win,text="Registration Form",width="5",padx=20,pady=20,font=('bold',15)
           ,bg="lawngreen")
l.place(x=180,y=20,width=200)

a1=st.Label(win,text="First Name",bg="lawngreen",font=('bold',15))
a1.place(x=50,y=90)

e=st.Entry(win)
e.place(x=180,y=90,width=200)

b1=st.Label(win,text="Last Name",bg="lawngreen",font=('bold',15))
b1.place(x=50,y=150)

e1=st.Entry(win)
e1.place(x=180,y=150,width=200)

c1=st.Label(win,text="Email",bg="lawngreen",font=('bold',15))
c1.place(x=50,y=210)

e2=st.Entry(win)
e2.place(x=180,y=210,width=200)

d1=st.Label(win,text="Contact No",bg="lawngreen",font=('bold',15))
d1.place(x=50,y=210)

e4=st.Entry(win)
e4.place(x=180,y=210,width=200)


a3=st.Label(win,text="Address",bg="lawngreen",font=('bold',15))
a3.place(x=50,y=270)

e3=st.Entry(win)
e3.place(x=180,y=270,width=250)

s=st.Label(win,text="Gender",bg="lawngreen",font=('bold',15))
s.place(x=50,y=330)
s3=st.Entry(win)
s3.place(x=180,y=330,width=250)
'''s1=st.Radiobutton(win,text="Male",value=1,bg="lawngreen",font=('bold',12))
s2=st.Radiobutton(win,text="Female",value=2,bg="lawngreen",font=('bold',12))
s1.place(x=180,y=330)
s2.place(x=270,y=330)'''

b=st.Button(win,text="Submit",width=10,height="2",font=10,bg="red")
b.place(x=180,y=390)
b.bind("<Button>",registration)
