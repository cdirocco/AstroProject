#!/usr/bin/python

import sqlite3
from AddingObjectInterface import *
sqlstatement = addObject()

connection = sqlite3.connect("astroProject.db")


# delete the table
"""
connection.execute('DROP TABLE celestialEntities;')

# create the table
connection.execute('''
    CREATE TABLE celestialEntities
    (id INTEGER PRIMARY KEY AUTOINCREMENT, 
    Name TEXT NOT NULL, 
    Kind TEXT NOT NULL, 
    Radius REAL NOT NULL, 
    Mass REAL NOT NULL, 
    Redshift REAL NOT NULL);
''')
"""

# insert a row
connection.execute('''
    %s
''' % sqlstatement )    

# commit entries to database table
connection.commit()


# a cursor holds returned values from a query
cursor = connection.execute('SELECT * FROM celestialEntities;')

for row in cursor:
    print "ID", row[0]
    print "Name", row[1]
    print "Kind", row[2]
    print "Mass", row[3]
    print "Radius", row[4]
    print "Redshift", row[5]

cursor.close()    
connection.close()