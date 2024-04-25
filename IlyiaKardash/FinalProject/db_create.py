# creating a database in sqlite

import sqlite3

# establishing a connection + giving a name for new db
conn = sqlite3.connect("expenses.db")

# creating an object for executing sql queries
cur = conn.cursor()

# creating a table and identifying columns and data types per column
cur.execute("""CREATE TABLE IF NOT EXISTS expenses(
            id INTEGER PRIMARY KEY,
            Date DATE,
            description TEXT,
            category TEXT,
            price REAL)""")

# committing the transaction
conn.commit()

# closing existing connection
conn.close()
