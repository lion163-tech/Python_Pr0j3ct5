#Original tutorial by Tomi Tokko
#Learning how to use Python for web dev
import sqlite3

connect = sqlite3.connect('data.db')

connect.execute("DROP TABLE IF EXITS COSTUMER")
connect.execute('''CREATE TABLE CUSTOMER
            (ID INT PRIMARY KEY NOT NULL,
            NAME TEXT NOT NULL);''')

connect.close()