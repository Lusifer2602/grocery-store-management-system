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
# sign in page 
def sign_in ():
    os.system("cls")

    print_banner("NEW   USER") 

    typing_effect("Press Enter to Continue.....", 0.05)
    input()
    os.system("cls")

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
    os.system("cls")
    hii_msg = f'Hi {new_user_name}\n'
    info = f"""
    Name > {new_user_name} 
    Email > {new_user_email}
    Password > {new_user_pass} """

    typing_effect(hii_msg,0.05)
    typing_effect("Please Verify the Information:-",0.05)
    typing_effect(info,0.06)
    return [new_user_email,new_user_name,new_user_pass]
# User_login page
def user_login():
    print_banner("GROCERRY MANAGMENT SYSTEM")
    typing_effect("Welcome.....")
    print("\n")
    msg = """Hii Please select From given options:--
1. Admin Login
2. Sign In 
3. Log In 
4. Exit
"""
    typing_effect(msg,0.06)
    while True:
        opt = int(input(":"))
        if opt ==1:
            # admin_pg()
            print("admin page temp....")
            break
        elif opt == 2:
            sign_in()
            break
        elif opt ==3:
            # log_in()
            print("Log in page temp......")
            break
        elif opt == 4:
            typing_effect("Thanks for using our app ")
            print("\n")
            typing_effect("Press enter to exit")

        else:
            typing_effect("Please enter correct options......")
            print("\n")