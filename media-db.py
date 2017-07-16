# Copyright 2017 - Adam Cripps adam@monkeez.org
# Distributed under the GPL license Version 2 June 1991 - Please see LICENSE file for more information about distribution rights. 

import sqlite3
import sys
import os.path
from datetime import date, datetime
from time import gmtime, strftime
def openDB(dbname):
    filename = dbname + '.db'
    con = sqlite3.connect(filename, detect_types=sqlite3.PARSE_DECLTYPES)
    #mycursor = con.cursor()
    #con = sqlite3.Connection(sqlite3.connect(filename))
    return

    
class Item:
    def __init__(self):
        id = 0 
        self.date = time.asctime()
        self.title = input("Title: ")
        self.location = input("Location: ")
        self.mediatype = input("Media type: ")
        return self
    
def createCursor(db):
    cursor = db.cursor()
    return cursor
        
def additem(dbname):
    db = sqlite3.connect(dbname + '.db', detect_types=sqlite3.PARSE_DECLTYPES)
    print ("we've opened a db ", db)
    mycursor = db.cursor()
    # mycursor = createCursor(db)
    # newitem = Item()
    idnumber = 0 
    #writedate = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    writedate = datetime.now()
    title = input("Title: ")
    location = input("Location: ")
    mediatype = input("Media type: ")
    print (writedate)
    #stringdate = str(date)
    mycursor.execute("INSERT INTO "+dbname+" VALUES (?, ?, ?, ?, ?)", (str(idnumber), writedate, title, location, mediatype))
    db.commit()
    db.close()

def createDatabase(dbname):
    print ("You want to create a database called ", dbname)
    dbfilename = dbname+'.db'
    con = sqlite3.connect(dbfilename, detect_types=sqlite3.PARSE_DECLTYPES)
    print ("Created a database called ", dbname)
    if os.path.isfile(dbname) == True:
        print ("That database already exists - try again ")
        newname = input("Choose a new database name: ")
        createDatabase(newname)
    else:
        mycursor = con.cursor()
        mycursor.execute("CREATE TABLE "+dbname+" (id, date DATE, title, location, mediatype)")
        con.commit()
        con.close()
        wherenext = input("Add items to this database? y/n ")
        if wherenext =="y":
            additem(dbname)
        else:
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
