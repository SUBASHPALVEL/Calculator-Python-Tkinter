"""

author SubashPalvel

"""

# 1 import statements

from tkinter import*

# 2 setting pysical properties of the calculator

me=Tk()
me.geometry("354x460")
me.title("CALCULATOR BY SUBASH")
melabel = Label(me,text="CALCULATOR BY SUBASH",bg='White',font=("Times",20,'bold'))
melabel.pack(side=TOP)
me.config(background='Dark gray')

textin=StringVar()
operator=""


# 3 defining functions

    # Displaying numbers in panel
def clickbut(number):   #lambda:clickbut(1)
     global operator
     operator=operator+str(number)
     textin.set(operator)

    # Addition
def equlbut():
     global operator
     add=str(eval(operator))
     textin.set(add)
     operator=''

     # Subtraction
def equlbut():
     global operator
     sub=str(eval(operator))
     textin.set(sub)
     operator=''   

     # Multiplication  
def equlbut():
     global operator
     mul=str(eval(operator))
     textin.set(mul)
     operator=''

     # Division
def equlbut():
     global operator
     div=str(eval(operator))
     textin.set(div)
     operator=''    

    # Clearing numbers in the panel
def clrbut():
     textin.set('')

# 4 Defining buttons

    # Display panel
metext=Entry(me,font=("Courier New",12,'bold'),textvar=textin,width=25,bd=5,bg='powder blue')
metext.pack()
    # Button 1
but1=Button(me,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(1),text="1",font=("Courier New",16,'bold'))
but1.place(x=10,y=100)
    # Button 2
but2=Button(me,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(2),text="2",font=("Courier New",16,'bold'))
but2.place(x=10,y=170)
    # Button 3
but3=Button(me,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(3),text="3",font=("Courier New",16,'bold'))
but3.place(x=10,y=240)
    # Button 4
but4=Button(me,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(4),text="4",font=("Courier New",16,'bold'))
but4.place(x=75,y=100)
    # Button 5
but5=Button(me,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(5),text="5",font=("Courier New",16,'bold'))
but5.place(x=75,y=170)
    # Button 6
but6=Button(me,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(6),text="6",font=("Courier New",16,'bold'))
but6.place(x=75,y=240)
    # Button 7
but7=Button(me,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(7),text="7",font=("Courier New",16,'bold'))
but7.place(x=140,y=100)
    # Button 8
but8=Button(me,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(8),text="8",font=("Courier New",16,'bold'))
but8.place(x=140,y=170)
    # Button 9
but9=Button(me,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(9),text="9",font=("Courier New",16,'bold'))
but9.place(x=140,y=240)
    # Button 0
but0=Button(me,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(0),text="0",font=("Courier New",16,'bold'))
but0.place(x=10,y=310)
    # Button .
butdot=Button(me,padx=47,pady=14,bd=4,bg='white',command=lambda:clickbut("."),text=".",font=("Courier New",16,'bold'))
butdot.place(x=75,y=310)
    # Button +
butpl=Button(me,padx=14,pady=14,bd=4,bg='white',text="+",command=lambda:clickbut("+"),font=("Courier New",16,'bold'))
butpl.place(x=205,y=100)
    # Button -
butsub=Button(me,padx=14,pady=14,bd=4,bg='white',text="-",command=lambda:clickbut("-"),font=("Courier New",16,'bold'))
butsub.place(x=205,y=170)
    # Button *
butml=Button(me,padx=14,pady=14,bd=4,bg='white',text="*",command=lambda:clickbut("*"),font=("Courier New",16,'bold'))
butml.place(x=205,y=240)
    # Button /
butdiv=Button(me,padx=14,pady=14,bd=4,bg='white',text="/",command=lambda:clickbut("/"),font=("Courier New",16,'bold'))
butdiv.place(x=205,y=310)
    # Button CE
butclear=Button(me,padx=14,pady=119,bd=4,bg='white',text="CE",command=clrbut,font=("Courier New",16,'bold'))
butclear.place(x=270,y=100)
    # Button =
butequal=Button(me,padx=151,pady=14,bd=4,bg='white',command=equlbut,text="=",font=("Courier New",16,'bold'))
butequal.place(x=10,y=380)

# 5 Running calculator continuously

me.mainloop()

