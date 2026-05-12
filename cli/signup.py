import sqlite3 as sq
import sys
import time
import pyfiglet
import shutil
import os
import bcrypt as bcr
import time
from functions import *

userdata=None
con=sq.connect('info.db')
c=con.cursor()

def signup():
    global userdata
    os.system("clear")

    print_banner("Sign Up for\nNew Account") 

    typing_effect("Press Enter to Continue.....", 0.05)
    input()

    name = input("Enter your Name : ")
    while True:
        mail = input("Enter you Email :").lower()
        mail=mail.lower()
        if mail.endswith("@gmail.com") and len(mail)>len("@gmail.com"):
            break
        else:
                print("Please Enter A Valid Email....")
    while True:
        passw= input("Enter New Password :")
        
        if len(passw) <8:
            print("Please Enter Atleast 8 Characters")
        else:
            break
    
    os.system("clear")
    hii_msg = f'Hi {name}\n'
    info = f"""
    Name > {name} 
    Email > {mail}
    Password > {passw} """

    typing_effect(hii_msg,0.05)
    typing_effect("Please Verify Your Information : \n",0.05)
    typing_effect(info)
    while True:
        choice=input("\nEnter 'y' if the information is correct\nand 'n' to re-setup your account : ")
        choice=choice.lower()

        if choice=='y' or choice == 'yes': 
           try:
               salt=bcr.gensalt()
               hashed=bcr.hashpw(passw.encode('utf-8'), salt)
               c.execute("""CREATE TABLE IF NOT EXISTS users(
                      name TEXT,
                      mail text PRIMARY KEY,
                      passw  BLOB NOT NULL
                      )""")
               c.execute("INSERT INTO users (name, mail, passw) VALUES (?, ?, ?)", (name, mail, hashed))
               con.commit()
               typing_effect("You've been added to the database!\n Login to your account now\n")

               return [name, mail, hashed]
               # login()
               break
           except:
               print("\nThis user is already in the database try signing up with another mail")
               signup()
               break
        elif choice=='n' or choice =='no':
            typing_effect("Alright no issues,\nlets setup your account again")
            time.sleep(2)
            signup()
            return
        else:
            typing_effect("Invalid Input")
            continue

signup()
