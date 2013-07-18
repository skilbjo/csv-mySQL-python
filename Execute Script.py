#!/usr/bin/python

import csv
import MySQLdb

mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='',
    db='forjar')
cursor = mydb.cursor()

query = ("SELECT * FROM csvtable ")
        # "WHERE hire_date BETWEEN %s AND %s")
		#hire_start = datetime.date(1999, 1, 1)
		#hire_end = datetime.date(1999, 12, 31)

cursor.execute(query) #(hire_start, hire_end))
result = cursor.fetchall()

for row in result:
	print row[0],"	", row[1],"	", row[2]


cursor.close()
mydb.close()
print "- - - - - - - - - - - - -"
print "Query executed."
print "Selected %s rows." % cursor.rowcount  
