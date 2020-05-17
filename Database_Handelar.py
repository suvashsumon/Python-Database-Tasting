"""
    this program is created for collecting mail address from a database and
    write mail addresses in a text file.
    dependency:
        1. database.db (sqlite database)
        2. mail.txt
"""

import sqlite3

con = sqlite3.connect("database.db")
cur = con.cursor()

f = open("mail.txt",'a')
cur.execute("SELECT \"mail\" FROM Contacts")
row = cur.fetchone()

while row is not None:
    print("---------------------------------------------------------")
    print("{0}".format(row[0]))
    f.write(row[0]+'\n')
    row = cur.fetchone()
print("---------------------------------------------------------")
con.commit()
f.close()
