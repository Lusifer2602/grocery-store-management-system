import sqlite3 as sq
import sys
import time
import pyfiglet
import shutil
import os
userdata=None
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
con=sq.connect('info.db')
c=con.cursor()

def signup():
    global userdata
    os.system("clear")

    print_banner("Sign Up for\nNew Account") 

    typing_effect("Press Enter to Continue.....", 0.05)
    input()

    new_user_name = input("Enter your Name : ")
    while True:
        new_user_email = input("Enter you Email :")
        if new_user_email.endswith("@gmail.com") and len(new_user_email)>len("@gmail.com"):
            break
        else:
                print("Please Enter A Valid Email....")
    while True:
        passw= input("Enter New Password :")
        
        if len(passw) <8:
            print("Please Enter Atleast 8 Characters ")
        else:
            break

    os.system("clear")
    hii_msg = f'Hi {new_user_name}\n'
    info = f"""
    Name > {new_user_name} 
    Email > {new_user_email}
    Password > {passw} """

    typing_effect(hii_msg,0.05)
    typing_effect("Please Verify Your Information : \n",0.05)
    typing_effect(info,0.04)
    choice=input("\nEnter 'y' if the information is correct\nand 'n' to re-setup your account : ").lower()
    if choice=='y' or choice == 'yes':
        c.execute("""CREATE TABLE IF NOT EXISTS users(
              name TEXT,
              mail text PRIMARY KEY,
              passw 
              )""")
        print("User Added Succesfully!")
        #now start a session from the same id 
    userdata=[new_user_email, new_user_name, passw]
    return [new_user_email,new_user_name,passw]
signup()
