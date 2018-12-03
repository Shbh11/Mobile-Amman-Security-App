import sys
import tkinter
from tkinter import messagebox
import pickle
import datetime
import os

def intro():
    messagebox.showinfo(title="Message",message="Mobile Amman App by DESC \nThis is a mobile security application that can monitor your phone for cyber threats and take action in the unlikely event of any cyber attack.\n")#introbox


def enterusernameandpassword():
    messagebox.showinfo(title="Message",message="PLEASE ENTER USERNAME AND PASSWORD.")#message to enter username and password
def enterpassword():
    messagebox.showinfo(title="Message",message="PLEASE ENTER YOUR PASSWORD.")#message to enter password
def enterusername():
    messagebox.showinfo(title="Message",message="PLEASE ENTER YOUR USERNAME .")#message to enter password
def incusernamepass():
    messagebox.showerror(title="Message",message="ENTERED USERNAME OR PASSWORD OR BOTH ARE INCORRECT.PLEASE TRY AGAIN")
def access():
    messagebox.showerror(title="Message",message="ACCESS DENIED.PLEASE TRY AGAIN.")
def notavail():
    messagebox.showinfo(title="Message",message="USERNAME NOT AVAILABLE.PLEASE CREATE A DIFFERENT USERNAME.")
def success():
    messagebox.showinfo(title="Message",message="YOU HAVE SUCCESSFULLY CREATED YOUR ACCOUNT.")
def usernamespecs():
    messagebox.showinfo(title="Message",message="YOUR USERNAME SHOULD BE ATLEAST 3 CHARACTERS LONG WITH A MINIMUM OF 3 LETTERS.")
def passwordlength():
    messagebox.showinfo(title="Message",message="YOUR PASSWORD SHOULD BE ATLEAST SIX CHARACTERS LONG.")
def passwordspec1():
    messagebox.showinfo(title="Message",message="YOUR PASSWORD SHOULD BE ATLEAST 6 CHARACTERS LONG.")
def passwordspec2():
    messagebox.showinfo(title="Message",message="YOUR PASSWORD SHOULD HAVE ATLEAST 2 NUMBERIC DIGITS AND ONE UPPERCASE LETTER.")
def passwordspec3():
    messagebox.showinfo(title="Message",message="YOUR PASSWORD CANNOT EXCEED MORE THAN 12 CHARACTERS.")
def usernamespec1():
    messagebox.showinfo(title="Message",message="YOUR USERNAME CANNOT EXCEED MORE THAN 12 CHARACTERS.")
def resentry():
    messagebox.showinfo(title="Message",message="PLEASE FILL THE THREE ENTRY FIELDS WITHOUT SPACES.")

def logout():#homepage frameglobal root2;global root1
    root2.destroy()
    login()

    
def action1():#homepage
    global root2
    takeAction1=tkinter.Label(root2,text="It is recommnded to uninstall the suspected app(s) :",bg="light green",fg="dark blue",font=('arial',14,'underline italic')).place(x=250,y=180)
    
def action2():#homepage
    global root2
    takeAction2=tkinter.Label(root2,text="It is recommnded to uninstall the suspected app(s):",bg="light green",fg="dark blue",font=('arial',14,'underline italic')).place(x=250,y=316)


def action3():#homepage
    global root2
    takeAction2=tkinter.Label(root2,text="If you find this suspicious , Log in to the DESC portal\nand block your number",bg="light green",fg="dark blue",font=('arial',14,'underline italic')).place(x=250,y=416)

def alertlist():#homepage
    global var
    global root2
    root2.destroy()#
    homepage(3)#
    
def tiplist():
    global root2
    root2.destroy()
    homepage(2)
    
def cat11():#homepage
    global root2
    alertlist()

def cat22():
    global root2
    tiplist()
    

def homepage(x=1,y="a"):
    global root1;global ment3;global root2;global ment5;global ment6;global ment7;global h
    root2=tkinter.Tk()
    root2.title("WELCOME"+" "+ment1.get())
    root2.geometry("900x550+195+20")
    root2.config(bg="black",bd=20,relief='sunken')
    root2.resizable(width=False,height=False)
    photo = tkinter.PhotoImage(file="logo.gif")
    label = tkinter.Label(image=photo)
    label.image = photo # reference for logo
    label.grid(row=0,column=0)
    star_label=tkinter.Label(text="*******************************************************************************************************",fg="white",bg="black").place(x=300,y=90)
    cat1=tkinter.Button(text="Alerts",command=cat11,width=12,relief="raised",bd=8,bg="dark green",fg="white",font=("copperlate",20,'bold italic underline')).place(x=5,y=280)
    cat2=tkinter.Button(text="Tip",command=cat22,width=12,relief="raised",bd=8,bg="dark green",fg="white",font=("copperlate",20,'bold italic underline')).place(x=5,y=360)
    logout1=tkinter.Button(text="Sign Out",command=logout,width=10,bg="light blue",fg="dark blue",font=('arial',16,' italic')).place(x=680,y=27)
    if x==2:
        y
        hname=tkinter.Label(text=y,bg="black",fg="turquoise",font=('arial',25,'bold underline italic')).place(x=430,y=200)
        seat_l=tkinter.Label(text="TIP1: Avoid installing third party apps\n\nTIP2: Avoid opening a mails/spam/sms from unknown sources\n\nTIP3:Never connect to unknown wifi hotspots\n\nTip4:Use a biometric identification for your phone",bg="black",fg="white",font=('arial',15,'bold italic')).place(x=235,y=210)
        
        
    if x==3:
        y
        button1 = tkinter.Button(root2, text="Take Action", command=action1,bg="dark green",fg="white")
        button1.place(x=730,y=177)
        button2 = tkinter.Button(root2, text="Take Action", command=action2,bg="dark green",fg="white")
        button2.place(x=730,y=304)
        button3 = tkinter.Button(root2, text="Take Action", command=action3,bg="dark green",fg="white")
        button3.place(x=730,y=420)
        alert1=tkinter.Label(root2,text="Alert1:Your Battery Consumpttion has been abnormally high for the past 2 days\n Suspected App:ABC",bg="red",fg="white",font=('arial',12,'underline italic')).place(x=240,y=116)
        alert2=tkinter.Label(root2,text="Alert2:Your Data/Wifi Usage for an app(s) is abnormally high\n Suspected App:XYZ ",bg="red",fg="white",font=('arial',12,'underline italic')).place(x=240,y=260)
        alert3=tkinter.Label(root2,text="Alert3:Your prepaid balance has reduced drastically ",bg="red",fg="white",font=('arial',12,'underline italic')).place(x=240,y=380)

    root2.mainloop()
    
def admincode():
    global root;global root1
    authcode=raw_input("Enter authorization code")
    if authcode=="8888":
        welcomeadmin()
    else:
        print ("Access denied due to incorrect code")
        root1.destroy()
        welcome()

def USERNAMEpasswordspecs(x,y):#registration
    m="usermembers.txt"
    i=0
    j=0
    k=0
    l=0
    if len(y)>12:
        usernamespec1()
    if len(y)>=3 and len(y)<=12:
        if y.isspace()=="True":
            usernamespecs()
        else:
            for q in y:
                if q.isalpha():
                    l=l+1
            if l>=3:
                if len(x)>12:
                    passwordspec3()
                if len(x)>=6 and len(x)<=12:
                    for g in x:
                        if g.isupper():
                            i=i+1
                        if g.isdigit():
                            j=j+1
                    if i>=1 and j>=2:
                        k=1
                    else:
                        k=0
                    if k==1:
                        search(m,ment3.get(),ment4.get(),root3)
                    if k==0:
                        passwordspec2()
                if len(x)<6:
                    passwordspec1()
            else:
                usernamespecs()
                
    if len(y)<3:
        usernamespecs()
                
def regfinish1():#registration
    global root3;global ment3;global ment4
    if ment3.get()=="" and ment4.get()=="" :
        enterusernameandpassword()
    elif ment3.get()=="" and ment4.get()!="" :
        enterusername()
    elif ment3.get()!="" and ment4.get()=="" :
        enterpassword()
    else:
        USERNAMEpasswordspecs(ment4.get(),ment3.get())
        
def append(x,a,b,root):#registration
    f=open(x,"a")
    f.write(a)
    f.write("\n")
    f.write(b)
    f.write("\n")
    f.close()

def search(x,a,b,root):#registration
    global root3
    f=open(x,"r")
    l=f.readlines()
    if a=="ADMIN":
        notavail()
    elif (a+'\n') not in l:
        global ment3
        append(x,a,b,root)
        regfinish(root3)
    else:
        notavail()
        
def regfinish(root):#registration
    success()
    root.destroy()
    welcome()

def back():#register frame
    global root3;global root1
    root3.destroy()
    login()
            
def register():
    global root1;global ment3;global ment4;global root3;
    root1.destroy()
    root3=tkinter.Tk()
    root3.title("Registration")
    root3.config(bg="black",bd=20,relief='flat')
    root3.resizable(width=False,height=False)
    root3.geometry("700x450+280+200")
    register_button=tkinter.Button(text="REGISTER",command=regfinish1,width=21,bg="black",fg="white",font=('copperlate',20,' italic')).place(x=155,y=297)
    ment3=tkinter.StringVar()
    ment4=tkinter.StringVar()
    entry_createusername=tkinter.Entry(root3,textvariable=ment3,width=40).place(x=290,y=120)
    entry_createpassword=tkinter.Entry(root3,show="*",textvariable=ment4,width=40).place(x=290,y=180)
    entry_createpin=tkinter.Entry(root3,show="#",width=40).place(x=290,y=240)
    
    cuser=tkinter.Label(root3,text="Create your username :",bg="black",fg="white",font=('times',14,'underline italic')).place(x=80,y=116)
    cpass=tkinter.Label(root3,text="Create your password :",bg="black",fg="white",font=('times',14,'underline italic')).place(x=80,y=176)
    cpin=tkinter.Label(root3,text="Create your 9 digit pin  :",bg="black",fg="white",font=('times',14,'underline italic')).place(x=80,y=236)
    acc=tkinter.Label(root3,text="CREATE YOUR ACCOUNT",bg="black",fg="light blue",relief="raised",font=('copperlate',30,'underline italic')).pack()
    back_button=tkinter.Button(text="BACK",command=back,width=8,bg="red",font=('copperlate',8,'underline italic')).place(x=15,y=350)
    root3.mainloop()

def homepagepath():#login 
    global root1
    root1.destroy()
    homepage()

def loginhomepage():#login
    global ment1;global ment2;global root1;global root2; global cuser
    cp=0;mp=0
    if ment1.get()=="" and ment2.get()=="":
        enterusernameandpassword()
    if ment1.get()=="" and ment2.get()!="":
        enterusername()
    if ment1.get()!="" and ment2.get()=="":
        enterpassword()
    if ment1.get()!="" and ment2.get()!="":
        f=open("usermembers.txt","r")
        l=f.readlines()
        if (ment1.get()+'\n') not in l:
            if ment1.get()=="ADMIN" and ment2.get()=="12345":
                admincode()
                cp=2
            else:
                cp=3
                
        if (ment1.get()+'\n')  in l:
            for i in range(len(l)):
                if l[i]==(ment1.get()+'\n'):
                    if l[i+1]==(ment2.get()+'\n'):
                        cuser=ment1.get()
                        cp=1
                        break
                    else:
                      pass
        if cp==1:
            homepagepath()
        if cp==0 or cp==3:
            incusernamepass()
        f.close()
 

def login():
    global root;global ment1;global ment2;global root1
    root1=tkinter.Tk()
    root1.title("LOGIN")
    root1.geometry("800x570+195+20")
    root1.config(bg="black",bd=20,relief='sunken')
    root1.resizable(width=False,height=False)
    label=tkinter.Label(root1,text="LOGIN",bg="black",fg="white",font=('copperlate',37,' underline bold italic')).place(x=288,y=7)
    logo_image=tkinter.PhotoImage(file="logo.gif")#logo image
    logo_label = tkinter.Label(image=logo_image,width=225,height=225)
    logo_label.place(x=252,y=80)
    ment1=tkinter.StringVar()
    ment2=tkinter.StringVar()
    entry_username=tkinter.Entry(root1,textvariable=ment1,width=25).place(x=340,y=330)#username
    entry_password=tkinter.Entry(root1,textvariable=ment2,show="*",width=25).place(x=340,y=355)#password
    username_label=tkinter.Label(root1,text="USERNAME",bg="black",fg="white",font=('times',15)).place(x=225,y=326)
    password_label=tkinter.Label(root1,text="PASSWORD",bg="black",fg="white",font=('times',15)).place(x=225,y=350)
    login_button=tkinter.Button(text="LOGIN",command=loginhomepage,width=18,font=('copperlate',15,'bold italic'),bg="red",fg="black").place(x=255,y=400)
    or_label=tkinter.Label(root1,text="OR",bg="black",fg="white",font=('copperlate',15,'italic')).place(x=348,y=441)
    register_button=tkinter.Button(text="REGISTER",command=register,width=18,font=('copperlate',15,'bold italic'),bg="red",fg="black").place(x=255,y=475)
    root1.mainloop()


def loginscreen():#welcome frame
    global root
    root.destroy()
    login()
    
#Welcome frame
def welcome():
    global root
    root=tkinter.Tk()
    root.title("Security APPLICATION")
    root.geometry("700x500+195+20")
    root.config(bg="black",bd=20,relief='sunken')
    root.resizable(width=False,height=False)#Lock window GUI
    label=tkinter.Label(root,text="WELCOME",bg="black",fg="white",font=('copperlate',37,' bold italic')).place(x=190,y=25)
    logo = tkinter.PhotoImage(file="logo.gif")
    tkinter.Button(root,image=logo,command=intro).place(x=210,y=100)#logo
    Next=tkinter.Button(text="NEXT",command=loginscreen,bd=8,relief=tkinter.RAISED,width=13,bg="black",fg="white",font=('copperlate',18,' bold italic')).place(x=217,y=360)
    root.mainloop()
welcome()






