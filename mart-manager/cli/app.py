import sys
import time
import pyfiglet
import shutil
import os
import bcrypt as bcr
import sqlite3 as sq

# --- Initialization & Globals ---
con = sq.connect('info.db')
c = con.cursor()
userdata = None # To later store and start a user's session

# Ensure tables exist
c.execute("""CREATE TABLE IF NOT EXISTS users(
              name TEXT,
              mail text PRIMARY KEY,
              passw BLOB NOT NULL
              )""")
c.execute('''CREATE TABLE IF NOT EXISTS items(
              id INTEGER PRIMARY KEY AUTOINCREMENT, 
              item TEXT UNIQUE, 
              price REAL NOT NULL
              )''')
con.commit()

# --- Utility Functions ---
def typing_effect(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)   
        sys.stdout.flush()       
        time.sleep(delay) 

def print_banner(text):
    columns = shutil.get_terminal_size().columns
    try:
        banner = pyfiglet.figlet_format(text)
        for line in banner.split("\n"):
            print(line.center(columns))
    except pyfiglet.FontNotFound:
        print(text.center(columns))

def clrscr():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

# --- User Authentication (Your Code) ---

def login():
    global userdata
    clrscr()
    print_banner("Login To Your\nAccount")
    
    while True:
        print("\n(Type 'q' to go back to main menu)")
        mail = input("Enter your mail : ").lower().strip()
        if mail == 'q': return False
        passw = input("Enter your password : ")
        
        try: 
            c.execute("SELECT passw FROM users WHERE mail=?", (mail,))
            auth = c.fetchone()
            
            if auth:
                hashed = auth[0]
                if bcr.checkpw(passw.encode('utf-8'), hashed): 
                    print("\n[SUCCESS] LOGIN SUCCESSFUL ! ! !")
                    c.execute("SELECT name FROM users WHERE mail=?", (mail,))
                    row = c.fetchone()
                    name = row[0]
                    print(f"Hi, {name}")
                    userdata = [name, mail]
                    time.sleep(1)
                    return True
                else:
                    print("\n[Error] Wrong password. Try again.")
            else:
                print("\n[Error] This mail doesn't exist. Try again.")
        except Exception as e:
            print(f"\n[Error] An error occurred: {e}")

def signup():
    global userdata
    clrscr()
    print_banner("Sign Up for\nNew Account") 

    typing_effect("Press Enter to Continue.....", 0.05)
    input()

    name = input("Enter your Name : ").strip()
    
    while True:
        mail = input("Enter you Email : ").lower().strip()
        if mail.endswith("@gmail.com") and len(mail) > len("@gmail.com"):
            break
        else:
            print("[Error] Please Enter A Valid @gmail.com Email....\n")
            
    while True:
        passw = input("Enter New Password : ")
        if len(passw) < 8:
            print("[Error] Please Enter Atleast 8 Characters\n")
        else:
            break
    
    clrscr()
    hii_msg = f'Hi {name}\n'
    info = f"""
    Name > {name} 
    Email > {mail}
    Password > {'*' * len(passw)} """ # Obscured password for security display

    typing_effect(hii_msg, 0.05)
    typing_effect("Please Verify Your Information : \n", 0.05)
    typing_effect(info)
    
    while True:
        choice = input("\n\nEnter 'y' if the information is correct\nand 'n' to re-setup your account : ").lower().strip()

        if choice in ['y', 'yes']: 
            try:
                salt = bcr.gensalt()
                hashed = bcr.hashpw(passw.encode('utf-8'), salt)
                
                c.execute("INSERT INTO users (name, mail, passw) VALUES (?, ?, ?)", (name, mail, hashed))
                con.commit()
                typing_effect("\n[Success] You've been added to the database!\nLogin to your account now\n")
                time.sleep(1.5)
                return True
            except sq.IntegrityError:
                print("\n[Error] This user is already in the database. Try signing up with another mail.")
                time.sleep(1.5)
                return False
        elif choice in ['n', 'no']:
            typing_effect("\nAlright no issues,\nlets setup your account again\n")
            time.sleep(1.5)
            return False
        else:
            print("Invalid Input. Try again.")

# --- Dashboard & Shopping ---

def user_dashboard():
    global userdata
    while True:
        clrscr()
        print_banner(f"Welcome {userdata[0]}")
        print("1. View Items")
        print("2. Buy Item")
        print("3. Logout")
        
        choice = input("\nEnter choice: ").strip()
        
        if choice == '1':
            showitems()
            input("Press Enter to return...")
        elif choice == '2':
            showitems()
            buy_item = input("Enter the name of the item you want to buy (or 'q' to cancel): ").lower().strip()
            if buy_item != 'q':
                c.execute("SELECT price FROM items WHERE item=?", (buy_item,))
                item_data = c.fetchone()
                if item_data:
                    print(f"\n[Success] You purchased {buy_item.title()} for ${item_data[0]:.2f}!")
                else:
                    print("\n[Error] Item not found.")
                input("\nPress Enter to return...")
        elif choice == '3':
            userdata = None
            print("\nLogging out...")
            time.sleep(1)
            break
        else:
            print("Invalid input.")
            time.sleep(1)

# --- Admin & Item Functions ---

def additems():
    while True:
        try:
            itemname = input("\nItem Name (or 'q' to quit): ").lower().strip()
            if itemname == 'q': break
            itemprice = float(input("Price: $"))

            c.execute("INSERT OR REPLACE INTO items (item, price) VALUES (?, ?)", (itemname, itemprice))
            con.commit()
            print(f"[Success] {itemname.title()} added.")
        except ValueError:
            print("\n[Error] Invalid price.")
        except Exception as e:
            print("Error: ", e)
            break

def delitems():
    typing_effect("\n1. Delete name by name\n2. Delete all items\nChoice: ")
    try:
        delchoice = int(input(""))
        if delchoice == 1:
            while True:
                tell = input("Enter item to remove (or 'q'): ").lower().strip()
                if tell == 'q': break
                c.execute("DELETE FROM items WHERE item=?", (tell,))
                con.commit()
                print(f"[Success] {tell.title()} removed.")
        elif delchoice == 2:
            c.execute("DELETE FROM items")
            con.commit()
            print("[Success] All items deleted.")
    except ValueError:
        print("Invalid input")

def showitems():
    c.execute("SELECT * FROM items")
    saman = c.fetchall()
    print("\n--- ITEM LIST ---")
    print(f"{'No.':<5} | {'Name':<15} | {'Price':<10}")
    print("-" * 35)
    for rows in saman:
        print(f"{rows[0]:<5} | {rows[1].title():<15} | ${rows[2]:<9.2f}")
    print('\n')

def items_menu():
    while True:
        clrscr()
        print_banner("Manage Items")
        print("1. Add Items\n2. View Items\n3. Delete Items\n4. Back")
        try:
            choice = int(input('\nEnter choice: '))
            if choice == 1: additems()
            elif choice == 2: 
                showitems()
                input("Press Enter...")
            elif choice == 3: delitems()
            elif choice == 4: break
        except ValueError:
            print("Invalid Input.")

def listusers():
    c.execute("SELECT name, mail FROM users")
    users = c.fetchall()
    print("\n--- USERS ---")
    for u in users:
        print(f"Name: {u[0]:<10} | Email: {u[1]}")
    input("\nPress Enter...")

def adminaccess():
    c.execute("""CREATE TABLE IF NOT EXISTS admin(adminid TEXT PRIMARY KEY, adminpass BLOB NOT NULL)""")
    salt = bcr.gensalt()
    hashed = bcr.hashpw(b"Iambatman", salt)
    c.execute("INSERT OR REPLACE INTO admin VALUES (?, ?)", ('vercitty', hashed))
    con.commit()
    
    clrscr()
    print_banner("Admin Login")
    adminlogin = input("Admin Name: ").lower().strip()
    adminpass = input("Password: ")
    
    c.execute("SELECT adminpass FROM admin WHERE adminid=?", (adminlogin,))
    row = c.fetchone()
    
    if row and bcr.checkpw(adminpass.encode('utf-8'), row[0]):
        while True:
            clrscr()
            print_banner("Admin Panel")
            print("1. Items\n2. Users\n3. Exit")
            try:
                adminchoice = int(input("\nChoice: "))
                if adminchoice == 1: items_menu()
                elif adminchoice == 2: listusers()
                elif adminchoice == 3: break
            except ValueError:
                print("Invalid input.")
    else:
        print("\n[Error] Invalid admin credentials.")
        time.sleep(1.5)

# --- Main Flow ---

def main_menu():
    while True:
        clrscr()
        print_banner("GROCERY SYSTEM")
        print("\n1. Sign Up")
        print("2. Sign In")
        print("3. Admin")
        print("4. Exit")
        
        try:
            opt = int(input("\n: "))
            if opt == 1:
                while not signup(): # Loops back to main menu if user aborts or fails
                    pass 
            elif opt == 2:
                if login():
                    user_dashboard()
            elif opt == 3:
                adminaccess()
            elif opt == 4:
                typing_effect("Thanks for using our app!\n")
                break
            else:
                print("Incorrect option.")
                time.sleep(1)
        except ValueError:
            print("Please enter a valid number.")
            time.sleep(1)

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\n\nExiting...")
        sys.exit()
