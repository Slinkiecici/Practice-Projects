import sqlite3

#conn = sqlite3.connect(":memory")          used for temp databases in memory
conn = sqlite3.connect("contactbook.db")

c = conn.cursor()                           #allows executing of sql commands

def create_table ():
    c.execute(''' SELECT count(name) FROM sqlite_master 
                WHERE type='table' AND name='contacts' ''')

    if c.fetchone()[0]==1 : {
	    print('Table exists.')
}
    else:
        c.execute('''CREATE TABLE contacts (name TEXT, surname TEXT)''')
    conn.commit()


def insert_to_table (named, surname):
    executed_string = "INSERT INTO contacts VALUES ( '" + named + "', '" + surname + "')"
    print (executed_string)
    c.execute(executed_string)

create_table()
insert_to_table("Cisquared", "Jellybeans")
conn.close()