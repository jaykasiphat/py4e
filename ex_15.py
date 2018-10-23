import sqlite3
import re

'''
    This program will read the mailbox data (mbox.txt) and count the number of email
    messages per organization (i.e. domain name of the email address) using a database with
    the following schema to maintain the counts.
'''

conn = sqlite3.connect('ex15.sqlite') #creates a connection object that represents the db
cur = conn.cursor() #creates a cursor object

cur.execute('''DROP TABLE IF EXISTS Counts''')
cur.execute('''CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1):
    fname = 'mbox.txt'
fhand = open(fname)
for line in fhand:
    if line.startswith('From '):
        ls = line.split()
        email = ls[1]
        mail = re.findall('@(.+)', email)
        org = mail[0]
        cur.execute('''SELECT count FROM Counts WHERE org = ?''', (org,))
        row = cur.fetchone()
        if row is None:
            cur.execute('''INSERT INTO Counts (org, count) VALUES (?, 1)''', (org,))
        else:
            cur.execute('''UPDATE Counts SET count = count + 1 WHERE org = ?''', (org,))
conn.commit()

sqlstr = '''SELECT org, count FROM Counts ORDER BY count DESC'''

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
