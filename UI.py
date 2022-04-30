from tkinter import *
import mysql.connector as myConnector
import tkinter.messagebox as MessageBox
from tkinter import ttk

myDataBase = myConnector.connect(host="localhost", user="prerak", passwd="prerak", database="buynget")
myCursor   = myDataBase.cursor()
myCursor.execute("use buynget")

#################################################################################################################################################

def login():
    global USER_ID
    username = variables[0].get()
    password = variables[1].get()

    myCursor.execute("select * from accounts where username = '{}' and password = '{}'".format(username, password))
    count = myCursor.fetchall()

    try:
        count   = count[0]
        USER_ID = count[3]
        MessageBox.showinfo( "Logged In", "Welcome " + username + " !")
        variables[2].pack_forget()
        category()
    except:
        variables[0].set("")
        variables[1].set("")
        MessageBox.showinfo( "Alert", "Invalid Credentials")
#-------------------------------------------------------------------------------------------------------------------------------------------------
def sign_up():
    myCursor.execute("select count(*) from accounts where username = '{}'".format(sign_up_data[0])) 
    count1 = myCursor.fetchall()
    count1 = count1[0][0]
    myCursor.execute("select count(*) from accounts where email = '{}'".format(sign_up_data[1])) 
    count2 = myCursor.fetchall()
    count2 = count2[0][0]
    if count1 == 1 or count2 == 1:
        if count1 == 1:
            MessageBox.showinfo( "Alert", "Username already taken !")
            variables[3].set("")
        else:
            MessageBox.showinfo( "Alert", "Email already taken !")
            variables[4].set("")

    else:
        myCursor.execute("insert into accounts (username, email, password) values ('{}', '{}', '{}')".format(sign_up_data[0], sign_up_data[1], sign_up_data[2]))
        myDataBase.commit()

        
        myCursor.execute("select count(*) from accounts")
        Cid         = myCursor.fetchall()
        Cid         = Cid[0][0]
        myCursor.execute("insert into customers(customer_id, customer_name, age, gender, phone_no, country, state, street_name, street_no, pincode) values({}, '{}', {}, '{}', '{}', '{}', '{}', '{}', {}, '{}')".format(Cid, sign_up_data[3], sign_up_data[4], sign_up_data[5], sign_up_data[6], sign_up_data[7], sign_up_data[8], sign_up_data[9], sign_up_data[10], sign_up_data[11]))
        myDataBase.commit()     
#-------------------------------------------------------------------------------------------------------------------------------------------------
def store_account_credentials():
    username = variables[3].get()
    email    = variables[4].get()
    password = variables[5].get()

    sign_up_data.append(username)
    sign_up_data.append(email)
    sign_up_data.append(password)  
#-------------------------------------------------------------------------------------------------------------------------------------------------
def store_customer_credentials():
    name        = variables[6].get()
    age         = int(variables[7].get())
    gender      = variables[8].get()
    phone_no    = variables[9].get()
    country     = variables[10].get()
    state       = variables[11].get()
    street_name = variables[12].get()
    street_no   = int(variables[13].get())
    pincode     = variables[14].get()

    sign_up_data.append(name)
    sign_up_data.append(age)
    sign_up_data.append(gender)
    sign_up_data.append(phone_no)
    sign_up_data.append(country)
    sign_up_data.append(state)
    sign_up_data.append(street_name)
    sign_up_data.append(street_no)
    sign_up_data.append(pincode)
#-------------------------------------------------------------------------------------------------------------------------------------------------
def add_for_sell():
    item_id  = int(variables[15].get())
    quantity = int(variables[16].get())

    myCursor.execute("select item_id from sells where customer_id = {}".format(USER_ID))
    allowed_items = myCursor.fetchall()
    temp = []
    for x in allowed_items:
        temp.append(x[0])
    allowed_items = temp
    if item_id not in allowed_items:
        verdict = MessageBox.askquestion("Alert", "Trying to sell something new ! Want to add this item to your preference ?")
        if(verdict == "yes"):
            myCursor.execute("insert into sells values ({}, {})".format(USER_ID, item_id))
            myDataBase.commit()

            add = []
            add.append(item_id)
            add.append(quantity)
            variables[17].append(add)    
    else:
        add = []
        add.append(item_id)
        add.append(quantity)
        variables[17].append(add)

    variables[15].set("")
    variables[16].set("")

#################################################################################################################################################

def successful_payment(mode):
    variables[19] = mode
    myCursor.execute("insert into payments (customer_id, mode, amount) values({}, '{}', {})".format(USER_ID, variables[19], variables[18]))
    myDataBase.commit()
    successful_payment_frame    = Frame(window, width = 450, height = 600, bg = "#ffffff")    
    Title                       = Label(successful_payment_frame,
                                        text="Payment has been successfully\ncredited to your Account via: " + mode,
                                        font=("Vrinda", 15, "bold")).place(x=40,y=80)
    exit_button                 = Button(successful_payment_frame,
                                         text= 'Logout',
                                         height= 1,
                                         width=10,
                                         bg = "#5d00a8",
                                         fg = "#ffffff",
                                         font = ("Vrinda", 8, "bold"),
                                         command=lambda:[login_page(),successful_payment_frame.pack_forget()]).place(x=200,y=350)
    successful_payment_frame.pack()
#-------------------------------------------------------------------------------------------------------------------------------------------------
def payments_page():
    payments_page_frame  = Frame(window, width=450, height=600, bg = "#ffffff")
    Title                = Label(payments_page_frame, 
                                 text="Payment Portal", 
                                 font=("Vrinda",15, "bold")).place(x=150, y=20)
    payments_page_frame.pack()
    
    total        = Label(payments_page_frame,
                         text = "Amount to be credited in your Account:  " + str(variables[18]),
                         font=("Vrinda",15, "italic")).place(x=32, y=120)

    message      = Label(payments_page_frame,
                         text = "Select Mode for Transfer: ",
                         font=("Vrinda", 12, "italic")).place(x=32, y=160)


    UPI          = Button(payments_page_frame, 
                          text ="UPI",
                          height= 1,
                          width=20,
                          command= lambda:[successful_payment("UPI"), payments_page_frame.pack_forget()]).place(x=150,y=240)

    net_banking  = Button(payments_page_frame, 
                          text ="NET BANKING",
                          height= 1,
                          width=20,
                          command= lambda:[successful_payment("Net-Banking"), payments_page_frame.pack_forget()]).place(x=150,y=290)

    credit_card  = Button(payments_page_frame,
                          text ="CREDIT CARD",
                          height= 1,
                          width=20,
                          command= lambda:[successful_payment("Credit-Card"), payments_page_frame.pack_forget()]).place(x=150,y=340)

    debit_card   = Button(payments_page_frame,
                          text ="DEBIT CARD",
                          height= 1,
                          width=20,
                          command= lambda:[successful_payment("Debit-Card"), payments_page_frame.pack_forget()]).place(x=150,y=390)

    back_button  = Button(payments_page_frame,
                          text= 'BACK',
                          height= 1,
                          width=10,
                          bg = "#8d31d4",
                          fg = "#ffffff",
                          font = ("Vrinda", 8, "bold"),
                          command = lambda:[login_page(),payments_page_frame.pack_forget()]).place(x=70, y=500)
    
    payments_page_frame.pack()
#-------------------------------------------------------------------------------------------------------------------------------------------------
def seller_sells():
    seller_sells_frame  = Frame(window, width=450, height=600, bg = "#ffffff")

    table               = ttk.Treeview(seller_sells_frame, column=('item_name', 'quantity', 'price'),height=50)

    table.column("#0", width=0)
    table.column("item_name",anchor=CENTER, width=150)
    table.column("quantity",anchor=CENTER,width=150)
    table.column("price",anchor=CENTER,width=150)


    table.heading("#0",text="",anchor=CENTER)
    table.heading("item_name",text="ITEM",anchor=CENTER)
    table.heading("quantity",text="QUANTITY",anchor=CENTER)
    table.heading("price",text="PRICE",anchor=CENTER)

    list_of_items = {} # item_id :-  name, quantity, overall price
    variables[18] = 0
    for pair in variables[17]:
        item_id = pair[0]
        quantity = pair[1]
        myCursor.execute("select item_name, cost_price from items where item_id = {}".format(item_id))
        item       = myCursor.fetchall()
        item_name  = item[0][0]
        item_price = item[0][1]
        res = []
        res.append(item_name)
        res.append(quantity)
        res.append(item_price * quantity)
        variables[18] += item_price * quantity
        list_of_items[item_id] = res

    iid_ = 0
    for entry in list_of_items.keys():
        tup = ()
        tup = list(tup)
        tup.append(str(list_of_items[entry][0]))
        tup.append(str(list_of_items[entry][1]))
        tup.append(str(list_of_items[entry][2]))
        tup = tuple(tup)
        table.insert(parent='', index='end' , iid=iid_, text='' , values = tup)
        iid_ += 1

    next_button  = Button(seller_sells_frame, 
                          text= 'NEXT',
                          height= 1, 
                          width=10,
                          bg = "#5d00a8",
                          fg = "#ffffff",
                          font = ("Vrinda", 8, "bold"),
                          command = lambda:[payments_page(),seller_sells_frame.pack_forget()]).place(x=350, y=550)

    back_button  = Button(seller_sells_frame,
                          text= 'BACK', 
                          height= 1, 
                          width=10, 
                          bg = "#8d31d4",
                          fg = "#ffffff",
                          font = ("Vrinda", 8, "bold"),
                          command = lambda:[seller_page(),seller_sells_frame.pack_forget()]).place(x=20, y=550)
    
    table.pack()
    seller_sells_frame.pack()
#-------------------------------------------------------------------------------------------------------------------------------------------------
def empty_cart():
    variables[20].clear()
    myCursor.execute("select cart_id from carts where customer_id = {}".format(USER_ID))
    cart_id = myCursor.fetchall()
    try:
        cart_id = cart_id[0][0]
        myCursor.execute("delete from stores where cart_id = {}".format(cart_id))
        myDataBase.commit()
    except:
        pass
#-------------------------------------------------------------------------------------------------------------------------------------------------
def make_transactions():
    make_transactions_frame   = Frame(window, width=450, height=600, bg = "#ffffff")
    Title                     = Label(make_transactions_frame, 
                                      text = "Successful Payment of $" + str(variables[21]),
                                      font=("Vrinda", 18, "bold")).place(x=49, y=90)

    message                   = Label(make_transactions_frame, 
                                      text = "Happy Shopping !",
                                      font=("Vrinda", 12, "bold")).place(x=160, y=190)
    
    electronics_button        = Button(make_transactions_frame,
                                       text = "logout",
                                       height= 2,
                                       width = 30,
                                       bg = "#5d00a8",
                                       fg = "#ffffff",
                                       font = ("Vrinda", 8, "bold"),
                                       command=lambda:[login_page(), make_transactions_frame.pack_forget()]).place(x=120, y=490)
    make_transactions_frame.pack()
#-------------------------------------------------------------------------------------------------------------------------------------------------
def place_order():
    myCursor.execute("insert into orders (customer_id, order_date, delivery_date) values ({}, current_date(), current_date())".format(USER_ID))
    myDataBase.commit()
    
    myCursor.execute("select count(*) from orders")
    order_id = myCursor.fetchall()
    order_id = order_id[0][0]
    for item_ in variables[20]:
        item               = item_[0]
        item_id            = item[0]
        item_name          = item[1]
        item_selling_price = float(item[2])
        item_quantity      = item[3]
        variables[21] += item_quantity * item_selling_price
        # we don't allow quantity = 0, SQL constraint will catch it
        myCursor.execute("insert into ordered_items values ({}, {}, {})".format(order_id, item_id, item_quantity))
        myDataBase.commit()
#-------------------------------------------------------------------------------------------------------------------------------------------------
def buyer_table(item_type):
    selected_items = []
    quantity = StringVar()
    def select():
        for i in table.selection():
            # print(table.item(i)['values'])
            selected_items.append(str(table.item(i)['values'][1]))
            
        buyer_table_frame.pack_forget()    
        selected_items_frame       = Frame(window, width=450, height=600, bg = "#ffffff")
        Title                      = Label(selected_items_frame, text="Enter Quantity", font=("Vrinda", 10, "bold")).place(x=200, y=20)

        selected_items_frame.pack()
        quantities = []
        for i in range (len(selected_items)):
            item_quantity = Label(selected_items_frame, text=selected_items[i]).place(x=100, y = 30 * i+90)
            quantity      = StringVar()
            Entry(selected_items_frame, textvariable = quantity, width = 20).place(x=200, y = 30 * i+90)
            quantities.append(quantity)

        def add_selections():
            l = []
            for i in table.selection():
                temp = table.item(i)['values']
                temp.append(int(quantities[0].get()))
                quantities.pop(0)
                l.append(temp)
            variables[20].append(l)

            for entry in l:
                myCursor.execute("select cart_id from carts where customer_id = {}".format(USER_ID))
                cart_id = myCursor.fetchall()
                cart_id = cart_id[0][0]
                myCursor.execute("insert into stores values({}, {}, {})".format(cart_id, entry[0], int(entry[3])))
                myDataBase.commit()
    

        next_button                = Button(selected_items_frame,
                                            text="Proceed",
                                            height= 1, 
                                            width=10,
                                            bg = "#5d00a8",
                                            fg = "#ffffff",
                                            font = ("Vrinda", 8, "bold"),
                                            command = lambda:[add_selections(), buyer_page(), selected_items_frame.pack_forget()]).place(x=350, y=550)
            
        
        
    buyer_table_frame  = Frame(window, width=450, height=600, bg = "#ffffff")

    table              = ttk.Treeview(buyer_table_frame, column = ('item_id', 'item_name', 'price'), height=50)

    table.column("#0", width=0)
    table.column("item_id", anchor=CENTER, width=150)
    table.column("item_name", anchor=CENTER,width=150)
    table.column("price", anchor=CENTER, width=150)


    table.heading("#0", text="", anchor=CENTER)
    table.heading("item_id", text="ITEM ID", anchor=CENTER)
    table.heading("item_name", text="ITEM", anchor=CENTER)
    table.heading("price", text="PRICE", anchor=CENTER)

    myCursor.execute("select item_id, item_name, selling_price from items where item_type = '{}'".format(item_type))
    data = myCursor.fetchall()
    iid_ = 0
    for tup in data:
        tup = list(tup)
        tup[0] = str(tup[0])
        tup[2] = str(tup[2])
        table.insert(parent='', index='end', iid = iid_, text='', values=tup)
        iid_ += 1
    

    table.pack()

    next_button  = Button(buyer_table_frame,
                          text = 'NEXT', 
                          height= 1, 
                          width=10,
                          bg = "#5d00a8",
                          fg = "#ffffff",
                          font = ("Vrinda", 8, "bold"),
                          command = select).place(x=350, y=550)

    back_button  = Button(buyer_table_frame, 
                          text = 'BACK',
                          height= 1, 
                          width=10,
                          bg = "#8d31d4",
                          fg = "#ffffff",
                          font = ("Vrinda", 8, "bold"),
                          command = buyer_table).place(x=20,y=550)

    buyer_table_frame.pack()
#-------------------------------------------------------------------------------------------------------------------------------------------------
def buyer_page():
    try:
        myCursor.execute("insert into buyers values({})".format(USER_ID))
        myDataBase.commit()
        myCursor.execute("insert into carts (customer_id) values({})".format(USER_ID))
        myDataBase.commit()
    except:
        pass
    buyer_page_frame    = Frame(window, width=450, height=600, bg = "#ffffff")
    Title               = Label(buyer_page_frame, 
                                text = "Select Category",
                                font=("Vrinda",25, "bold")).place(x=100, y=90)

    electronics_button  = Button(buyer_page_frame,
                                 text = "ELECTRONICS",
                                 height= 2,
                                 width = 30,
                                 bg = "#5d00a8",
                                 fg = "#ffffff",
                                 font = ("Vrinda", 8, "bold"),
                                 command=lambda:[buyer_table("electronics"), buyer_page_frame.pack_forget()]).place(x=120, y=190)

    grocery_button      = Button(buyer_page_frame,
                                 text = "GROCERY",
                                 height= 2,
                                 width = 30,
                                 bg = "#8d31d4",
                                 fg = "#ffffff",
                                 font = ("Vrinda", 8, "bold"),
                                 command=lambda:[buyer_table("grocery"), buyer_page_frame.pack_forget()]).place(x=120, y=250)

    daily_care_button   = Button(buyer_page_frame,
                                 text = "DAILY CARE",
                                 height= 2,
                                 width = 30,
                                 bg = "#5d00a8",
                                 fg = "#ffffff",
                                 font = ("Vrinda", 8, "bold"),
                                 command=lambda:[buyer_table("daily care"), buyer_page_frame.pack_forget()]).place(x=120, y=310)

    empty_cart_button   = Button(buyer_page_frame,
                                 text = "Empty Cart",
                                 height= 1, 
                                 width=10, 
                                 command = empty_cart).place(x=100, y=550)

    finish_button       = Button(buyer_page_frame, 
                                text = "Pay", 
                                height= 1, 
                                width=10, 
                                command = lambda:[place_order(), make_transactions(), buyer_page_frame.pack_forget()]).place(x=280, y=550)
    buyer_page_frame.pack()
#-------------------------------------------------------------------------------------------------------------------------------------------------
def seller_page():
    try:
        myCursor.execute("insert into sellers values({})".format(USER_ID))
        myDataBase.commit()
    except:
        pass

    seller_page_frame   = Frame(window, width=450, height=600, bg = "#ffffff")
    Title               = Label(seller_page_frame, 
                                text="List Items to\nbe Sold", 
                                font=("Vrinda",25, "italic")).place(x=150,y=90)

    item_id             = Label(seller_page_frame, text="Item ID").place(x=100,y=230)
    quantity            = Label(seller_page_frame, text="Quantity").place(x=100,y=300)

    item_input          = Entry(seller_page_frame, textvariable = variables[15], width = 20, borderwidth=1, relief="solid").place(x=200,y=230)
    quantity_input      = Entry(seller_page_frame, textvariable = variables[16], width = 20, borderwidth=1, relief="solid").place(x=200,y=300)
    
    add_button          = Button(seller_page_frame, 
                                 text="ADD",
                                 height=2,
                                 width=10,
                                 bg = "#8d31d4",
                                 fg = "#ffffff",
                                 font = ("Vrinda", 8, "bold"),   
                                 command=lambda:[add_for_sell(), seller_page_frame.pack_forget(), seller_page()]).place(x=100,y=380)

    finish_button       = Button(seller_page_frame,
                                 text="FINISH", 
                                 height=2, 
                                 width=10,
                                 bg = "#5d00a8",
                                 fg = "#ffffff",
                                 font = ("Vrinda", 8, "bold"),
                                 command = lambda:[seller_sells(), seller_page_frame.pack_forget()]).place(x=280,y=380)

    seller_page_frame.pack()
#-------------------------------------------------------------------------------------------------------------------------------------------------
def category():
    category_frame = Frame(window, width = 450, height=600, bg = "#ffffff")
    Title          = Label(category_frame, text = "Sign in as...", font=("Vrinda",20, "italic")).place(x=160,y=120)
    back_button    = Button(category_frame,
                            text = "Back", 
                            height=1, 
                            width=8, 
                            command=category_frame.pack_forget).place(x=10,y=30)

    buyer_button   = Button(category_frame,
                            text = "BUYER",
                            height=3, 
                            width=30,
                            bg = "#5d00a8",
                            fg = "#ffffff",
                            font = ("Vrinda", 8, "bold"),
                            command=lambda:[buyer_page(),category_frame.pack_forget()]).place(x=120, y=250)

    seller_button  = Button(category_frame, 
                            text = "SELLER",
                            height=3, 
                            width=30,
                            bg = "#8d31d4",
                            fg = "#ffffff",
                            font = ("Vrinda", 8, "bold"),
                            command=lambda:[seller_page(),category_frame.pack_forget()]).place(x=120, y=350)
    category_frame.pack()
#-------------------------------------------------------------------------------------------------------------------------------------------------
def details_page():
    
    details_frame          = Frame(window, width=450, height=600, bg = "#ffffff")
    Title                  = Label(details_frame, text= "Enter Details",
                                          font=("Arial",15, "bold")).place(x=155, y=36)

    name              = Label(details_frame, text="Name").place(x=60, y=90)
    age               = Label(details_frame, text ="Age").place(x=60, y=130) 
    gender            = Label(details_frame, text="Gender").place(x=60, y=170)  
    phone             = Label(details_frame, text="Phone No.").place(x=60, y=210)  
    country           = Label(details_frame, text="Country").place(x=60, y=250)
    state             = Label(details_frame, text="State").place(x=60, y=290)
    street_name       = Label(details_frame, text="Street Name").place(x=60, y=330)
    street_no         = Label(details_frame, text="Street No.").place(x=60, y=370)
    pincode           = Label(details_frame, text="Pincode").place(x=60, y=410)
    


    name_input        = Entry(details_frame, textvariable = variables[6], width=30, borderwidth=1, relief="solid").place(x=200, y=90)
    age_input         = Entry(details_frame, textvariable = variables[7], width=30, borderwidth=1, relief="solid").place(x=200, y=130) 
    gender_input      = Entry(details_frame, textvariable = variables[8], width=30, borderwidth=1, relief="solid").place(x=200, y=170)
    phone_input       = Entry(details_frame, textvariable = variables[9], width=30, borderwidth=1, relief="solid").place(x=200, y=210)
    state_input       = Entry(details_frame, textvariable = variables[10], width=30, borderwidth=1, relief="solid").place(x=200, y=250)
    country_input     = Entry(details_frame, textvariable = variables[11], width=30, borderwidth=1, relief="solid").place(x=200, y=290)
    street_name_input = Entry(details_frame, textvariable = variables[12], width=30, borderwidth=1, relief="solid").place(x=200, y=330)
    street_no_input   = Entry(details_frame, textvariable = variables[13], width=30, borderwidth=1, relief="solid").place(x=200, y=370)
    pincode_input     = Entry(details_frame, textvariable = variables[14], width=30, borderwidth=1, relief="solid").place(x=200, y=410)    
    
    back_button       = Button(details_frame, 
                               text="Back",
                               height= 1, 
                               width=8,
                               bg = "#5d00a8",
                               fg = "#ffffff",
                               font = ("Vrinda", 8, "bold"),
                               command=lambda:[details_frame.pack_forget(), signup_page()]).place(x=10,y=30)

    submit            = Button(details_frame,
                               text="Sign Up !",
                               bg = "#5d00a8",
                               fg = "#ffffff",
                               font = ("Vrinda", 8, "bold"),
                               command=lambda:[store_customer_credentials(), sign_up(), details_frame.pack_forget(), login_page()]).place(x=200,y=540)
    
    details_frame.pack()
#-------------------------------------------------------------------------------------------------------------------------------------------------
def signup_page():
    sign_up_data.clear()
    signup_frame  = Frame(window, width = 450, height = 600, bg = "#ffffff")
    Title         = Label(signup_frame,
                          text = "Buy-n-Get",
                          font = ("Freestyle Script", 15, "bold")).place(x=340, y=12)
    
    user_name     = Label(signup_frame, text = "Username").place(x=80, y=200)  
    user_email    = Label(signup_frame, text = "Email ID").place(x=80, y=270)  
    user_password = Label(signup_frame, text = "Password").place(x=80, y=340)
    
    user_name_input_area     = Entry(signup_frame, textvariable = variables[3], width=30, borderwidth=1, relief="solid").place(x=200, y=200)  
    user_email_input_area    = Entry(signup_frame, textvariable = variables[4], width=30, borderwidth=1, relief="solid").place(x=200, y=270) 
    user_password_input_area = Entry(signup_frame, textvariable = variables[5], width=30, borderwidth=1, relief="solid").place(x=200, y=340)
    
    next_button   = Button(signup_frame,
                           text = "Next",
                           height= 1,
                           width=8,
                           bg = "#5d00a8",
                           fg = "#ffffff",
                           font = ("Vrinda", 8, "bold"),
                           command = lambda:[store_account_credentials(), signup_frame.pack_forget(), details_page()]).place(x = 200, y = 470)
                    

    back_button   = Button(signup_frame, 
                           text ="Back",
                           height=1,
                           width=8,
                           bg = "#5d00a8",
                           fg = "#ffffff",
                           font = ("Vrinda", 8, "bold"),
                           command = signup_frame.pack_forget).place(x=10, y=10)

    
    signup_frame.pack()    
#-------------------------------------------------------------------------------------------------------------------------------------------------
def login_page():
    initialize_variables()

    login_frame   = Frame(window, width=450, height=600, bg = "#ffffff")

    Title         = Label(login_frame,
                          text = "Buy-n-Get",
                          font = ("Freestyle Script", 15, "bold")).place(x=340, y=12)
    
    acc           = Label(login_frame,
                          text = "Login",
                          font = ("Arial",25, "bold")).place(x=170, y=150)
    
    username       = Label(login_frame, text = "Username").place(x=80, y=250)  
    password       = Label(login_frame, text = "Password").place(x=80, y=320)  
    username_input = Entry(login_frame, textvariable = variables[0], width=30, borderwidth=1, relief="solid").place(x = 150,y = 250)  
    password_input = Entry(login_frame, textvariable = variables[1], width=30, borderwidth=1, relief="solid").place(x=150, y=320)     
    
    variables[2]   = login_frame
    submit_button  = Button(login_frame, 
                            text = "Done",
                            height = 1, 
                            width = 8,
                            bg = "#5d00a8",
                            fg = "#ffffff",
                            font = ("Vrinda", 8, "bold"),
                            command = login).place(x=200, y=380)
    
    back_button   = Button(login_frame,
                            text = "Back",
                            height= 1, 
                            width=8,
                            bg = "#5d00a8",
                            fg = "#ffffff",
                            font = ("Vrinda", 8, "bold"),
                            command = login_frame.pack_forget).place(x=10, y=10) 
    login_frame.pack()

#################################################################################################################################################

def initialize_variables():
    global variables
    global USER_ID
    global sign_up_data
    USER_ID = -1
    variables = []

    sign_up_data = []
    sign_up_data.clear()

    # 0 : username input (login page)
    # 1 : password input (login page)
    # 2 : login frame    (login page)
    for i in range(0, 2):
        variables.append(StringVar())
    variables.append(-1)

    # 3 : name input      (signup page)
    # 4 : email input     (signup page)
    # 5 : password input  (signup page)
    for i in range(3, 6):
        variables.append(StringVar())

    # 6  :  name input        (details page)
    # 7  :  age input         (details page)
    # 8  :  gender input      (details page)
    # 9  :  phone input       (details page)
    # 10 :  country input     (details page)
    # 11 :  state input       (details page)
    # 12 :  street name input (details page)
    # 13 :  street no input   (details page)
    # 14 :  pincode input     (details page)
    for i in range(6, 15):
        variables.append(StringVar())

    # 15 : seller item id             (seller page)
    # 16 : seller quantity input      (seller page)
    # 17 : list of "list of id-quantity" which will be added in stock; the seller sells that item id
    # 18 : total amount we pay to seller
    # 19 : mode of payment
    for i in range(15, 17):
        variables.append(StringVar())
    variables.append([])
    variables.append(-1)
    variables.append(-1)

    # 20 : items selected by buyers
    # 21 : total cost for the purchase
    variables.append([])
    variables.append(0)

if __name__ == '__main__':

    window = Tk()
    window.geometry("450x600")
    window.configure(bg = "#ffffff")
    window.title("Buy-n-Get")
    Title         = Label(window,
                          text = "Buy-n-Get",
                          font = ("Freestyle Script", 40, "bold")).place(x=100, y=40)    

    USER_ID = -1
    variables = []
    sign_up_data = []

    initialize_variables()

    login_button  = Button(window, 
                           text = "LOGIN",
                           height = 3,
                           width = 30,
                           bg = "#5d00a8",
                           fg = "#ffffff",
                           font = ("Vrinda", 8, "bold"),
                           command = login_page).place(x=118, y=250)

    no_acc        = Label(window,
                          text = "Don't have an account?", 
                          font = ("Arial", 10)).place(x=157, y=350)

    signup_button = Button(window, 
                           text = "SIGN UP",
                           height = 3,
                           width = 30,
                           bg = "#8d31d4",
                           fg = "#ffffff",
                           font = ("Vrinda", 8, "bold"),
                           command = signup_page).place(x=118, y=380)

    window.mainloop()
