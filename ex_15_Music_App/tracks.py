# Import libraries needed for project.
import xml.etree.ElementTree as ET
import sqlite3

# Establish connection for database.  If Database does not exist, create the database.
conn = sqlite3.connect('trackdb.sqlite')

# Connection Handle
cur = conn.cursor()

# Make some fresh tables using executescript()
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')

# Gather input from user for file name.
fname = input('Enter file name: ')

# Created a short cut so you don't have to type a file name since we are only using one file. 
if ( len(fname) < 1 ) : fname = 'Library.xml'

# <key>Track ID</key><integer>369</integer>
# <key>Name</key><string>Another One Bites The Dust</string>
# <key>Artist</key><string>Queen</string>
# Created a function to lookup entries by key by passing both the entry and the key
def lookup(d, key):

    # Set found to false as a starting point.
    found = False
    
    # Loop through the results to see if there is a match. 
    for child in d:

        # If there is a match, then show the child.text
        if found : return child.text

        # You determine if when the child tag equals the key and the child text equals the key that was passed in.
        if child.tag == 'key' and child.text == key :

            # Turn found to True to indicate file found
            found = True
    return None

# Parse the XML
stuff = ET.parse(fname)

# Finall Third dictionary tag inside of the parse data.
all = stuff.findall('dict/dict/dict')

# Print out the results of your search.
print('Dict count:', len(all))

# Loop through your result and grab the entry.
for entry in all:

    # If you don't see the entry and track ID, continue to the next line.
    if ( lookup(entry, 'Track ID') is None ) : continue

    # If you find the entry and the string and run it through the lookup function. 
    name = lookup(entry, 'Name')
    
    artist = lookup(entry, 'Artist')
    
    album = lookup(entry, 'Album')

    genre = lookup(entry, 'Genre')  # Pull Genre out of the XML file.
    
    count = lookup(entry, 'Play Count')
    
    rating = lookup(entry, 'Rating')
    
    length = lookup(entry, 'Total Time')
    
    # If you don't see a name, artist and album bypass the line
    # Added Genre 
    if name is None or artist is None or album is None or genre is None : 
        continue

    # If you don't find it, print them.
    print('PULLED RECORDS \n----------')
    print('Name:', name)
    print('Artist:', artist)
    print('Album:', album)
    print('Genre', genre)  # Successfully printed out Genre from the XML file.
    print('Count:', count)
    print('Rating', rating)
    print('Length:', length)
    print('==========')

    # BEGIN YOUR SQLITE EXECUTION.
    # INSERT the name of the artist into the ARTIST table.
    cur.execute('''INSERT OR IGNORE INTO Artist (name) 
        VALUES ( ? )''', ( artist, ) )

    # SELECT id from the ARTIST table where the first record of name equals the artist you found.
    # You need the id so you can insert it into Album.
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    artist_id = cur.fetchone()[0]
    print('Artist_id:', artist_id)
    print('==========')

    # INSERT the name of the genre into the GENRE table.
    cur.execute('''INSERT OR IGNORE INTO Genre (name) 
        VALUES ( ? )''', ( genre, ) )

    # SELECT id from the GENRE table where the first record of name equals the artist you found.
    # You need the id so you can insert it into Album.
    cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ))
    genre_id = cur.fetchone()[0]
    print('Genre_id:', genre_id)
    print('==========')

    # INSERT Album title and artist_id into the ARTIST table.
    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
        VALUES ( ?, ? )''', ( album, artist_id ) )

    # SELECT ID from Album where the first record of title = the title that we found
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cur.fetchone()[0]

    # Insert into Table Track the title, album_id, length, rating, count.
    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, genre_id, len, rating, count) 
        VALUES ( ?, ?, ?, ?, ?, ? )''', 
        ( name, album_id, genre_id, length, rating, count ) )

    # Query Answer
    
    sqlstr = "SELECT Track.title, Artist.name, Album.title, Genre.name FROM Track JOIN Genre JOIN Album JOIN Artist ON Track.genre_id = Genre.ID and Track.album_id = Album.id AND Album.artist_id = Artist.id ORDER BY Artist.name LIMIT 3"

    for row in cur.execute(sqlstr):
        print(row)
    conn.commit()
