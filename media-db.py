# Copyright 2017 - Adam Cripps adam@monkeez.org


import sqlite3
import sys

def createDatabase(dbname):
    print ("You want to create a database called ", dbname)
    con = sqlite3.connect(dbname)
    print ("Created a database called ", dbname)
    return

def quitme(status):
    if status == True:
        print("Goodbye")
        sys.exit(0)
    else:
        MenuItem()

def MenuItem():
    menu = {}
    menu['1']="Open Database"
    menu['2']="Save Database"
    menu['3']="New Database"
    menu['4']="Quit program"
    while True:
        options=menu.keys()
        sortedoptions = sorted(options)
        for entry in sortedoptions:
            print (entry, menu[entry])

        selection = input("Please Select:")
        if selection=='1':
            print ("open")
        elif selection=='2':
            print ("save")
        elif selection=='3':
            print ("create")
            dbname = input("Please name the database: ")
            createDatabase(dbname)
        elif selection=='4':
            confirm = input("You want to quit? Y to confirm: ")
            if confirm == "Y":
                quitme(True)
                break
            else:
               MenuItem()
class db:
    def __init__(self):
      print ("db created")  
      MenuItem()

if __name__ == "__main__":
    mydb = db() 
