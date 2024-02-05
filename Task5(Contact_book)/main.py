import sqlite3

connection = sqlite3.connect('Task5(Contact_book)/contact.db')
cursor = connection.cursor()

def create_table():
    try:
        create_table_query = """CREATE TABLE IF NOT EXISTS contacts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(50) NOT NULL,
        number INT NOT NULL,
        email VARCHAR(50),
        address VARCHAR(50)
        ) """
        cursor.execute(create_table_query)
        connection.commit()
    except Exception as e:
        print(f"Error in Creating Table: ({e})")
    
def add_contact(n,num,e,a):
    try:
        add_contact_query = f"INSERT INTO contacts (name,number,email,address) VALUES ('{n}',{num},'{e}','{a}')"
        cursor.execute(add_contact_query)
        connection.commit()
        print("Data added")
    except Exception as e:
        print(f"Error in Adding Contact: ({e})")

def search_contact(attribute,value):
        try:
            search_query = f"SELECT id from contacts WHERE {attribute} = '{value}'"
            cursor.execute(search_query)
            result = cursor.fetchone()
            if result:
                return result[0]
            else:
                return None
        except Exception as e:
            print(f"Error searching for Contact: ({e})")