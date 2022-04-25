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




















******New Code*********



from tkinter import *

#import mysql.connector as myConnector

#myDataBase = myConnector.connect(host="localhost", user="prerak", passwd="prerak", database="buynget")
#myCursor   = myDataBase.cursor()
#myCursor.execute("use buynget")

#################################################################################################################################################



def insert_into_accounts():
    try:
        print(username_input.get())
        print(password_input.get())
    except:
        print("Enter something first")


    # myCursor.execute("select count(*) from accounts where username = '{}'".format(username))
    # count = myCursor.fetch()
    # count = count[0]
    # if count == 1:
    #     print("if") # goto buyer/seller
    #      # tkMessageBox.showinfo( "Hello Python", "Hello World")
    # else:
    #     login_frame.pack_forget
    
#-------------------------------------------------------------------------------------------------------------------------------------------------
def insert_into_customers(info):
    pass
    #myCursor.execute("insert into accounts(username, email, password) values('{}', '{}', '{}')".format(username, email, password))

#################################################################################################################################################

def seller_page():
    frame               = Frame(window, width=450, height=600)
    
    item_id_var = StringVar()
    quantity_var = StringVar()
    Title               = Label(frame, text= "List Items to\nbe Sold", font=("Vrinda",25, "italic")).place(x=150,y=90)
    item_id             = Label(frame, text="Item ID").place(x=100,y=230)
    item_input_area     = Entry(frame,textvariable =item_id_var, width = 20).place(x=200,y=230)
    
    quantity            = Label(frame, text="Quantity").place(x=100,y=300)
    quantity_input_area = Entry(frame,textvariable = quantity_var,width = 20).place(x=200,y=300)
    
    add_button          = Button(frame, text="ADD", height=2, width=10, command=lambda:[frame.pack_forget()]).place(x=100,y=380)
    finish_button       = Button(frame, text="FINISH", height=2, width=10).place(x=280,y=380)

    frame.pack()
#-------------------------------------------------------------------------------------------------------------------------------------------------
def category():
    frame         = Frame(window, width = 450, height=600)
    Title         = Label(frame, text = "Sign in as...", font=("Vrinda",20, "italic")).place(x=160,y=120)
    back_button   = Button(frame, text = "Back", height=1, width=8).place(x=10,y=30)
    seller_button = Button(frame, text = "SELLER", height=3, width=30, command=lambda:[seller_page(),frame.pack_forget()]).place(x=120,y=250)
    buyer_button  = Button(frame, text = "BUYER", height=3, width=30).place(x=120,y=350)
    frame.pack()
#-------------------------------------------------------------------------------------------------------------------------------------------------
def details_page():
    
    details_frame          = Frame(window, width=450, height=600)
    
    name_var=StringVar()
    age_var=StringVar()
    gender_var = StringVar()
    phone_var=StringVar()
    country_var=StringVar()
    state_var = StringVar()
    street_name_var=StringVar()
    street_no_var=StringVar()
    pincode_var = StringVar()
    
    Title                  = Label(details_frame, text= "Enter Details",
                                          font=("Arial",15, "bold")).place(x=155, y=36)

    name              = Label(details_frame, text="Name").place(x=60, y=90)
    age               = Label(details_frame, text = "Age").place(x=60, y=130) 
    gender            = Label(details_frame, text="Gender").place(x=60, y=170)  
    phone             = Label(details_frame, text="Phone No.").place(x=60, y=210)  
    country           = Label(details_frame, text="Country").place(x=60, y=250)
    state             = Label(details_frame, text="State").place(x=60, y=290)
    street_name       = Label(details_frame, text="Street Name").place(x=60, y=330)
    street_no         = Label(details_frame, text="Street No.").place(x=60, y=370)
    pincode           = Label(details_frame, text="Pincode").place(x=60, y=410)
    


    name_input        = Entry(details_frame,textvariable= name_var,width = 30).place(x=200, y=90)
    user_age          = Entry(details_frame,textvariable= age_var, width=30).place(x=200, y=130) 
    gender_input      = Entry(details_frame,textvariable= gender_var, width=30).place(x=200, y=170)
    phone_input       = Entry(details_frame,textvariable= phone_var, width=30).place(x=200, y=210)
    state_input       = Entry(details_frame,textvariable= state_var, width=30).place(x=200, y=250)
    country_input     = Entry(details_frame,textvariable= country_var, width=30).place(x=200, y=290)
    street_name_input = Entry(details_frame,textvariable= street_name_var, width=30).place(x=200, y=330)
    street_no_input   = Entry(details_frame,textvariable= street_no_var, width=30).place(x=200, y=370)
    pincode_input     = Entry(details_frame,textvariable= pincode_var, width=30).place(x=200, y=410)    
    

    back_button       = Button(details_frame, 
                               text="Back",
                               height= 1, 
                               width=8,
                               command=details_frame.pack_forget).place(x=10,y=30)

    submit            = Button(details_frame,
                               text="Sign Up !",
                               command=lambda:[login_page(),details_frame.pack_forget()]).place(x=200,y=540)
    
    details_frame.pack()
#-------------------------------------------------------------------------------------------------------------------------------------------------
def signup_page():
     
    signup_frame  = Frame(window, width = 450, height = 600)
    name_var=StringVar()
    passw_var=StringVar()
    email_var = StringVar()
    Title         = Label(signup_frame,
                          text = "Buy-n-Get",
                          font = ("Freestyle Script", 15, "bold")).place(x=340, y=12)
    
    user_name     = Label(signup_frame, text = "Name").place(x=80, y=200)  
    user_email    = Label(signup_frame, text = "Email ID").place(x=80, y=270)  
    user_password = Label(signup_frame, text = " New Password").place(x=80, y=340)
    
    user_name_input_area     = Entry(signup_frame,textvariable = name_var, width=30).place(x=200, y=200)  
    user_email_input_area    = Entry(signup_frame,textvariable = email_var, width=30).place(x=200, y=270) 
    user_password_input_area = Entry(signup_frame,textvariable = passw_var, width=30,show = '*').place(x=200, y=340)
    
    next_button   = Button(signup_frame,
                           text = "Next",
                           height= 1,
                           width=8, 
                           command = lambda:[details_page(),signup_frame.pack_forget()]).place(x = 200, y = 470)

    back_button   = Button(signup_frame, 
                           text ="Back", 
                           height=1, 
                           width=8, 
                           command = signup_frame.pack_forget).place(x=10, y=10)

    
    signup_frame.pack()    
#-------------------------------------------------------------------------------------------------------------------------------------------------
def login_page():
    login_frame   = Frame(window, width=450, height=600)
    name_var=StringVar()
    passw_var=StringVar()

    Title         = Label(login_frame,
                          text = "Buy-n-Get",
                          font = ("Freestyle Script", 15, "bold")).place(x=340, y=12)
    
    acc           = Label(login_frame,
                          text = "Login",
                          font = ("Arial",25, "bold")).place(x=170, y=150)
    
    username       = Label(login_frame, text = "Username").place(x=80, y=250)  
    password       = Label(login_frame, text = "Password").place(x=80, y=320)  
    username_input = Entry(login_frame,textvariable = name_var, width=30).place(x = 150,y = 250)  
    password_input = Entry(login_frame,textvariable = passw_var,width=30,show= '*').place(x=150, y=320) 
   

    submit_button  = Button(login_frame, 
                            text = "Submit",
                            height = 1, 
                            width = 8,
                            # command = lambda:[category(),login_frame.pack_forget()]).place(x=200, y=380)
                            command = lambda:[print(name_var.get()),print(passw_var.get()),category(),login_frame.pack_forget()]).place(x=200, y=380)
    
    back_button    = Button(login_frame,
                            text = "Back",
                            height= 1, width=8,
                            command = login_frame.pack_forget).place(x=10, y=10) 
    login_frame.pack()
    

#################################################################################################################################################

if __name__ == '__main__':

    window = Tk()
    window.geometry("450x600")
    window.title("Buy-n-Get")
    Title         = Label(window,
                          text = "Buy-n-Get     ",
                          font = ("Freestyle Script", 40, "bold")).place(x=100, y=40)

    login_button  = Button(window, 
                           text = "LOGIN",
                           height = 3, width = 30,
                           command = login_page).place(x=118, y=250)

    no_acc        = Label(window,
                          text = "Don't have an account?", 
                          font = ("Arial", 10)).place(x=157, y=350)

    signUP_button = Button(window, 
                           text = "SIGN UP",
                           height = 3, width = 30,
                           command = signup_page).place(x=118, y=380)

    window.mainloop()
