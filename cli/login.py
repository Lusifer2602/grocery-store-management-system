import sqlite3 as sq
import sys
import time
import pyfiglet
import shutil
import os
import bcrypt as bcr
import time
from functions import *
con=sq.connect('info.db')
c=con.cursor()

userdata=None #to later store and start a user's session for their purchase, etc

os.system("clear")
print_banner("Login To Your\nAccount")

input()
def login():
    while True:
        mail=input("Enter your mail : ")
        mail=mail.lower()
        passw=input("Enter your password : ")
        global userdata
        
        try : #check authentication here
            c.execute("SELECT passw FROM users WHERE mail=?", (mail,))
            auth=c.fetchone()
            hashed=auth[0]
            
            if bcr.checkpw(passw.encode('utf-8'), hashed): #for checking password
                print("LOGIN SUCCESSFUL ! ! !")
                c.execute("SELECT name FROM users WHERE mail=?", (mail,))
                row=c.fetchone()
                name=row[0]
                print(f"Hi, {name}")
                userdata=[name, mail]
                #call function to order items
                return True
                break
            else:
                print("Wrong authentication try again")
                login()
            break

        except :
            print("This mail doesn't exist try again")
            login()
            break

login()

