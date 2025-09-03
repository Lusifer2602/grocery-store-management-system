from functions import * #shall import all the contets of fuctions here so i ca use to call them
# clrscr() #add later when you actually call it in main file or testing
con.connect('info.db')

def adminaccess():
    c.execute("""CREATE TABLE IF NOT EXISTS admin(
              adminid TEXT PRIMARY KEY,
              adminpass BLOB NOT NULL)""")
    userid='vercitty'
    salt=bcr.gensalt()
    passw="Iambatman"
    hashed=bcr.hashpw(passw.encode('utf-8'), salt)
    c.execute("INSERT OR REPLACE INTO admin VALUES (?, ?)", userid, hashed)

    typing_effect("Enter your credentials to login as admin\n")
    adminid=input("Enter your id : ")
    adminpass=input("Enter password : ")

    try:
        adminlogin=input("Enter Admin Name : ")
        adminlogin=adminlogin.lower()
        adminpass=input("Password : ")
        c.execute("SELECT * FROM admin WHERE admin=?", (,passw))
        row=c.fetchone()
        passcheck=row[0]

        if bcr.checkpw(adminpass.encode('utf-8'), passcheck):
            while True:
                clrscr()
                print_banner("Welcome Admin")
                typing_effect("Choose what would you like to do today?"
                          "\n1. Items\n2. Users\n3. Bills\n4.Exit"
                          "\n Choose your choice : ") 
                adminchoice=input("")

                if adminchoice==4:
                    break
                elif adminchoice==1:
                    items()        

                elif adminchoice==2:
                    listusers()

                elif adminchoice==3:
                    #print all the bills here
                else: print("Invalid Input")
