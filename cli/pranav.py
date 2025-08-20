print("Welcome To Our Grocery Store")
def signin():
    login=input("Enter your email/mobile : ").lower()
    #add code where this place looks up the user in database then asks for password and also look for their pass in user database
    #later add password decryption here
    answer=input("Enter password : ")
    print(f"Hi, {username}")


while True:
    user=int(input("\n1.Sign In(if already a user\n2.Sign Up for a new account\n3.Admin Login"
                   "\n4. quit the app here : "))
    if user==4:
        break
    elif user==1:
        signin()
