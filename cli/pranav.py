print("Welcome To Our Grocery Store")
def order():
    
def signin():
    login=input("Enter your email/mobile : ").lower()
    #add code where this place looks up the user in database then asks for password and also look for their pass in user database
    #later add password decryption here
    answer=input("Enter password : ")
    print(f"Hi, {username}")
    choice=int(input("What would you like today?"
           "\n1.Order new items\n2.View your previous orders\n3.Just go through items in our stock : "))
    if choice==1:
        order()


while True:
    user=int(input("\n1.Sign In(if already a user\n2.Sign Up for a new account\n3.Admin Login"
                   "\n4. quit the app here : "))
    if user==4:
        break
    elif user==1:
        signin()
