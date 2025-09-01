import sqlite3 as sq
import sys
import time
import pyfiglet
import shutil
import os
import bcrypt as bcr
import time
from functions import *
con=sq.connect('info.db')
c=con.cursor()

def items():
    while True:
        c.execute("""CREATE TABLE IF NOT EXISTS items(
        item text NOT NULL,
        price REAL NOT NULL
        """)
        
        try:
            choice=int(input("What do you want to do about the list"
                       "\n1. Edit Item List\n2. View previous Items\n3. Delete Items : "))
        except:
            print("Invalid Input Try Again . . .")
            continue

        if choice==1: #edit/add items to the database
            try:
                itemname=input("Item Name : ")
                itemname=itemname.lower()
                itemprice=float(input("Price : "))

                c.execute("INSERT OR REPLACE INTO items(item, price) VALUES (itemname, itemprice)")
                #INSERT OR REPLACE LOOKS UP IF THE VALUE ALREADY EXISTS AND THEN DELETS IT AND THEN INSERTS A NEW ONE TO THE SAME TABLE
                c.commit()
            except:
                print("Some error occured fuckoff now")
                continue

        elif choice==2:
            c.execute("SELECT * FROM items")
                saman=c.fetchall()
                print("ITEM LIST"
                      "Name    Price")
                for rows in saman:
                    print(row[0], row[1])
                print("\nWhat would you like to do next?")
                continue
        elif choice=3:
            choice2=("Enter 1 if you want to delete one by one\n"
                     "2 if you want to delete all the items at once")
            tell=input("Enter the item you want to remove from the table : ")
            c.execute("DELETE FROM 
            continue
        elif choice=4:
            print("Exiting Items window . . .")
            time.sleep(2)
            break
