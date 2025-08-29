from function import *
print_banner("GROCERRY MANAGMENT SYSTEM")
typing_effect("Welcome.....")
print("\n")
msg = """Hii Please select From given options:--
1. Admin Login
2. Sign In 
3. Log In 
"""
typing_effect(msg,0.06)
opt = int(input(":"))
if opt ==1:
    sign_in()