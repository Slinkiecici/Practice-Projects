import sqlite3
class ContactDatabase (object):
    def __init__(self):
        #conn = sqlite3.connect(":memory")          used for temp databases in memory
        self.conn = sqlite3.connect("contactbook.db")
        self.c = self.conn.cursor()                           #allows executing of sql commands

    def create_table (self):
        self.c.execute(''' SELECT count(name) FROM sqlite_master 
                    WHERE type='table' AND name='contacts' ''')

        if self.c.fetchone()[0]==1 : {
            print('Table exists.')
    }
        else:
            self.c.execute('''CREATE TABLE contacts (name TEXT, surname TEXT)''')
        self.conn.commit()
        
    def insert_to_table (self):
        named = input("Insert new contact name: ")
        surname = input("Insert new surname name: ")
        #executed_string = "INSERT INTO contacts VALUES ( '" + named + "', '" + surname + "')"
        self.c.execute("INSERT INTO contacts VALUES (?, ?)", (named, surname))
        #self.c.execute(executed_string)
        self.conn.commit()

    def display_contact_list (self):
        self.c.execute("Select * FROM contacts")
        print (self.c.fetchall())
    
    def display_specific_contact (self):
        named = input("Insert name to search: ")
        self.c.execute("Select * FROM contacts WHERE name='" + named + "' ")
        print (self.c.fetchall())        
        
contact_database = ContactDatabase()            #Create class instance
contact_database.create_table()                 #run create table function
#contact_database.insert_to_table()
contact_database.display_specific_contact()
contact_database.display_contact_list()
#conn.close()