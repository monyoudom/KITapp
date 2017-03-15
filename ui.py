from tkinter import *
from tkintertable import TableCanvas, TableModel
from PIL import Image,ImageTk
import MySQLdb
import time
import tkMessageBox

def desigup():
    R.destroy()
    sigup()
def sigup():
   

    def Sigups():
        
        
        usernames = username.get()
        passwords = password.get()
        if usernames == None :
            print "Pleas fill all information"
            
        
        
        aa= MySQLdb.connect(host='127.0.0.1',port= 3306,user="root",passwd="010905885",db="kitpage")
        mm = aa.cursor()
        #mm.execute("CREATE TABLE IF NOT EXISTS singup ( username varchar(30) not null, passwords int(30), dp varchar(30), batch varchar(20))")
        #mm.execute("""INSERT INTO singup VALUES (%s,%s,%s,%s)""",(usernames,passwords,a,b))
       
        
        mm.execute("""INSERT INTO singup VALUES (%s,%s,%s,%s)""",(usernames,passwords,dps,batchs))
        aa.commit()
        
        tkMessageBox.showinfo("Welcome to %s" %usernames, "Let Login")
        

        
       
        
        
        
        
        
        deslogin()

        
       
        
    def dp(v1):
        global dps
        dps = v1
    def batch(v2):
        global batchs
        batchs = v2
        
        
    
    
    gw = '#134e86'
    g="#0a2845#"
    gg ="white"
    global R1
    R1 = Tk()

    R1.geometry('712x712')
    R1.title('SigUp Now')
    R1.resizable(width = FALSE ,height= FALSE)
    Image_open = Image.open("image/KITSigup.png")
    image = ImageTk.PhotoImage(Image_open)
    sigup = Label(R1,image=image,bg=gg)
    sigup.place(x=0,y=0,bordermode="outside")
    username=Entry(R1,width=20,font=("bold",15),highlightthickness=2,bg=gg,relief=SUNKEN)
    username.place(x=242,y= 190 )
    password=Entry(R1,width=20,show="*",font=("bold",15),highlightthickness=2,bg=gg,relief=SUNKEN)
    password.place(x=242,y=250 )
    options = ["SoftWare", "Toresem", "Actiture"]
    var = StringVar()
    var.set("Choice Here")
    dp = OptionMenu(R1, var, *options,command = dp)
    dp.config(width=20,font=("bold",10))
    dp.place(x=242, y=380)
    option1 = ["Batch_One", "Batch_Two", "Batch_Three","Batch_Four"]
    var2 = StringVar()
    var2.set("Choice Here")
    batch = OptionMenu(R1, var2, *option1,command = batch)
    batch.config(width=20,font=("bold",10))
    batch.place(x=242, y=310)
    loginbt = Button(R1,text = "Login",width=10,height=2,bg=g,fg="white",font="5",relief=RAISED,overrelief=RIDGE,command=deslogin)
    signUpbt = Button(R1,text = "SignUp",width=10,height=2,bg=g,fg="white",font="5",relief=RAISED,overrelief=RIDGE,command=Sigups)
    loginbt.place(x =225 ,y=500)
    signUpbt.place( x =400,y=500)
    
   
    R1.mainloop()


    
def login():
    def loginto():
        aa= MySQLdb.connect(host='127.0.0.1',port= 3306,user="root",passwd="010905885",db="kitpage")
        mm = aa.cursor()
        username = e1.get()
        password = e2.get()
        mm.execute('SELECT * FROM singup WHERE username = %s AND passwords = %s', (username, password))
        for i in username:
            print i
        if mm.fetchall():
            tkMessageBox.showinfo("Welcome to %s" %username, "Let GO")
            R.destroy()
            master = Tk()
            tframe = Frame(master)
            tframe.pack()
            table = TableCanvas(tframe)
            table.createTableFrame()

            model = TableModel()adf
            table = TableCanvas(tframe, model=model)


            master.mainloop()

            
            
        else:
            tkMessageBox.showinfo("Sorry" , "Wrong Password")
    gw = '#134e86'
    g="#0a2845#"
    gg ="white"
    global R
    
    R = Tk()
    

    R.geometry('720x720')
    R.title('Login')
    R.resizable(width = FALSE ,height= FALSE)
    Image_open = Image.open("image\KITpage.png")
    R.winfo_x()
    R.winfo_y()
    image = ImageTk.PhotoImage(Image_open)
    logo = Label(R,image=image,bg=gg)
    logo.place(x=0,y=0,bordermode="outside")
    e1=Entry(R,width=20,font=("bold",15),highlightthickness=2,bg=gg,relief=SUNKEN)
    e1.place(x=242,y=288 )
    e2=Entry(R,width=20,show="*",font=("bold",15),highlightthickness=2,bg=gg,relief=SUNKEN)
    e2.place(x=242,y=380 )
    loginbt = Button(R,text = "Login",width=10,height=2,bg=g,fg="white",font="5",relief=RAISED,overrelief=RIDGE,command = loginto)
    signUpbt = Button(R,text = "SignUp",width=10,height=2,bg=g,fg="white",font="5",relief=RAISED,overrelief=RIDGE,command=desigup)
    loginbt.place(x =225 ,y=500)
    
    signUpbt.place( x =400,y=500)
    R.mainloop()
def deslogin():
    R1.destroy()
    login()