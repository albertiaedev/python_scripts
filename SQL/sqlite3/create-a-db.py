import sqlite3

db = sqlite3.connect('test.db')
c = db.cursor()
c.execute("""CREATE TABLE dataypes(
                dtype_1 text,
                dtype_2 integer,
                dtype_3 real,
                dtype_4 text
                )""")

# IN SQLITE3 THERE ARE 5 DATATYPES: NULL; INTEGER; REAL; TEXT; BLOB

db.commit()
db.close()
