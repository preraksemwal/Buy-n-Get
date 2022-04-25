from tkinter import *

window = Tk()
window.geometry("500x660")
window.title("Buy-n-Get")
Title = Label(window, text= "Buy-n-Get",font=("Freestyle Script",40, "bold")).place(x=155, y=60)

def seller_page():
    frame=Frame(window, width=450, height=600)
    Title = Label(frame, text= "List Items to\nbe Sold",font=("Vrinda",25, "italic")).place(x=150,y=90)
    item_id = Label(frame,text="Item ID").place(x=100,y=230)
    item_input_area= Entry(frame,width = 20).place(x = 200,y = 230)
    
    quantity = Label(frame,text="Quantity").place(x=100,y=300)
    quantity_input_area = Entry(frame,width = 20).place(x = 200,y = 300)
    
    add_button = Button(frame,text= "ADD",height=2,width=10,command=lambda:[frame.pack_forget(),seller_page()]).place(x=100,y=380)
    finish_button = Button(frame,text= "FINISH",height=2,width=10).place(x=280,y=380)

    
    frame.pack()
    
def category():
    frame=Frame(window, width=450, height=600)
    Title = Label(frame, text= "Join As...",font=("Vrinda",25, "italic")).place(x=160,y=120)
    back_button = Button(frame, text= "Back",height= 1, width=8,command=frame.pack_forget).place(x=10,y=30)
    seller_button = Button(frame, text = "SELLER",height = 3, width= 30,command=lambda:[seller_page(),frame.pack_forget()]).place(x=120,y=250)
    buyer_button = Button(frame,text= "BUYER",height=3,width=30).place(x=120,y=350)
    frame.pack()


def details_page():
    
    frame=Frame(window, width=450, height=660)
    Title = Label(frame, text= "Enter Details",font=("Arial",15, "bold")).place(x=155, y=40)
    
    name = Label(frame,text="Name").place(x=60,y=90)
    name_input_area= Entry(frame,width = 30).place(x = 200,y = 90)
    
    age = Label(frame,text="Age").place(x=60,y=140)
    age_input_area = Entry(frame,width = 30).place(x = 200,y = 140)
    
    gender = Label(frame,text = "Gender").place(x = 60,y = 190)  
    gender_input_area = Entry(frame,width = 30).place(x = 200,y = 190)

    Phone = Label(frame,text = "Phone No.").place(x = 60,y = 240)  
    phone_input_area = Entry(frame,width = 30).place(x = 200,y = 240)
    
    Street_no =Label(frame,text = "Street No.").place(x = 60,y = 290)
    Street_no_input_area = Entry(frame,width = 30).place(x = 200,y = 290)
    
    Street_name =Label(frame,text = "Street Name").place(x = 60,y = 340)
    Street_name_input_area = Entry(frame,width = 30).place(x = 200,y = 340)
    
    Pincode = Label(frame, text = "Pincode").place(x=60,y=390)
    pincode_input_area = Entry(frame,width = 30).place(x = 200,y = 390)
    
    state = Label(frame, text = "State").place(x=60,y=440)
    state_input_area = Entry(frame,width = 30).place(x = 200,y = 440)
    
    country = Label(frame, text = "Country").place(x=60,y=490)
    country_input_area = Entry(frame,width = 30).place(x = 200,y = 490)
    
    back_button = Button(frame, text= "Back",height= 1, width=8,command=frame.pack_forget).place(x=10,y=30)
    
    submit = Button(frame,text="Sign Up now!",command=lambda:[login_page(),frame.pack_forget()]).place(x=160,y=540)
    
    frame.pack()

def signup_page():
     
    frame=Frame(window, width=450, height=660)
    Title = Label(frame, text= "Buy-n-Get",font=("Freestyle Script",40, "bold")).place(x=155, y=60)
    
   
        
    
    user_name = Label(frame, 
                  text = "Username").place(x = 80,
                                           y = 200)  
    

    user_email = Label(frame, 
                      text = "Email ID").place(x = 80,
                                               y = 270)  
    user_password =Label(frame, 
                      text = " New Password").place(x = 80,
                                               y = 340)
    
    
    next_button = Button(frame, text = "Next",height= 1, width=8,command=lambda:[details_page(),frame.pack_forget()]).place(x = 200,
                                              y = 410)
    
    back_button = Button(frame, text= "Back",height= 1, width=8,command=frame.pack_forget).place(x=10,y=10)
    
    user_name_input_area = Entry(frame,width = 30).place(x = 200,y = 200)  
    
    user_email_input_area = Entry(frame,width = 30).place(x = 200,y = 270) 
    
    user_password_input_area =Entry(frame,width = 30).place(x = 200,y = 340)
    
    
    frame.pack()
    
def login_page():
     
    frame=Frame(window, width=450, height=600)
    Title = Label(frame, text= "Buy-n-Get",font=("Freestyle Script",40, "bold")).place(x=155, y=50)
    
    acc = Label(frame, text= "MY ACCOUNT",font=("Arial",15, "bold")).place(x=155, y=180)
    
    user_name = Label(frame, 
                  text = "Username").place(x = 80,
                                           y = 250)  
    

    user_password = Label(frame, 
                      text = "Password").place(x = 80,
                                               y = 320)  
    
    submit_button = Button(frame, 
                       text = "Submit",height= 1, width=8,command=lambda:[category(),frame.pack_forget()]).place(x = 200,
                                              y = 380)
    
    back_button = Button(frame, text= "Back",height= 1, width=8,command=frame.pack_forget).place(x=10,
                                                    y=10) 
    
    user_name_input_area = Entry(frame,width = 30).place(x = 150,y = 250)  
    
    user_password_entry_area = Entry(frame,width = 30).place(x = 150,y = 320)  
    frame.pack()
    

login_button = Button(window, 
                       text = "LOGIN",height= 3, width=30,command= login_page).place(x = 130,
                                              y = 200)
no_acc = Label(window, text= "Don't have an account?",font=("Arial",10)).place(x=165,y=300)

signUP_button = Button(window, 
                       text = "SIGN UP",height= 3, width=30,command= signup_page).place(x = 130,
                                              y = 330)

window.mainloop()
