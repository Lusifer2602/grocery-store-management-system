import sqlite3 as sq
import sys
import time
import pyfiglet
import shutil
import os
import bcrypt as bcr
import time
from functions import *

con=sq.connect("info.db")
c=con.cursor()
clrscr()
def additems():
    while True:
        try:
            itemname=input("\nItem Name : ")
            itemname=itemname.lower()
            if itemname=='q':
                break
            itemprice=float(input("Price : "))
            if itemprice==404:
                break

            c.execute("INSERT OR REPLACE INTO items (item, price) VALUES (?, ?)", (itemname, itemprice))
            #INSERT OR REPLACE LOOKS UP IF THE VALUE ALREADY EXISTS AND THEN DELETS IT AND THEN INSERTS A NEW ONE TO THE SAME TABLE
            con.commit()
        except Exception as e:
            print("Error : ", e)
            break
def delitems():
    typing_effect("Enter 1 if you want to delete name by name\n"
             "2 if you want to delete all the items at once : ")
    delchoice=int(input(""))
    if delchoice==1:
        while True:
            try:
                tell=input("Enter the item to remove : ")
                tell=tell.lower()
                if tell=='q':
                    break
                c.execute("DELETE FROM items  WHERE item=?", (tell,))
                con.commit()
                continue
            except Exception as e:
                print("error :", e)

    elif delchoice==2:
        try:
            typing_effect("All items shall be purged now . . . ")
            c.execute("DELETE FROM items")
            con.commit()
            time.sleep(1)
            typing_effect("All items have beeen deleted successfully")
        except Exception as e:
            print("error :", e)
    else:
        print("invalid input")

def showitems():
    #indent here        
    c.execute("SELECT * FROM items")
    saman=c.fetchall()
    print("\nITEM LIST\n"
          "No.| Name | Price")
    for rows in saman:
        print(rows[0]," ", rows[1], rows[2])
    print('\n')
     


def items():
    print_banner("What do you want to do about the list")        
    c.execute("""CREATE TABLE IF NOT EXISTS items(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        item TEXT UNIQUE,
        price REAL NOT NULL)
        """)
    while True:
        try:
            typing_effect("\nEnter your choice"
                          "\n1. Add to Item List\n2. View previous Items\n3. Delete Items \n4. Close Program : ")

            choice=int(input(''))
        except:
            print("Invalid Input Try Again . . .")
            continue

        if choice==1: #edit/add items to the database
           additems() 

        elif choice==2:
            showitems()
            continue

        elif choice==3: #delete entries
            delitems()

        elif choice==4:
            print("Exiting Items window . . .")
            typing_effect("Goodbye")
            time.sleep(1)
            clrscr()
            break
        else:
            print("invalid input")
        clrscr()
items()
