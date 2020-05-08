import sqlite3

con = sqlite3.connect("CSE_Sompurok_27_RU.db")
cur = con.cursor()

f = open("mail.txt",'a')
cur.execute("SELECT \"Mail\" FROM Contacts")
row = cur.fetchone()

while row is not None:
    print("---------------------------------------------------------")
    print("{0}".format(row[0]))
    f.write(row[0]+'\n')
    row = cur.fetchone()
print("---------------------------------------------------------")
con.commit()
f.close()
