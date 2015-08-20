#!/usr/bin/python
# -*-coding:Utf-8 -*


#import Adafruit_BMP.BMP085 as BMP085
import sqlite3
import os

#Connection à la bdd
database_name = "meteolog.db"
db_connection = sqlite3.connect(database_name)
db_cursor = db_connection.cursor()
try:
    db_cursor.execute('CREATE TABLE IF NOT EXISTS logging (datetime TIMESTAMP, temp FLOAT, pressure INT)')
except sqlite3.OperationalError:
    print ('le fichier est corompu ou n\'est pas la bdd')



#initialise un objet capteur
#sensor = BMP085.BMP085()


#print 'Temperature = {0:0.3f} *C'.format(sensor.read_temperature())
#0|datetime|TIMESTAMP|0||0
#1|temp||0||0
#2|FLOAT||0||0
#3|pressure|INT|0||0