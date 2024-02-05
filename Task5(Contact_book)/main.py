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

def search_contact(attribute,value,return_columns = None):
        try:
            if return_columns:
                columns = ", ".join(return_columns)
            else:
                columns = "*"
            search_query = f"SELECT {columns} from contacts WHERE {attribute} = '{value}'"
            cursor.execute(search_query)
            result = cursor.fetchone()
            if result:
                if return_columns and len(return_columns) == 1:
                    return result[0]
                else:
                    return result
            else:
                return None
        except Exception as e:
            print(f"Error searching for Contact: ({e})")

def update_contact(contact_id,new_value_lst,new_attribute_lst):
    try:
        set_clause = ", ".join([f"{new_attribute} = ?" for new_attribute in new_attribute_lst])
        update_query = f"UPDATE contacts SET {set_clause} WHERE id = ?"
        new_value_lst.append(contact_id) 
        cursor.execute(update_query, new_value_lst)
        connection.commit()
        print("Contact Updated!")
    except Exception as e:
        print(f"Error in updating contact: {e}")

def display_contacts():
    try:
        cursor.execute("SELECT * FROM contacts")
        contacts = cursor.fetchall()
        if contacts:
            print("Contacts:")
            for contact in contacts:
                name = contact[1]
                number = contact[2]
                email = contact[3]
                address = contact[4]
                print("Contact found!")
                print(f"{name}\t{number}\t{email}\t{address}")
        else:
            print("No contacts found.")
    except sqlite3.Error as e:
        print("Error:", e)

def delete_contact():
    try:
            attribute = input("Enter Attribute(name,number,email,address): ").lower()
            while attribute not in ["name","number","email","address"]:
                print("Enter valid input: ")
                attribute = input("Enter Attribute(name,number,email,address): ").lower()
            value = input(f"Enter {attribute}: ").lower()
            contact_id = search_contact(attribute,value)
            if contact_id:
                delete_query = f"DELETE FROM contacts WHERE id = {contact_id}"
                cursor.execute(delete_query)
                connection.commit()
                print("Contact deleted successfully")
            else:
                print("No contact Found!")
        
    except Exception as e:
        print("Error deleting contact:", e)

def search_contact(attribute,value,return_columns = None):
        try:
            if return_columns:
                columns = ", ".join(return_columns)
            else:
                columns = "*"
            search_query = f"SELECT {columns} from contacts WHERE {attribute} = '{value}'"
            cursor.execute(search_query)
            result = cursor.fetchone()
            if result:
                if return_columns and len(return_columns) == 1:
                    return result[0]
                else:
                    return result
            else:
                return None
        except Exception as e:
            print(f"Error searching for Contact: ({e})")