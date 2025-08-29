# Module Area
import sys
import time
import pyfiglet
import shutil
import os
# Function Area

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


# Code Area

os.system("cls")

print_banner("Welcome to our GMS\nlet's setup your account") 

typing_effect("Press Enter to Continue.....", 0.05)
input()
os.system("cls")

new_user_name = input("Enter your Name : ")
while True:
    new_user_email = input("Enter you Email : ")
    if new_user_email.endswith("@gmail.com"):
        break
    else:
        print("Please Enter Valid Email....")
while True:
    new_user_pass = input("Enter Password :")
    if len(new_user_pass) <8:
        print("Please Enter Atleast 8 Characters ")
    else:
        break
os.system("cls")
typing_effect("Please revise your info before we save it to the database"
              "\nPress y moving ahead & n to re-setup your account : ")
input()
info = f"""
Name > {new_user_name} 
Email > {new_user_email}
Password > {new_user_pass} """

typing_effect(hii_msg,0.05)
typing_effect("Please Verify the Information:-",0.05)
typing_effect(info,0.06)
print("\n")
