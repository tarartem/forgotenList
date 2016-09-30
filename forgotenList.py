import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

goods = {}
guests = {}
tasks = {}

# Function add guest and their emails to the guests list
def addGuest():
    print("Please enter name of your guests OR press 'n' to quit ")
    while True:
        guest = input("Guest name: ")
        if guest == "n":
            break
        email = input("Guest email: ")
        if email == "n":
            break
        else:
            guests[guest]=email

# Here we are create list of the items that we forget to bye
def newItem():
    print("Input goods that you want to add and quantity OR press 'n' to quit ")
    while True:
        item = input("Goods name: ")
        if item == "n":
            break
        itemQuantity = input("How many pieces: ")    
        if itemQuantity == 'n':
            break
        else:
            goods[item]=itemQuantity

# Function show goods that we have forgett to bye
def showGoods():
    print("Here is what we need:")
    for key in goods:
        print ("--------------")
        print ("| "+goods[key]+" | "+key+" |")
    print("--------------")

# Here we are assigning task to chosen guest from the list that we have create before 
def assignee():
    print("Here are invited persons: ")
    for key in guests:
        print(key)
    guest = input("Input guests name you want to assigne a task (Please use lowercase charracters) ")
    print ("Ok, we need: ")
    for key in goods:
        print (goods[key]+" of "+key)
    print("What you want to assign to "+ guest+" ?")
    item = input("Input goods name listed abow ")
    for i in range (len(goods)):
        tasks[guest] = {item:goods[item]}
    print("Well, "+ guest+ " please bring us "+goods[item]+" of "+ item+".")
    send_message(guest, item)
    print('Message was successfuly sent to '+guest)

    print ("Choose next guest ")
    guest = input("Input guests name you want to assigne a task (Please use lowercase charracters) ")
    send_message(guest, item)

# Function that create email message and send it to your guest
def send_message(guest, item):
    recipient = guests[guest]
    sender_lgn = 'tarartem@gmail.com'
    sender_pwd = 'Goo979198033'
    subj = 'Task from Artem'
    email_body = 'Hello, ' + guest + '! '+'\n' + 'Unfortunately we have forgoten to bye some staff for our festive table. Would you be so kinde to take with you following goods: ' + '\n' + goods[item] + ' of ' + item 

    msg = MIMEMultipart('alternative')
    smtpsrvr = smtplib.SMTP('smtp.gmail.com', 587)
    smtpsrvr.ehlo()
    smtpsrvr.starttls()
    smtpsrvr.ehlo()
    smtpsrvr.login(sender_lgn, sender_pwd)

    msg['Subject'] = subj
    msg['From'] = sender_lgn
    body = email_body

    content = MIMEText(body, 'plain')
    msg.attach(content)
    smtpsrvr.sendmail(sender_lgn, recipient, msg.as_string())
    smtpsrvr.close()

# Main program function
def main():
        addGuest()
        newItem()
        showGoods()
        assignee()

main()
