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
def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


#Login Functions

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
            clear_screen()
            admin_login()
            break
        elif opt == 2:
            clear_screen()
            sign_in()
            break
        elif opt ==3:
            clear_screen()
            log_in()
            break
        elif opt == 4:
            typing_effect("Thanks for using our app ")
            print("\n")
            typing_effect("Press enter to exit")
            input()
            break

        else:
            typing_effect("Please enter correct options......")
            print("\n")


def admin_login():
    print_banner("ADMIN")
    typing_effect("Hii, Sir Please Enter you id and password for login")
    print("\n")
    print("This is for only testing purpose  id:- abc pass:-2345")
    while True:
        typing_effect("Enter your ID:---\n",0.06)
        admin_id = input(":")
        typing_effect("Enter your PASS:---\n",0.06)
        admin_pass = input(":")
        if admin_id == "abc" and admin_pass == "2345":
            print("Welcome.., Press Enter to Continue")
            input()
            clear_screen()
            admin_page()
            break
        else:
            print("Wrong ID and PASS please try again ")

def admin_page():
    print_banner("ADMIN")
    msg = '''OPT:- 
1. View Users list
2. Remove User
3. Items List
4. View Bills history
5. Exit'''
    typing_effect(msg,0.04)
    while True:
        opt = int(input("\n:"))

        if opt == 1:
            clear_screen()
            print_banner("User List")
            print("Pandu sql ki list print krvani h yha pe tuje iska bhi alg se simple page bna na h fuck... ")
            #user_list_page()
            input()
        elif opt == 2:
            clear_screen()
            print_banner('Remove User')
            print("yha pe bhai sql use hoga tuje user remove ka krna h iska bhi page bna na pde ga fuckk....")
            #user_remove_page()
            input()
        elif opt ==3:
            clear_screen()
            print_banner("Items List")
            print("Items list...")
            input()
            #item list()
        elif opt==4:
            clear_screen()
            print_banner("Bills History")
            input()
            #bills_history page()
        elif opt ==5:
            clear_screen()
            user_login()
        else:
            print("Please Enter Valid options..")
        
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

