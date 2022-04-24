from tkinter import *
import mysql.connector as myConnector

def details_page():
    
    frame=Frame(window, width=450, height=600)
    Title = Label(frame, text= "Enter Details",font=("Arial",15, "bold")).place(x=155, y=40)
    
    gender = Label(frame, 
                  text = "Gender").place(x = 60,
                                           y = 110)  
    gender_input_area = Entry(frame,width = 30).place(x = 200,y = 110)

    Phone = Label(frame, 
                      text = "Phone No.").place(x = 60,
                                               y = 180)  
    phone_input_area = Entry(frame,width = 30).place(x = 200,y = 180)
    Street_no =Label(frame, 
                      text = "Street No.").place(x = 60,
                                               y = 250)
    Street_no_input_area = Entry(frame,width = 30).place(x = 200,y = 250)
    Street_name =Label(frame, 
                      text = "Street Name").place(x = 60,
                                               y = 320)
    Street_name_input_area = Entry(frame,width = 30).place(x = 200,y = 320)
    Pincode = Label(frame, text = "Pincode").place(x=60,y=390)
    pincode_input_area = Entry(frame,width = 30).place(x = 200,y = 390)
    state = Label(frame, text = "State").place(x=60,y=460)
    state_input_area = Entry(frame,width = 30).place(x = 200,y = 460)
    country = Label(frame, text = "Country").place(x=60,y=530)
    country_input_area = Entry(frame,width = 30).place(x = 200,y = 530)
    
    frame.pack()

def signup_page():
     
    frame = Frame(window, width = 450, height = 600)
    Title = Label(frame, text = "Buy-n-Get", font = ("Freestyle Script", 40, "bold")).place(x=155, y=60)
    
    user_name     = Label(frame, text="Name").place(x=80, y=200)  
    user_email    = Label(frame, text="Email ID").place(x=80, y=270)  
    user_password = Label(frame, text=" New Password").place(x=80, y=340)
    age =Label(frame,text = "Age").place(x = 80,y = 410) 
    
    next_button = Button(frame, text = "Next",height= 1, width=8,command=lambda:[details_page(),frame.pack_forget()]).place(x = 200,
                                              y = 470)
    back_button   = Button(frame, text="Back", height=1, width=8, command=frame.pack_forget).place(x=10, y=10)
    
    user_name_input_area     = Entry(frame, width=30).place(x=200, y=200)  
    user_email_input_area    = Entry(frame, width=30).place(x=200, y=270) 
    user_password_input_area = Entry(frame, width=30).place(x=200, y=340)
    user_age                = Entry(frame, width=30).place(x=200, y=410) 
    
    frame.pack()
    

def login_page():
     
    frame         = Frame(window, width=450, height=600)

    Title         = Label(frame,
                          text = "Buy-n-Get",
                          font = ("Freestyle Script", 40, "bold")).place(x=155, y=50)
    
    acc           = Label(frame,
                          text = "MY ACCOUNT",
                          font = ("Arial",15, "bold")).place(x=155, y=180)
    
    user_name     = Label(frame, text = "Username").place(x=80, y=250)  
    user_password = Label(frame, text = "Password").place(x=80, y=320)  
    
    submit_button = Button(frame, 
                           text = "Submit",
                           height= 1, width=8).place(x=200, y=380)
    
    back_button   = Button(frame,
                           text = "Back",
                           height= 1, width=8,
                           command = frame.pack_forget).place(x=10, y=10) 
    
    user_name_input_area     = Entry(frame, width=30).place(x = 150,y = 250)  
    user_password_entry_area = Entry(frame, width=30).place(x=150, y=320)  

    frame.pack()
    






window = Tk()
window.geometry("450x600")
window.title("Buy-n-Get")
Title = Label(window, text = "Buy-n-Get", font = ("Freestyle Script", 40, "bold")).place(x = 155, y = 60)

login_button  = Button(window, 
                       text = "LOGIN",
                       height = 3, width = 30,
                       command = login_page).place(x = 130, y = 200)

no_acc        = Label(window,
                      text = "Don't have an account?", 
                      font = ("Arial", 10)).place(x = 165, y = 300)

signUP_button = Button(window, 
                       text = "SIGN UP",
                       height = 3, width = 30,
                       command = signup_page).place(x = 130, y = 330)

window.mainloop()
