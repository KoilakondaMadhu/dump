import sqlite3

# Create a connection to the database
conn = sqlite3.connect('Inventory_Management.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Create the manufacture table
cursor.execute('''CREATE TABLE manufacture
                 (id INTEGER PRIMARY KEY,
                 product_name TEXT,
                 color TEXT,
                 quantity INTEGER,
                 manufacturing_date TEXT,
                 defective INTEGER)''')

# Create the goods table
cursor.execute('''CREATE TABLE goods
                 (id INTEGER PRIMARY KEY,
                 product_name TEXT,
                 color TEXT,
                 quantity INTEGER,
                 manufacturing_date TEXT)''')

# Create the purchase table
cursor.execute('''CREATE TABLE purchase
                 (id INTEGER PRIMARY KEY,
                 store_name TEXT,
                 product_name TEXT,
                 color TEXT,
                 quantity INTEGER,
                 purchase_amount REAL,
                 purchase_date TEXT)''')

# Create the sale table
cursor.execute('''CREATE TABLE sale
                 (id INTEGER PRIMARY KEY,
                 store_name TEXT,
                 product_name TEXT,
                 color TEXT,
                 quantity INTEGER,
                 sale_amount REAL,
                 sale_date TEXT)''')

# Save the changes and close the connection
conn.commit()
conn.close()

----------------
# Insert data into the manufacture table
cursor.execute("INSERT INTO manufacture VALUES (1, 'Toy Car', 'Red', 100, '01-05-23', 0)")
cursor.execute("INSERT INTO manufacture VALUES (2, 'Toy Train', 'Green', 50, '01-05-23', 0)")
cursor.execute("INSERT INTO manufacture VALUES (3, 'Wooden Chair', 'Brown', 200, '01-04-23', 0)")
cursor.execute("INSERT INTO manufacture VALUES (4, 'Wooden Table', 'Brown', 100, '01-03-23', 0)")
cursor.execute("INSERT INTO manufacture VALUES (5, 'Shirt', 'Blue', 50, '01-02-23', 1)")

# Insert data into the goods table
cursor.execute("INSERT INTO goods VALUES (1, 'Toy Car', 'Red', 100, '01-05-23')")
cursor.execute("INSERT INTO goods VALUES (2, 'Toy Train', 'Green', 50, '01-05-23')")
cursor.execute("INSERT INTO goods VALUES (3, 'Wooden Chair', 'Brown', 200, '01-04-23')")
cursor.execute("INSERT INTO goods VALUES (4, 'Wooden Table', 'Brown', 100, '01-03-23')")

# Insert data into the purchase table
cursor.execute("INSERT INTO purchase VALUES (1, 'MyKids', 'Toy Car', 'Red', 50, 500, '01-05-23')")
cursor.execute("INSERT INTO purchase VALUES (2, 'MyKids', 'Toy Train', 'Green', 25, 250, '01-05-23')")
cursor.execute("INSERT INTO purchase VALUES (3, 'ORay', 'Shirt', 'Blue', 10, 200, '01-05-23')")