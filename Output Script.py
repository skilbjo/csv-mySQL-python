#!/usr/bin/python

import csv
import MySQLdb

mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='',
    db='forjar')
cursor = mydb.cursor()

## query
query = ("SELECT * FROM csvtable ")
cursor.execute(query)

### write to csv file
csv_writer = csv.writer(open("CSV_Output.csv", "wt")) # create csv
csv_writer.writerow([i[0] for i in cursor.description]) # write headers
csv_writer.writerows(cursor) # write records
del csv_writer # close csv file

cursor.close()
mydb.close()
print "Query executed."
print "Wrote %s rows to csv." % cursor.rowcount  
