from tkinter import *
from PIL import ImageTk,Image
from tkinter.filedialog import askopenfile
from tkinter import filedialog
from email.message import EmailMessage
import imghdr

import smtplib


coffee_selected = ''
roast_selected = ''
type_selected = ''
weight_selected = ''
price = 0



root = Tk()
root.title('Fairnist Order')
root.geometry('1600x800')
root.config(bg='GRAY17')


backgroundImage = Image.open('background.png')
background_resized = backgroundImage.resize((1600,900),Image.ANTIALIAS)
bgI = ImageTk.PhotoImage(background_resized)
background = Label(root, image=bgI)
background.place(x=0,y=0)


title = Label(root,text='Welcome to Fairnist Ordering')
title.place(x=20,y=20)
title.config(bg='GRAY50',fg ='WHITE',font=('Courier',30))


coffeeLabel = Label(root,text='Select Your Coffee')
coffeeLabel.place(x=20,y=80)
coffeeLabel.config(bg='GRAY50',fg ='WHITE',font=('Courier',20))


selection = Label(root,text='-Select-',bg='gray50',fg='white')
selection.place(x=20,y=120)
selection.config(font=('Courier',20))



def select_wild_honey():
    global coffee_selected
    coffee_selected = 'Wild Honey'

    selection['text'] = 'Wild Honey'
    roast_options_display()

def select_brown_ale():
    global coffee_selected
    coffee_selected = 'Brown Ale'

    selection['text'] = 'Brown Ale Peaberry'
    roast_options_display()

def select_sweet_cherry():
    global coffee_selected
    coffee_selected = 'Sweet Cherry'


    selection['text'] = 'Sweet Cherry'
    roast_options_display()



#Wildhoney icon
wildhoney = Image.open('wildhoney.png')
wh_resized = wildhoney.resize((210,200),Image.ANTIALIAS)
wh = ImageTk.PhotoImage(wh_resized)
wildhoney_icon = Button(root,image=wh,command=select_wild_honey)
wildhoney_icon.place(x=20,y=150)

#BrownAle icon
brownale = Image.open('brownale.png')
ba_resized = brownale.resize((210,200),Image.ANTIALIAS)
ba = ImageTk.PhotoImage(ba_resized)
brownale_icon = Button(root,image=ba,command=select_brown_ale)
brownale_icon.place(x=250,y=150)

#SweetCherry icon
sweetcherry = Image.open('sweetcherry.png')
sc_resized = sweetcherry.resize((210,200),Image.ANTIALIAS)
sc = ImageTk.PhotoImage(sc_resized)
sweetcherry_icon = Button(root,image=sc,command=select_sweet_cherry)
sweetcherry_icon.place(x=480,y=150)

#Center alignment variable
roastX = 310

def medium_roast():
    global roastX
    roastX = 315

    global roast_selected
    roast_selected = 'Medium'

    roastSelectionText['text'] = 'Medium'
    roastSelectionText.place(x=roastX, y=450)
    coffee_type_display()


def dark_roast():
    global roastX
    roastX = 325

    global roast_selected
    roast_selected = 'Dark'

    roastSelectionText['text'] = 'Dark'
    roastSelectionText.place(x=roastX,y=450)
    coffee_type_display()


#Medium Roast Icon
medium = Image.open('mediumr.png')
medium_resize = medium.resize((210, 200), Image.ANTIALIAS)
mediumroast = ImageTk.PhotoImage(medium_resize)
mediumroast_icon = Button(root, image=mediumroast, command=medium_roast)

#Dark Roast Icon
dark = Image.open('darkr.png')
dark_resize = dark.resize((210, 200), Image.ANTIALIAS)
darkroast = ImageTk.PhotoImage(dark_resize)
darkroast_icon = Button(root, image=darkroast, command=dark_roast)

roastSelectionText = Label(root,text='Select')
roastSelectionText.config(bg='GRAY50',fg='white',font=('Courier',20))


def roast_options_display():
    mediumroast_icon.place(x=20, y=370)
    darkroast_icon.place(x=480,y=370)

    selectRoast = Label(root,text='Select Your Roast')
    selectRoast.place(x=250, y=380)
    selectRoast.config(bg='GRAY50', fg='WHITE',font=('Courier',20))
    roastSelectionText.place(x=roastX,y=450)

#Alignment Variable
selectx = 310

def ground_selected():
    global selectx
    selectx = 310

    global type_selected
    type_selected = 'Ground'

    typeSelectionText['text'] = 'Ground'
    typeSelectionText.place(x=selectx, y=670)
    weight_selection_display()

def beans_selected():
    global selectx
    selectx = 320

    global type_selected
    type_selected = 'Beans'

    typeSelectionText['text'] = 'Beans'
    typeSelectionText.place(x=selectx, y=670)
    weight_selection_display()

#Ground Icon
ground = Image.open('ground.png')
ground_resized = ground.resize((210, 200), Image.ANTIALIAS)
groundCoffeee = ImageTk.PhotoImage(ground_resized)
groundCoffeee_icon = Button(root, image=groundCoffeee,command=ground_selected)

#Bean Icon
bean = Image.open('bean.png')
bean_resized = bean.resize((210, 200), Image.ANTIALIAS)
beanCoffee = ImageTk.PhotoImage(bean_resized)
beanCoffee_icon = Button(root, image=beanCoffee,command=beans_selected)

typeSelectionText = Label(root,text='Select')
typeSelectionText.config(bg='GRAY50',fg='white',font=('Courier',20))

def coffee_type_display():
    global selectx
    groundCoffeee_icon.place(x=20,y=590)
    beanCoffee_icon.place(x=480, y=590)

    selectType = Label(root, text='Ground or Beans?')
    selectType.config(bg='Gray50',fg='white',font=('Courier',20))
    selectType.place(x=255, y=590)

    typeSelectionText.place(x=selectx,y=670)


def g250_selected():
    global weight_selected
    weight_selected = '250g'
    label['text'] = weight_selected
    display_number_bag()
    display_price()


def kg2_selected():
    global weight_selected
    weight_selected = '2kg'
    label['text'] = weight_selected
    display_number_bag()
    display_price()

label = Label(root, text='What Size?')
label.config(bg='GRAY50', fg='WHITE', font=('Courier', 20))


#Weight bag icon
weight = Image.open('weighticon.png')
weight = weight.resize((210,200), Image.ANTIALIAS)
weight = ImageTk.PhotoImage(weight)
weight_icon = Button(root, image=weight)


g250 = Image.open('250gbutton.png')
g250 = g250.resize((95,60), Image.ANTIALIAS)
g250 = ImageTk.PhotoImage(g250)
button250g = Button(root, image=g250, command=g250_selected)


kg2 = Image.open('2kgbutton.png')
kg2 = kg2.resize((95,60), Image.ANTIALIAS)
kg2 = ImageTk.PhotoImage(kg2)
button2kg = Button(root, image=kg2, command=kg2_selected)

def weight_selection_display():
    weight_icon.place(x=780,y=150)

    label.place(x=780, y=120)

    button250g.place(x=780, y=370)
    button2kg.place(x=895, y=370)

#Number of Bags
numberLabel = Label(root,text='How Many Bags?')
numberLabel.config(bg='Gray50',fg='White', font=('Courier',20),width=16)
total = 0

def add_bags():
    global total
    total += 1
    bag = 'bags'
    if total == 1:
        bag = 'bag'
    elif total > 1:
        bag = 'bags'

    numberLabel['text'] = (str(total),bag)
    display_email()
    display_price()


def subtract_bags():
    global total
    bag = 'bag'
    if total >1:
        total -=1
        if total == 1:
            bag = 'bag'
        elif total > 1:
            bag = 'bags'
    else:
        total = 1

    numberLabel['text'] = (str(total), bag)
    display_email()
    display_price()



add = Image.open('addbutton.png')
add = add.resize((95,90), Image.ANTIALIAS)
add = ImageTk.PhotoImage(add)
addbutton = Button(root, image=add, command=add_bags)

subtract = Image.open('subtractbutton.png')
subtract = subtract.resize((95,90), Image.ANTIALIAS)
subtract = ImageTk.PhotoImage(subtract)
subtractbutton = Button(root, image=subtract, command=subtract_bags)


def display_number_bag():
    numberLabel.place(x=780, y=440)
    addbutton.place(x=780,y=480)
    subtractbutton.place(x=895,y=480)


email = ''
customer = ''


def get_email():
    global email
    global customer
    email = emailInput.get()

    if '@'  in email:
        emailLabel['text'] = 'Confirmed'
        emailLabel.config(bg='green')
        print(email)
        if email[0].isnumeric():
            customer = 'Student'
        elif email[0].isalpha():
            customer = 'Adult'
        display_price()
        show_price()
    else:
        emailLabel['text'] = 'Non Valid Email'
        emailLabel.config(bg='red')






emailLabel = Label(root,text='Enter Your Email',bg='Gray50',fg='white',font=('Courier',20),width=16)
emailInput = Entry(root, width=23)
confirm = Button(root,text='Confirm',font=('Courier',20), width=16, command=get_email)


def display_email():
    emailLabel.place(x=780, y=590)
    emailInput.place(x=780, y=620)
    confirm.place(x=780, y=670)


priceLabel = Label(root,bg='Gray50',fg='white',font=('Courier',20),width=16)

def display_price():
    global customer
    global total
    global weight_selected
    global price
    studentPrice = [250,549]
    adultPrice = [250,549]

    if customer == 'Student':
        if weight_selected == '250g':
            if total == 4: #Temporary Stock Clearance Price
                price = 900
            else:
                price = studentPrice[0]*total
        elif weight_selected == '2kg':
            price = studentPrice[1]*total
    elif customer == 'Adult':
        if weight_selected == '250g':
            if total == 4: #Temporary Stock Clearance Price
                price = 900
            else:
                price = adultPrice[0]*total
        elif weight_selected == '2kg':
            price = adultPrice[1]*2*total

    priceLabel['text'] = ('Total:',str(price)+'THB')

def show_price():
    priceLabel.place(x=780, y=720)
    display_details()


addressLabel = Label(root,text='Enter Your Address',font=('Courier',20),bg='Gray50',fg='white')
addressInput = Entry(root,width=23)
commentLabel = Label(root,text='Additional Comment?',font=('Courier',20),bg='gray50',fg='white')
commentInput = Entry(root,width=23)
phoneLabel = Label(root,text = 'Phone Number',font=('Courier',20),bg='Gray50',fg='White')
phoneInput = Entry(root,width=23)

address = ''
comment = ''
phoneNumber = ''


def get_details():
    global address
    global comment
    global phoneNumber
    address = addressInput.get()
    comment = commentInput.get()
    phoneNumber = phoneInput.get()
    receipt()


confirmDetails = Button(root,text='Confirm',font=('Courier',20), width=16,command=get_details)

def display_details():
    addressLabel.place(x=1070,y=120)
    addressInput.place(x=1070,y=150)
    commentLabel.place(x=1070,y=200)
    commentInput.place(x=1070,y=230)
    phoneLabel.place(x=1070,y=280)
    phoneInput.place(x=1070,y=310)
    confirmDetails.place(x=1070,y=370)


receiptTitle = Label(root,text='Receipt',font=('Courier',20),bg='Gray50',fg='white')



def receipt():
    global coffee_selected
    global roast_selected
    global type_selected
    global weight_selected

    global price
    global total

    global address
    global comment
    global phoneNumber

    receiptTitle.place(x=1070,y=430)


    selected = Label(root,text=coffee_selected,font=('Courier',20),bg='Gray50',fg='white')
    selected.place(x=1070,y=460)

    roast = Label(root,text=roast_selected,font=('Courier',20),bg='Gray50',fg='white')
    roast.place(x=1070,y=490)

    type = Label(root,text=type_selected,font=('Courier',20),bg='Gray50',fg='white')
    type.place(x=1070,y=520)

    totalweight = (weight_selected,'x',str(total))
    weight = Label(root,text=totalweight,font=('Courier',20),bg='Gray50',fg='white')
    weight.place(x=1070,y=550)

    totalprice = (str(price),'THB')
    finalPrice = Label(root,text=totalprice,font=('Courier',20),bg='Gray50',fg='white')
    finalPrice.place(x=1070,y=580)

    def open_file():
        global imageFile
        root.filename = filedialog.askopenfilename(title='Select Image',filetypes=(('png files','*png'),('jpg files','*jpg'),('jpeg files','*jpeg')))
        imageFile = root.filename
        if root.filename == '':
            print('False Upload')
        else:
            uploadfile['text'] = 'Payment Slip Uploaded'

    uploadfile = Button(root, text='Upload Payment Slip', font=('Courier', 20), command=lambda: open_file())
    uploadfile.place(x=1070, y=610)

    def confirm_order():
        get_details()
        global email
        global imageFile
        stringprice = str(price)
        final_selection = coffee_selected+' '+roast_selected+' '+type_selected+' '+weight_selected+' '+str(total)+' '+stringprice+' '+email+' '+str(address)+' '+phoneNumber+' '+str(comment)
        receiptmail = coffee_selected+' '+roast_selected+' '+type_selected+' '+weight_selected+' '+str(total)+' bags for '+stringprice+' THB '+'Deliver to '+str(address)

        #actual password for account is not shared
        emailpassword = ''
        if address == '' or phoneNumber == '' or uploadfile['text'] == 'Upload Payment Slip':
            display_error()
        else:
            display_thank_you()

            msg = EmailMessage()
            msg['Subject'] = 'Order Recieved'
            msg['From'] = 'fairnistorder@gmail.com'
            msg['To'] = 'fairnistorder@gmail.com'
            msg.set_content(final_selection)

            with open(imageFile, 'rb') as f:
                file_data = f.read()
                file_type = imghdr.what(f.name)
                file_name = f.name

            msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

            with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                smtp.ehlo()
                smtp.starttls()
                smtp.ehlo()

                smtp.login('fairnistorder@gmail.com', emailpassword)

                subject = 'Order Recieved'
                userbody = receiptmail

                receiptmailmsg = f'Subject: {subject}\n\b{userbody}'
                smtp.sendmail('fairnistorder@gmail.com', email, receiptmailmsg)

                smtp.send_message(msg)
                display_thank_you()

    confirmOrder = Button(root, text='Confirm Order', font=('Courier', 20), command=confirm_order)
    confirmOrder.place(x=1070, y=710)


    def display_thank_you():
        thank = Label(root,text='Thank You For Ordering!',bg='Green',fg='white',font=('Courier',20))
        thank.place(x=1070,y=650)


    def display_error():
        error = Label(root, text='Missing Details', bg='Red', fg='white', font=('Courier', 20))
        error.place(x=1070, y=650)











root.mainloop()
