import sys
import time
import pyfiglet
import shutil
import os

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

os.system("cls")

print_banner("NEW   USER")

typing_effect("Press Enter to Continue.....", 0.05)
input()
os.system("cls")

new_user_name = input("Enter your Name\n:")
while True:
    new_user_email = input("Enter you Email \n:")
    if new_user_email.endswith("@gmail.com"):
        break
    else:
        print("Please Enter Valid Email....")
while True:
    new_user_pass = input("Enter your Password\n:")
    if len(new_user_pass) <8:
        print("Please Enter Atleast 8 Character ")
    else:
        break
os.system("cls")

typing_effect(f"Hi {new_user_name}",0.05)
typing_effect(f"Please Verify the Information:- ")