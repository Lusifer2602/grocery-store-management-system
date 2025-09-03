import sys
import time
import pyfiglet
import shutil
import os
import bcrypt
import sqlite3 as sq

con=sq.connect('info.db')
c=con.cursor()

def typing_effect(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)   
        sys.stdout.flush()       
        time.sleep(delay) 

def print_banner(text):
    columns = shutil.get_terminal_size().columns
    banner = pyfiglet.figlet_format(text)
    for line in banner.split("\n"):
        print(line.center(columns))
def clrscr():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


#Login Functions

def user_login():
    clrscr()
    print_banner("GROCERRY MANAGMENT SYSTEM")
    typing_effect("Welcome.....")
    print("\n")
    msg = """Hii Please select From given options:--
1. Sign Up (if already a user)
2. Sign In (for new account)
3. Admin
4. Exit
"""
    typing_effect(msg,0.06)
    while True:
        opt = int(input(":"))
        if opt ==1:
            clear_screen()
            signup()
            break
        elif opt == 2:
            clear_screen()
            login()
            break
        elif opt ==3:
            clear_screen()
            admin()
            break
        elif opt == 4:
            typing_effect("Thanks for using our app ")
            time.sleep(1)
            break

        else:
            typing_effect("Please enter correct options......")
            print("\n")


def admin():

def sign_in ():
    clear_screen()
    print_banner("NEW   USER") 

    typing_effect("Press Enter to Continue.....", 0.05)
    input()
    clear_screen()

    new_user_name = input("Enter your Name\n:")
    while True:
        new_user_email = input("Enter you Email \n:")
        if new_user_email.endswith("@gmail.com") and len(new_user_email)>len("@gmail.com"):
            break
        else:
                print("Please Enter Valid Email....")
    while True:
        new_user_pass = input("Enter your Password\n:")
        if len(new_user_pass) <8:
            print("Please Enter Atleast 8 Character ")
        else:
            break
            clear_screen()
    hii_msg = f'Hi {new_user_name}\n'
    info = f"""
    Name > {new_user_name} 
    Email > {new_user_email}
    Password > {new_user_pass} """

    typing_effect(hii_msg,0.05)
    typing_effect("Please Verify the Information:-",0.05)
    typing_effect(info,0.06)
    return [new_user_email,new_user_name,new_user_pass]




def log_in():
    print_banner("LOGIN")
    typing_effect("Hi, Welcome Back..")

    print("Please Enter Login Id & Pass")
    input("Enter to exit for now")

def additems():
    while True:
        try:
            itemname=input("\nItem Name : ")
            itemname=itemname.lower()
            if itemname=='q':
                break
            itemprice=float(input("Price : "))

            c.execute("INSERT OR REPLACE INTO items (item, price) VALUES (?, ?)", (itemname, itemprice))
            #INSERT OR REPLACE LOOKS UP IF THE VALUE ALREADY EXISTS AND THEN DELETS IT AND THEN INSERTS A NEW ONE TO THE SAME TABLE
            con.commit()
        except ValueError:
            print("\nStr in price detected, exiting adding items")
            time.sleep(1)
            clrscr()
            break
        except Exception as e:
            print("Error : ", e)
            break

def delitems(): #for admin
    typing_effect("Enter 1 if you want to delete name by name\n"
             "2 if you want to delete all the items at once : ")
    delchoice=int(input(""))
    if delchoice==1:
        while True:
            try:
                tell=input("Enter the item to remove : ")
                tell=tell.lower()
                if tell=='q':
                    break
                c.execute("DELETE FROM items  WHERE item=?", (tell,))
                con.commit()
                continue
            except Exception as e:
                print("error :", e)

    elif delchoice==2:
        try:
            typing_effect("All items shall be purged now . . . ")
            c.execute("DELETE FROM items")
            con.commit()
            time.sleep(1)
            typing_effect("All items have beeen deleted successfully\n")
        except Exception as e:
            print("error :", e)
    else:
        print("invalid input")

def showitems(): #for both users and admin
    #indent here        
    c.execute("SELECT * FROM items")
    saman=c.fetchall()
    print("\nITEM LIST\n"
          "No.| Name | Price")
    for rows in saman:
        print(rows[0]," ", rows[1], rows[2])
    print('\n')

#call this one for admin
def items():
    clrscr()
    print_banner("What do you want to do about the list")        
    c.execute("""CREATE TABLE IF NOT EXISTS items(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        item TEXT UNIQUE,
        price REAL NOT NULL)
        """)
    while True:
        try:
            typing_effect("\nEnter your choice"
                          "\n1. Add to Item List\n2. View previous Items\n3. Delete Items \n4. Close Program : ")

            choice=int(input(''))
        except:
            print("Invalid Input Try Again . . .")
            continue

        if choice==1: #edit/add items to the database
           additems() 

        elif choice==2:
            showitems()
            continue

        elif choice==3: #delete entries
            delitems()

        elif choice==4:
            print("Exiting Items window . . .")
            typing_effect("Goodbye")
            time.sleep(1)
            clrscr()
            break
        else:
            print("invalid input try again")

def listusers():
    c.execute("SELECT * FROM users")
    user=c.fetchall()
    print("username  mail ")
    for users in user:
        print(users[0], users[1])
