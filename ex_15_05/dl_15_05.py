# Import the sqlite library into the program
import sqlite3

# Establish connection with new database
conn = sqlite3.connect("Ages_DB.sqlite")

# Establish handle for the connection
cur = conn.cursor()

# Drop Table if it exists.  When you rerun the program,  the create Table is display that you already have a table.
cur.execute("DROP TABLE IF EXISTS Ages")

# Create a table for Ages that has a name TEXT and age INTEGER
cur.execute("CREATE TABLE Ages (name TEXT, age INTEGER)")

cur.execute("DELETE FROM Ages")

'''
Created an insert record class.  I didn't have to create a class since it's just one method.  I didn't have to create a method or a function. I could've copied the code from the assignment.  I just made this class because I wanted to practice it.
'''
class insert:
    
    def record(n, a):
        
        print('Constructed:', n,type(n),a,type(a))
        cur.execute("INSERT INTO Ages (name, age) VALUES (?,?)", (n,a))

# Insert the names and ages into the database.
insert.record('Maison',40)
insert.record('Aanya',24)
insert.record('Alissa', 14)
insert.record('Malak', 37)
insert.record('Nikoleta', 25)

# Confirm that the records exist on the database.
record = "SELECT name, age FROM Ages ORDER BY age DESC LIMIT 10"

print('Names ( Ages ) \n=====================')
# Loop through the results and print.
for row in cur.execute(record):
    print(str(row[0]), '(',row[1],')')

# Pass the command through the execute method within the instance of cur and save to variable.
answer = 'SELECT hex(name || age) AS X FROM Ages ORDER BY X'

print(answer, type(answer))

for row in cur.execute(answer):
    print(str(row[0]))
# close the connection to the database.
cur.close()