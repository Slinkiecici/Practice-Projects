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

    def show_table(self):
        self.cursor.execute("SELECT * FROM USER")
        print (self.cursor.fetchall())


    def update_user_info(self, identifier):
        #self.cursor.execute("UPDATE USER SET name = whatever WHERE)
        pass
    
    def delete_user_info(self, named):
        delete_statement = "DELETE FROM USER WHERE  email = ?"
        self.cursor.execute(delete_statement, (named, ))
        self.conn.commit ()

database_class = DatabaseForUser()
database_class.get_user_info()
database_class.insert_user_info()
database_class.show_table()
database_class.delete_user_info("@frog")
database_class.conn.close()