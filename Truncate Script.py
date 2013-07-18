#!/usr/bin/python

import csv
import MySQLdb

mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='',
    db='forjar')
cursor = mydb.cursor()

## create truncate query
cursor.execute('truncate csvtable')

mydb.commit() # execute truncate query
cursor.close()
mydb.close()
print "Table truncated."
