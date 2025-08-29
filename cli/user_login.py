from function import *

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