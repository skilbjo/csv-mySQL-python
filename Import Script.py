#!/usr/bin/python

import csv
import MySQLdb

mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='',
    db='forjar')
cursor = mydb.cursor()

## read csv
csv_data = csv.reader(file('CSV_Import.csv','rU'))

## create insertion query
for row in csv_data:
    cursor.execute('INSERT INTO csvtable(sname ,sclass)' \
            'VALUES(%s, %s)',  row)

mydb.commit() ## execute insertion query
cursor.close()
mydb.close()
print "Import to MySQL is over"
