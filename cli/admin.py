import sys
import time
import pyfiglet
import shutil
import os
import bcrypt as bcr
import sqlite3 as sq
from functions import * #shall import all the contets of fuctions here so i ca use to call them
# clrscr() #add later when you actually call it in main file or testing

con=sq.connect('info.db')
c=con.cursor()

def adminaccess():
    c.execute("""CREATE TABLE IF NOT EXISTS admin(
              adminid TEXT PRIMARY KEY,
              adminpass BLOB NOT NULL)""")
    userid='vercitty'
    salt=bcr.gensalt()
    passw="Iambatman"
    hashed=bcr.hashpw(passw.encode('utf-8'), salt)
    c.execute("INSERT OR REPLACE INTO admin VALUES (?, ?)", (userid, hashed))
        #align here
    while True:
        try:
            adminlogin=input("Enter Admin Name : ")
            adminlogin=adminlogin.lower()
            adminpass=input("Password : ")
            c.execute("SELECT adminpass FROM admin WHERE adminid=?", (adminlogin,))
            row=c.fetchone()
            passcheck=row[0]

            if bcr.checkpw(adminpass.encode('utf-8'), passcheck):
                while True:
                    # clrscr()
                    print_banner("Welcome Admin")
                    typing_effect("Choose what would you like to do today?"
                              "\n1. Items\n2. Users\n3. Bills\n4.Exit"
                              "\n Choose your choice : ") 
                    try:
                        adminchoice=int(input(""))

                        if adminchoice==4:
                            return #this return will exit both the loop and calling this function will into fuck with the program's execution in later stages
                        elif adminchoice==1:
                            items()

                        elif adminchoice==2:
                            listusers()

                        elif adminchoice==3:
                            print("Here are bills from users")
                            #print all the bills here
                        else:
                            print("invalid choice try again")
                    except Exception as e:
                        print("ERROR : ", e)
                        typing_effect("Exiting now")
            else:
                print("wrong password admin sahab")
                time.sleep(0)
                return False
        except Exception as e:
            typing_effect("Invalid Credentials\nTry Again\n")
            # clrscr()
            adminaccess()
            break
adminaccess()
