import sqlite3

class DatabaseForUser():
    def __init__(self):
        self.conn = sqlite3.connect('user_details.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS USER(id INTEGER PRIMARY KEY, name TEXT, email TEXT, password TEXT);")

    def get_user_info(self):
        self.name_in = input('Please enter your full name: ')
        self.email_in = input('Please enter your email address: ')
        x = True
        while x is True:
            self.password_in_1 = input('Please enter a password: ')
            self.password_in_2 = input('Please enter password again: ')
            if self.password_in_1 == self.password_in_2:
                x = False
            else: continue

    def insert_user_info(self):   
        self.cursor.execute("""
        INSERT INTO USER(NAME, EMAIL, PASSWORD)
        VALUES (?,?,?)
        """, (self.name_in, self.email_in, self.password_in_1))
        self.conn.commit ()

    #self.cursor = self.conn.execute("SELECT ID, NAME, EMAIL, PASSSWORD")
    #for row in self.cursor:
    #   print ("ID = ", row[0])
    #   print ("NAME = ", row[1])
    #   print ("EMAIL = ", row[2])
    #   print ("PASSWORD = ", row[3], "\n")
    def show_table(self):
        self.cursor.execute("SELECT * FROM USER")
        print (self.cursor.fetchall())
        self.conn.close()

database_class = DatabaseForUser()
database_class.get_user_info()
database_class.insert_user_info()
database_class.show_table()