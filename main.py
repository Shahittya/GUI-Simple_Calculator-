#a simple calculator using python (GUI)
from tkinter import *
#defining the event handler
def add():
    x=int(Entry_one.get())
    y=int(Entry_two.get())
    result['text']=x+y
def sub():
    x=int(Entry_one.get())
    y=int(Entry_two.get())
    result['text']=x-y
def mul():
    x=int(Entry_one.get())
    y=int(Entry_two.get())
    result['text']=x*y
def div():
    x=int(Entry_one.get())
    y=int(Entry_two.get())
    result['text']=x/y
root=Tk()
root.title("A Simple Calculator")
#setting the input fields
Num_one=Label(root,text="Enter the very first integer:",font=('Serif',20))
Entry_one=Entry(root)
Num_two=Label(root,text="Enter the second integer:",font=('Serif',20))
Entry_two=Entry(root)
result=Label(root,text="The output appears here! ",font=('Serif',20))

#setting the button
add=Button(root,text="Addition",width=12,command=add,bg='grey',fg='blue')
sub=Button(root,text="Subtraction",width=12,command=sub,bg='grey',fg='blue')
mul=Button(root,text="Multipicaon",width=12,command=mul,bg='grey',fg='blue')
div=Button(root,text="Addition",width=12,command=div,bg='grey',fg='blue')

#griding the button
Num_one.grid(row=0,column=0)
Entry_one.grid(row=0,column=1)
Num_two.grid(row=1,column=0)
Entry_two.grid(row=1,column=1)
add.grid(row=2,column=0)
sub.grid(row=2,column=1)
mul.grid(row=3,column=0)
div.grid(row=3,column=1)
result.grid(row=5,column=0)

#the mainloop
root.mainloop()
