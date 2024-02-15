import random
import string
from tkinter import*
root=Tk()
root.geometry("440x500")
root.title("Password Generator")
root.configure(background="light cyan")
Title=Label(root,text="Password Generator",bg='light blue',fg='black',
            font=('Courier New',23,"bold"))
Title.pack(anchor='center',padx=10,pady=40)

length=Label(root,text="Enter the length of password :",bg='light cyan',font=('Courier New',16,"bold"))
length.pack(anchor='center',pady=10)

box1=Entry(root,width=20,font=('Courier New',20),borderwidth=5)
box1.pack(anchor='center',padx=20,pady=5)

def submit():
    try:
        plen=int(box1.get())
        alpha=string.ascii_letters
        num=string.digits
        special=string.punctuation
        pswdpool=list(alpha+num+special)
        out=("".join(random.sample(pswdpool,plen)))
        box2.delete(0,END)
        box2.insert(0,out)
    except:
        box2.insert(0,'Error')

def clear():
    box1.delete(0,END)
    box2.delete(0,END)
   
#submit button
sub=Button(root, text="Generate Password", font=('Courier New',14), pady=5, bg="yellow", command=submit)
sub.pack(anchor='center',pady=10)

result=Label(root,text="Password Generated is:",bg='light cyan',font=('Courier New',16,"bold"))
result.pack(anchor='center',pady=15)

box2=Entry(root,width=37,font=('Courier New',20),borderwidth=5)
box2.pack(anchor='center',padx=20,pady=5)

clr=Button(root, text="Clear All", font=('Courier New',14), pady=5, bg="light pink", command=clear)
clr.pack(anchor='center',pady=10)
root.mainloop()