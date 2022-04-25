from tkinter import *
import mysql.connector as myConnector

myDataBase = myConnector.connect(host="localhost", user="prerak", passwd="prerak", database="buynget")
myCursor   = myDataBase.cursor()
myCursor.execute("use buynget")

#################################################################################################################################################



def insert_into_accounts():
    username_input = Entry(login_frame, width=30).place(x = 150,y = 250)  
    password_input = Entry(login_frame, width=30).place(x=150, y=320) 
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
    myCursor.execute("insert into accounts(username, email, password) values('{}', '{}', '{}')".format(username, email, password))

#################################################################################################################################################

def seller_page():
    frame               = Frame(window, width=450, height=600)
    Title               = Label(frame, text= "List Items to\nbe Sold", font=("Vrinda",25, "italic")).place(x=150,y=90)
    item_id             = Label(frame, text="Item ID").place(x=100,y=230)
    item_input_area     = Entry(frame, width = 20).place(x=200,y=230)
    
    quantity            = Label(frame, text="Quantity").place(x=100,y=300)
    quantity_input_area = Entry(frame, width = 20).place(x=200,y=300)
    
    add_button          = Button(frame, text="ADD", height=2, width=10, command=lambda:[frame.pack_forget(),seller_page()]).place(x=100,y=380)
    finish_button       = Button(frame, text="FINISH", height=2, width=10).place(x=280,y=380)

    frame.pack()
#-------------------------------------------------------------------------------------------------------------------------------------------------
def category():
    frame         = Frame(window, width = 450, height=600)
    Title         = Label(frame, text = "Sign in as...", font=("Vrinda",20, "italic")).place(x=160,y=120)
    back_button   = Button(frame, text = "Back", height=1, width=8, command=frame.pack_forget).place(x=10,y=30)
    seller_button = Button(frame, text = "SELLER", height=3, width=30).place(x=120,y=250)
    buyer_button  = Button(frame, text = "BUYER", height=3, width=30).place(x=120,y=350)
    frame.pack()
#-------------------------------------------------------------------------------------------------------------------------------------------------
def details_page():
    
    frame                  = Frame(window, width=450, height=600)
    Title                  = Label(frame, text= "Enter Details",
                                          font=("Arial",15, "bold")).place(x=155, y=40)


    gender                 = Label(frame, text="Gender").place(x=60, y=110)  
    Phone                  = Label(frame, text="Phone No.").place(x=60, y=180)  
    Street_no              = Label(frame, text="Street No.").place(x=60, y=250)
    Street_name            = Label(frame, text="Street Name").place(x=60, y=320)
    Pincode                = Label(frame, text="Pincode").place(x=60, y=390)
    country                = Label(frame, text="Country").place(x=60, y=530)
    state                  = Label(frame, text="State").place(x=60, y=460)

    gender_input_area      = Entry(frame, width=30).place(x=200, y=110)
    phone_input_area       = Entry(frame, width=30).place(x=200, y=180)
    Street_no_input_area   = Entry(frame, width=30).place(x=200, y=250)
    Street_name_input_area = Entry(frame, width=30).place(x=200, y=320)
    pincode_input_area     = Entry(frame, width=30).place(x=200, y=390)    
    state_input_area       = Entry(frame, width=30).place(x=200, y=460)
    country_input_area     = Entry(frame, width=30).place(x=200, y=530)

    back_button            = Button(frame, text="Back",height= 1, width=8,command=frame.pack_forget).place(x=10,y=30)
    
    frame.pack()
#-------------------------------------------------------------------------------------------------------------------------------------------------
def signup_page():
     
    frame         = Frame(window, width = 450, height = 600)
    Title         = Label(frame,
                          text = "Buy-n-Get",
                          font = ("Freestyle Script", 15, "bold")).place(x=340, y=12)
    
    user_name     = Label(frame, text = "Name").place(x=80, y=200)  
    user_email    = Label(frame, text = "Email ID").place(x=80, y=270)  
    user_password = Label(frame, text = " New Password").place(x=80, y=340)
    age           = Label(frame, text = "Age").place(x = 80,y = 410) 
    
    next_button   = Button(frame,
                           text = "Next",
                           height= 1,
                           width=8, 
                           command = lambda:[details_page(),frame.pack_forget()]).place(x = 200, y = 470)

    back_button   = Button(frame, 
                           text ="Back", 
                           height=1, 
                           width=8, 
                           command = frame.pack_forget).place(x=10, y=10)
    
    user_name_input_area     = Entry(frame, width=30).place(x=200, y=200)  
    user_email_input_area    = Entry(frame, width=30).place(x=200, y=270) 
    user_password_input_area = Entry(frame, width=30).place(x=200, y=340)
    user_age                 = Entry(frame, width=30).place(x=200, y=410) 
    
    frame.pack()    
#-------------------------------------------------------------------------------------------------------------------------------------------------
def login_page():
    login_frame   = Frame(window, width=450, height=600)

    Title         = Label(login_frame,
                          text = "Buy-n-Get",
                          font = ("Freestyle Script", 15, "bold")).place(x=340, y=12)
    
    acc           = Label(login_frame,
                          text = "MY ACCOUNT",
                          font = ("Arial",15, "bold")).place(x=160, y=180)
    
    username       = Label(login_frame, text = "Username").place(x=80, y=250)  
    password       = Label(login_frame, text = "Password").place(x=80, y=320)  
        

    submit_button  = Button(login_frame, 
                            text = "Submit",
                            height = 1, 
                            width = 8,
                            # command = lambda:[category(),login_frame.pack_forget()]).place(x=200, y=380)
                            command = insert_into_accounts).place(x=200, y=380)
    
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
