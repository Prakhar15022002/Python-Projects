#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *

bank = Tk()
bank.configure(bg="blue")
bank.geometry("600x700")
bank.maxsize(900,900)

def register():
    def Back():
        yellow_frame.destroy()
        login()
    
    def Return():
        yellow_frame.destroy()
        welcome()

    def Register_detail():
        a = username.get()
        b = password.get()
        print(a)
        print(b)
        yellow_frame.destroy()
        login()

    
    yellow_frame = Frame(bank,height=700,width=600,bg="#FDA50F")
    yellow_frame.pack()

    white_frame = Frame(yellow_frame,height=600,width=500,bg="white")
    white_frame.place(x=50,y=50) 

    account_text = Label(white_frame,text= "New Account",font=("Times",30,"bold"),bg="white",fg="Black")
    account_text.place(x=50,y=100)

    username = Entry(white_frame,font=("Open Sans",15),width =35,bg="white",border = 0)
    username.place(x=50,y=170)
    username.insert(0,"Username")

    line = Frame(white_frame,height= 2 ,width=400,bg="black")
    line.place(x=50,y=200)
    
    password = Entry(white_frame,font=("Open Sans",15),width =35,bg="white",border = 0,)
    password.place(x=50,y=230)
    password.insert(0,"Password")

    line = Frame(white_frame,height= 2 ,width=400,bg="black")
    line.place(x=50,y=260)

    register_button = Button(white_frame,text = "Register",bg="#FDA50F",fg="black",width=20,font=("Times",18,"bold"),command=Register_detail)
    register_button.place(x=100,y=300)

    back_button = Button(white_frame,text="Back",font=("Open Sans",12),bg="White",activebackground="white",border=0,command=Back)
    back_button.place(x=370,y=15)
    
    return_button = Button(white_frame,text="Return",font=("Open Sans",12),bg="White",activebackground="white",border=0,command=Return)
    return_button.place(x=430,y=15)

def login():
    def homepage():
        a=username.get()
        b=password.get()
        print(a)
        print(b)
        yellow_frame.destroy()
        home()

    def Back():
        yellow_frame.destroy()
        welcome()
    
    def tab3():
        yellow_frame.destroy()
        register()



    yellow_frame = Frame(bank,height=700,width=600,bg="#FDA50F")
    yellow_frame.pack()

    white_frame = Frame(yellow_frame,height=600,width=500,bg="white")
    white_frame.place(x=50,y=50)        
    
    login_text = Label(white_frame,text= "Login",font=("Times",30,"bold"),bg="white",fg="Black")
    login_text.place(x=50,y=100)

    username = Entry(white_frame,font=("Open Sans",15),width =35,bg="white",border = 0)
    username.place(x=50,y=170)
    username.insert(0,"Username")

    line = Frame(white_frame,height= 2 ,width=400,bg="black")
    line.place(x=50,y=200)
    
    password = Entry(white_frame,font=("Open Sans",15),width =35,bg="white",border = 0)
    password.place(x=50,y=230)
    password.insert(0,"Password")

    line = Frame(white_frame,height= 2 ,width=400,bg="black")
    line.place(x=50,y=260)

    forget = Button(white_frame,text = "Forget",fg="blue",bg="white",activebackground="white",font=("Open Sans",13),border=0)
    forget.place(x=380,y=230)

    login_button = Button(white_frame,text = "Login",bg="#FDA50F",fg="black",width=20,font=("Times",18,"bold"),command=homepage)
    login_button.place(x=100,y=300)

    ltext = Label(white_frame,text = "Looks Like you're New here",font=("Open Sans",13),bg="white",fg="black")
    ltext.place(x=50,y=530)

    registerbutton  = Button(white_frame,text ="Register Now",font=("Open Sans",13,"bold"),bg="white",fg="blue",border=0,activebackground="white",command=tab3)
    registerbutton.place(x=255,y=528)

    back_button = Button(white_frame,text="Back",font=("Open Sans",12),bg="White",activebackground="white",border=0,command=Back)
    back_button.place(x=430,y=15)

def welcome():
    def next():
        white_frame.destroy()
        yellow_frame.destroy()
        login()
        

        
    white_frame = Frame(bank,height=350,width=800,bg="white")
    white_frame.pack(side="top")

    yellow_frame = Frame(bank,height=350,width=600,bg="#FDA50F")
    yellow_frame.pack(side="bottom")
    
    name = Label(white_frame,text = "Water Quality Prediction",bg="white",fg="BLACK",font=("Space Grotesk",45,"bold"))
    name.place(x=70,y=120) 


    welcome_text = Label(yellow_frame,text="Welcome to Water Quality Prediction",font=("Open Sans",12,"bold"),bg="#FDA50F")
    welcome_text.place(x=5,y=15)


    welcome_button = Button(yellow_frame,text="WELCOME",bg="#FDA50F",fg = "blue",font=("Times",15,"bold"),border=0,activebackground="#FDA50F",command=next)
    welcome_button.place(x=230,y=180)

def home():
    yellow_frame = Frame(bank,height=700,width=600,bg="#FDA50F")
    yellow_frame.pack()

    white_frame = Frame(yellow_frame,height=600,width=500,bg="white")
    white_frame.place(x=50,y=50) 

    sensor_text = Label(white_frame,text= "Choose Your Sensor !",font=("Times",30,"bold"),bg="white",fg="Black")
    sensor_text.place(x=60,y=60)

    temp_button = Button(white_frame,text = "Temperature Sensor",bg="#FDA50F",fg="black",width=20,font=("Times",18,"bold"))
    temp_button.place(x=10,y=150)
    
    Ph_button = Button(white_frame,text = "PH Sensor",bg="#FDA50F",fg="black",width=20,font=("Times",18,"bold"))
    Ph_button.place(x=200,y=240)
    
    water_button = Button(white_frame,text = "Waterlevel Sensor",bg="#FDA50F",fg="black",width=20,font=("Times",18,"bold"))
    water_button.place(x=10,y=330)
    
    Turb_button = Button(white_frame,text = "Turbidity Sensor",bg="#FDA50F",fg="black",width=20,font=("Times",18,"bold"))
    Turb_button.place(x=200,y=420)
    
    
welcome()

bank.mainloop()


# In[ ]:




