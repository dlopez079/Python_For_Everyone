# Import the SQLite library to enable SQLite functionality
import sqlite3

# Establish connection with the org database.  If the database does not exist, it will create the database.
conn = sqlite3.connect('orgdb.sqlite')

# Establish a handle for the connection.
cur = conn.cursor()

# Drop tables if the database has any tables so you have a fresh start.
cur.execute('DROP TABLE IF EXISTS Counts')

# Create a table called Counts which has a column for orgs in text format and the a column for count in integer format.
cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

# Enter the name oof the file that you would like to search.  For this assignment, it will be mbox-short.txt
fname = input('Enter file name: ')

# If you hit return, the value will automatically be mbox-short.txt
if (len(fname) < 1): fname = 'mbox.txt'

# Establish a handle for the file.
fh = open(fname)

# Loop through each line of the file and pull out line.
for line in fh:
    
    # # If the line does not start with 'From: ' continue to the next line.
    if not line.startswith('From: '): continue

    # # Grab the pieces of the line (or words)
    pieces = line.split()
    print('Pieces:', pieces)
    # # The piece that has the email will be in index 1
    email = pieces[1]
    print('Email:', email)
    # Seperate the email at "@" location.  The results will get you the senders name and domain name [index 1] where I will have to eliminate the periods
    domain = email.split('@')
    print('Domain:', domain)

    # Seperate the email at "." location.  The results will seperate the string at the period location but the first index will be the Company name.
    org = domain[1].strip()
    print('Org:', org)
    # Save the company names to a variable
    # org = company[0]
    # print('Print:', org)

    print("==============")
    # Select the column count from the table Counts where org is the org that I just pulled out of the document.
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))

    # Grab the first record of your search and save it to row.
    row = cur.fetchone()

    # If there is no row that fits the search:
    if row is None:

        #...Insert into the Counts table the org and count values.  The org value will be the new org and the default will be 1.
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (org,))
    else:
        #...Update into the Counts table by setting the count column to increment where the org already exists.
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (org,))

    # Commit the changes that you've just made.
    conn.commit()

# Select both the org values and count values from the table counts in decending order by the column count with a limit of 10 records.
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

# loop through the sqlstr object and pull the rows.
for row in cur.execute(sqlstr):

    # Print the rows
    print(str(row[0]), row[1])

# Close your connection.
cur.close()