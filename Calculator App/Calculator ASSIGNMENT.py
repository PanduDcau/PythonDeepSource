from tkinter import*
from tkinter.ttk import*
from tkinter import messagebox
##Main Window
window = Tk()
window.geometry("300x200")
window.title("Your NAME")
window.resizable(False,False)
My_Index="INDEX"
My_Name="Type YOUR NAME"
##Introducing Frames
frame1=Frame(window)
frame1.pack()
frame2=Frame(window)
frame2.pack()
frame3=Frame(window)
frame3.pack()
frame4=Frame(window)
frame4.pack()
frame5=Frame(window)
frame5.pack()
frame6=Frame(window)
frame6.pack()
frame7=Frame(window)
frame7.pack()
frame8=Frame(window)
frame8.pack()
##Index number Appear @ 2nd frame


lb1=Label(frame1,font=("Lucida Console",10),width=40,background="cyan")
lb1.pack(side="left",fill='x')
def TopAppear(X):
    lb1.configure(text=My_Index)
def TopDisappear(X):
    lb1.configure(text="")


####User Inputs Display

Char_var=''

def btnClick(letter):
    Char_typed=txtDisplay.get()
    global Char_var
    Char_var = Char_typed+letter
    txtDisplay.insert(END,letter)

def reverseClick():
    Char_typed = txtDisplay.get()
    reversed_Typed=Char_typed[::-1]
    txtDisplay.delete(0,END)
    txtDisplay.insert(0,reversed_Typed)
def ResetDisplay(e):
    txtDisplay.delete(0, END)

text_Input=StringVar()
global txtDisplay

txtDisplay = Entry( frame2, width=46 , justify="right" )
txtDisplay.grid()

#######My Name Appear @ 7th frame

lb3=Label(frame7,font=("Lucida Console",10),foreground="yellow",background="white",width=40)
lb3.pack(side="left",fill='x')

def BottomAppear(X):
    lb3.configure(text=My_Name,background="black")
def BottomDisappear(X):
    lb3.configure(text="",background="white")





##Introducing Buttons
B1=Button(frame3,text="h",command=lambda:btnClick("h")).pack(side="left")
B2=Button(frame3,text="a",command=lambda:btnClick("a")).pack(side="left")
B3=Button(frame3,text="r",command=lambda:btnClick("r")).pack(side="left")
B4=Button(frame4,text="i",command=lambda:btnClick("i")).pack(side="left")
B5=Button(frame4,text="t",command=lambda:btnClick("t")).pack(side="left")
B6=Button(frame4,text="k",command=lambda:btnClick("k")).pack(side="left")
B7=Button(frame5,text="u",command=lambda:btnClick("u")).pack(side="left")
B8=Button(frame5,text="l",command=lambda:btnClick("l")).pack(side="left")
B9=Button(frame5,text="n",command=lambda:btnClick("n")).pack(side="left")
B10=Button(frame6,text="g",command=lambda:btnClick("g")).pack(side="left")
B11=Button(frame6,text="space",command=lambda:btnClick(" ")).pack(side="left")
B12=Button(frame6,text="reverse",command=lambda:reverseClick()).pack(side="left")



##Color Buuton Deffine


lb4=Label(frame8,text="Select the Display Color:",font=("Lucida Console",7),foreground="green",width=25)
lb4.grid(row=0,column=0)

def ColorRed(Red):
    txtDisplay['foreground']="red"
def ColorBlue(Blue):
    txtDisplay['foreground']="blue"
def ColorPink(Pink):
    txtDisplay['foreground']="pink"
def ColorGreen(Green):
    txtDisplay['foreground']="green"

##Color Selection


colorRed=Label(frame8,background='red',width=5)
colorRed.grid(row=0,column=1)
colorBlue=Label(frame8,background='blue',width=5)
colorBlue.grid(row=0,column=2)
colorPink=Label(frame8,background='pink',width=5)
colorPink.grid(row=0,column=3)
colorGreen=Label(frame8,background='green',width=5)
colorGreen.grid(row=0,column=4)


    
   

##Handling All the Events of Mouse

txtDisplay.bind("<Button-3>",ResetDisplay)
lb3.bind('<Enter>',BottomAppear)
lb3.bind('<Leave>',BottomDisappear)
lb1.bind('<Enter>',TopAppear)
lb1.bind('<Leave>',TopDisappear)
colorRed.bind('<Button-1>' ,ColorRed)
colorBlue.bind('<Button-1>' ,ColorBlue)
colorPink.bind('<Button-1>' ,ColorPink)
colorGreen.bind('<Button-1>' ,ColorGreen)
   





window.mainloop()
















































