# Import the libraries necessary for the assignment
import json
import sqlite3

# Establish a connection to your database.
# If the datbase does not exist, this will create one.
conn = sqlite3.connect('rosterdb.sqlite')

# Establish a handle to your database.
cur = conn.cursor()

# Set up the tables for the database.
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

# Enter the file name of the json file that you wish to read.
fname = input('Enter file name: ')

# If the input is empty, default to the assignment file.
if len(fname) < 1:
    fname = 'roster_data.json'

# [
#   [ "Charley", "si110", 1 ],
#   [ "Mea", "si110", 0 ],

# read the data and parse it into a string.
str_data = open(fname).read()

# Read the string data and parse it into a jason object.
json_data = json.loads(str_data)

# Loop through the object
for entry in json_data:

    # Pull the name and tile
    name = entry[0]
    title = entry[1]
    role = entry[2]

    # Print the name and title.
    print((name, title, role))

    # Insert in the USER table, the name into the name column
    cur.execute('''INSERT OR IGNORE INTO User (name)
        VALUES ( ? )''', ( name, ) )
    
    # Grab the User's ID so you can input into the pivot table
    cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
    user_id = cur.fetchone()[0]
    print('User_id:', user_id)
    
    # INSERT into the Course table the title into the title's column
    cur.execute('''INSERT OR IGNORE INTO Course (title)
        VALUES ( ? )''', ( title, ) )

    # SELECT the ID from the COURSE table where title = title for the course id.
    cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
    course_id = cur.fetchone()[0]
    print('Course_id:', course_id)
    
    
    # INSERT USER_ID AND COURSE_ID INTO PIVOT TABLE.
    cur.execute('''INSERT OR REPLACE INTO Member
        (user_id, course_id, role) VALUES ( ?, ?, ? )''',
        ( user_id, course_id, role ) )
    print('Role:', role)
    print('----------')

    testsqlstr = '''
    SELECT User.name,Course.title, Member.role 
    FROM User JOIN Member JOIN Course 
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY User.name DESC, Course.title DESC, Member.role DESC LIMIT 2;
    '''
    print('TEST ANSWER')
    for r in cur.execute(testsqlstr):
        print(r[0],'|',r[1],'|',r[2])
    
    print('----------')
    print('FINAL ANSWER')
    answersqlstr = '''
    SELECT 'XYZZY' || hex(User.name || Course.title || Member.role ) AS X FROM 
    User JOIN Member JOIN Course 
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY X LIMIT 1;
    '''
    for r in cur.execute(answersqlstr):
        print(r[0])
    print('==========') 
    conn.commit()