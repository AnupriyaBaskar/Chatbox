from tkinter import *
from tkinter.font import Font
import pymysql
from tkinter import messagebox
c=Tk()
c.title("E COZY")
c.geometry("940x1000")
c.iconbitmap("favicon.ico")
#<----image--->
img=PhotoImage(file="sample3.png")
l=Label(image=img)
l.pack(fill="both")


def menubar():
    M=Toplevel(c)
    M.title("MENU BAR")
    M.geometry("900x80")
    ml=Label(M,bg="#3b3a3a",fg="#ff5757",relief="flat",width=40,height=20)
    ml.pack(fill="both")
    ml2=Button(M,text="MENU",bg="#3b3a3a",fg="#ff5757",relief="flat",font=("times",20,"bold"))
    ml2.place(x=50,y=18)

    def aboutus():
        s1=Toplevel(M)
        s1.geometry("1000x1000")
        s1.title("aboutus")
        img1=PhotoImage(file="2.png")
        l1=Label(s1,image=img1)
        l1.pack(fill="both")
        s1.resizable(height="false",width="false")
        s1.mainloop()
    ml3=Button(M,text="ABOUT US",bg="#3b3a3a",fg="white",relief="flat",font=("times",14,"bold"),command=aboutus)
    ml3.place(x=200,y=25)

    

    def services():
        s=Toplevel(M)
        s.geometry("900x900")
        s.title("services")
        s.config(bg="#3b3a3a")
        
        fs=Frame(s,width=300,height=200)
        fs.place(x=500,y=20)
        fs3=Frame(s,width=600,height=200)
        fs3.place(x=40,y=20)
        fsi=PhotoImage(file="fgrs.png")
        LF=Label(fs3,image=fsi)
        LF.pack()
        fs1=Frame(s,width=600,height=300)
        fs1.place(x=40,y=260)
        fsi2=PhotoImage(file="hh (2).png")
        LF2=Label(fs1,image=fsi2)
        LF2.pack()
        fs2=Frame(s,width=600,height=200)
        fs2.place(x=40,y=500)
        fsi3=PhotoImage(file="hh (1).png")
        LF3=Label(fs2,image=fsi3)
        LF3.pack()
        

        myfontc=Font(family="times",size=20,weight="bold",slant="italic")
        myfontd=Font(family="times",size=10,weight="bold",slant="italic")
        myfonte=Font(family="times",size=15,weight="bold",slant="roman")
        c=PhotoImage(file="comment2.png")
        cl=Label(fs,image=c)
        cl.pack(fill="both",side="right")
        c2=Label(s,text="COMMENT SECTION",bg="#3b3a3a",fg="#ff5757",font=myfontc)
        c2.place(x=460,y=100)
        c3=Label(s,text="(GIVE US YOUR FEEDBACK BELOW)",bg="#3b3a3a",fg="white",font=myfontd)
        c3.place(x=500,y=130)
        fs4=Frame(s,width=600,height=500)
        fs4.place(x=500,y=300)
        fsi4=PhotoImage(file="main.png")
        LF4=Label(fs4,image=fsi4)
        LF4.pack()

        def save():
            if (comment.get()==""):
              messagebox.showinfo("Insert status","enter some feedback")

            else:    
                con=pymysql.connect(host="localhost",user="root",passwd="anupriya17",port=3308,database='comment')
                cursor=con.cursor()
                cursor.execute("insert into commentdata values('comment')")
                cursor.execute("commit")
                messagebox.showinfo("MESSAGE","THANK YOU FOR YOUR FEEDBACK")
                con.close()
        bc=Button(s,text="SAVE",bg="#ff5757",fg="white",width=10,height=1,font=myfonte,command=save)
        bc.place(x=550,y=220)

        
        comment=Entry(s,width=40)
        comment.place(x=500,y=170)
        s.resizable(height="false",width="false")
        s.mainloop()

    ml4=Button(M,text="SERVICES",bg="#3b3a3a",fg="white",relief="flat",font=("times",14,"bold"),command=services)
    ml4.place(x=350,y=25)
    ml5=Button(M,text="REGISTER",bg="#3b3a3a",fg="white",relief="flat",font=("times",14,"bold"))
    ml5.place(x=500,y=25)
    mlp=PhotoImage(file="imap.png")
    mllabel=Label(M,image=mlp)
    
    
    mllabel.pack()

    def chatbox():
        cb=Toplevel(M)
        cb.title("CHAT BOX")
        cb.geometry("900x900")
        imgg=PhotoImage(file="sample4.png")
        iml=Label(cb,image=imgg)
        iml.pack(fill="both")
        
        def ml7():
            ml7="You>>.." + e.get()
            t.insert(END,"\n" + ml7)
            client=e.get().lower()


            if (client=="hi there" or client=="hi" or client=="hello"):
                t.insert(END, "\n" + "EZOY>>..hello what can i do for you")
            elif (client=="what are different courses available" or client=="what courses avaiable?" or client=="can you help me with the courses"):
                t.insert(END,"\n" +"EZOY>>..there is a different courses available 1.BASIC 2.INTERMEDIATE 3.ADVANCED 4.WRITING SKILLS 5.ACADEMIC WRITING")
            elif (client=="what is the fees struture" or client=="fees?" or client=="what will be the fees"):
                t.insert(END,"\n" +"EZOY>>..it depends according to the courses mam")
            elif (client=="basic" or client=="basic?"):
                t.insert(END,"\n" +"EZOY>>..2000/-")
            elif (client=="intermediate" or client=="intermediate?"):
                t.insert(END,"\n" +"EZOY>>..3000/-")
            elif (client=="session timings" or client=="what is the timings for the class?"):
                t.insert(END,"\n" +"EZOY>>..3000/-")
            else:
                t.insert(END,"\n" +"EZOY>>..i can't understand")
            e.delete(0,END)
            
               



        ml6=Label(cb,text="CHAT BOX>>>>>>>",bg="#96d1c5",fg="#333333",relief="flat",font=("times",20,"bold"))
        ml6.place(x=155,y=30)
        f=Frame(cb,bg="#96d1c5",width=500,height=600,highlightbackground="white",highlightthickness=5)
        f.place(x=160,y=70)
        
        
        t=Text(f,width=42,height=22,bg="#f9c0c2",padx=5,pady=5,font=("times",15,"bold"),wrap=CHAR,state=NORMAL)
        t.place(x=24,y=20)
       

        e=Entry(f,bg="white",relief="flat",fg="black",width=60)
        e.place(x=23,y=550)
        
        
        
        ml7=Button(f,text="ENTER",bg="#f59698",fg="#333333",relief="raised",font=("times",9,"bold"),height=0,width=7,command=ml7)
        ml7.place(x=400,y=547)
        cb.resizable(height="false",width="false")

        cb.mainloop()
    ml6=Button(M,text="CHAT BOX",bg="#3b3a3a",fg="white",relief="flat",font=("times",14,"bold"),command=chatbox)
    ml6.place(x=650,y=25)
    
   
    M.resizable(height="false",width="false")
    M.mainloop()

    

b=Button(c,text="CLICK HERE",bg="#ff5757",fg="white",relief="flat",font=("times",20,"bold"),command=menubar)
b.place(x=90,y=610)
c.resizable(height="false",width="false")
#<----------label------------->

c.mainloop()