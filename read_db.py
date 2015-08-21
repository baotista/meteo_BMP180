#!/usr/bin/env python
# -*-coding:Utf-8 -*

import cgi
import cgitb
import sqlite3
import os

# enable tracebacks of exceptions
cgitb.enable()

#acquerir les data et les formater
#[(u'2015-08-21 08:26:02.011808', 23.1, 1019),
#['Year', 'Sales', 'Expenses'],
#
#

def print_table(donnees):
    data_lines=[]
    result=""
    donnees.strip("[")
    donnees.strip("]")
    donnees.strip("(u")
    result = donnees
    return result




# print an HTTP header
#
print "Content-type: text/html"
print
with open('top_page.html') as f:
  print f.read()

#Connection à la bdd
database_name = "/home/pi/python/meteo_BMP180/meteolog.db"
db_connection = sqlite3.connect(database_name)
db_cursor = db_connection.cursor()

db_cursor.execute("SELECT * FROM logging")
all_rows = db_cursor.fetchall()

with open('page.html') as f:
  print f.read()

print (print_table(all_rows))


db_connection.close()
with open('bpage.html') as f:
  print f.read()
