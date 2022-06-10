# Import the sqlite library into the program.
import sqlite3

# Establish connection with the database.
# If the file does not exist, then it will create the fil within the directory.
conn = sqlite3.connect('emaildb.sqlite')

# Establish the handle for the connection.
cur = conn.cursor()

# Use the execute command to drop the table if it exists.
# Pass your MySql commands inside of the Quotes
cur.execute('DROP TABLE IF EXISTS Counts')

# Use the execute command to create a table
# Pass your MySql commands inside of the Quotes
cur.execute('CREATE TABLE Counts (email TEXT, count INTEGER)')

# Grab input from user 
fname = input('Enter file name: ')

# If the length of the file name that is entered is less than one, default to the text file for assignment.
if (len(fname) < 1) : fname = 'mbox-short.txt'

# Open the file name
fh = open(fname)

# Loop through the lines in the document
for line in fh:

    # If the line does not start with 'From: ' then continue to the next line.
    if not line.startswith('From: '): continue

    # Grab the pieces of the line that match your search
    pieces = line.split()
    
    # Grab the email, which is index number 1, and save it.
    email = pieces[1]

    # Execute the following MySql comment 
    # Select the count column from within the Counts table where email equals the email that you grabbed.
    cur.execute('SELECT count FROM Counts WHERE email = ?', (email,))

    # Grab the first row that you got from the previous execute
    row = cur.fetchone()

    # If there are no rows in the table that contain that email
    if row is None:

        # ... INSERT the email into a new record.
        cur.execute('INSERT INTO Counts (email, count) VALUES (?, 1)', (email,))

    # If the record does exists,  
    else: 

        # ... UPDATE the record with mysql code.
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?', (email,))

    # Use the commit method to save the changes that you've made on MySql.
    conn.commit()

# Save MySql string that will select email and count from the Counts table and order the records by count in decending with a limit of 10
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

# Loop through the results and print.
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

# close the connection to the database.
cur.close()