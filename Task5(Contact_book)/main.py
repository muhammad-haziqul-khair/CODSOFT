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

def main():
    create_table()
    while True:
        print("")
        print("\t\t\tCONTACT BOOK\t\t\t")
        print()
        print("""    OPTIONS:
          TYPE 1: ADD NEW CONTACT
          TYPE 2: SEARCH CONTACT
          TYPE 3: UPDATE CONTACT
          TYPE 4: DELETE CONTACT
          TYPE 5: DISPLAY CONTACTS
          TYPE 6: EXIT
          """)

        opt = input("Enter your choice: ")

        if opt == "1":
            # Add new contact
            print("ADD NEW CONTACT")
            name = input("Enter Name: ").lower()
            number = input("Enter Number: ")
            while not number.isdigit():
                print("Please enter a valid number.")
                number = input("Enter Number: ")
            email = input("Enter Email: ").lower()
            address = input("Enter Address: ").lower()
            add_contact(name, number, email, address)

        elif opt == "2":
            # Search contact
            print("SEARCH CONTACT")
            attribute = input("Enter Attribute(name, number, email, address): ").lower()
            while attribute not in ["name", "number", "email", "address"]:
                print("Please enter a valid attribute.")
                attribute = input("Enter Attribute(name, number, email, address): ").lower()
            value = input(f"Enter {attribute.capitalize()}: ").lower()
            info = search_contact(attribute, value)
            for result in info:
                name = info[1]
                number = info[2]
                email = info[3]
                address = info[4]
            print("__________________________________________________________________")
            print(f"{name}\t{number}\t{email}\t\t{address}")

        elif opt == "3":
            try:
                attribute = input("Enter Attribute(name,number,email,address): ").lower()
                while attribute not in ["name", "number", "email", "address"]:
                    print("Enter valid input: ")
                    attribute = input("Enter Attribute(name,number,email,address): ").lower()
                value = input(f"Enter {attribute}: ").lower()
                contact_id = search_contact(attribute, value)
                if contact_id is None:
                    print("Contact not found!")
                    return
                possible_attribute_lst = ["name", "number", "email", "address"]
                new_attribute_lst = []
                new_value_lst = []
                for new_attribute in possible_attribute_lst:
                    opt = input(f"Wanna update {new_attribute.capitalize()} (y/n): ").lower()
                    while True:
                        if opt == "y":
                            new_attribute_lst.append(new_attribute)
                            if new_attribute == "number":
                                new_value = input(f"Enter new {new_attribute}: ")
                                while not(new_value.isdigit()):
                                    print("Enter Valid Input!")
                                    new_value = input(f"Enter new {new_attribute}: ")
                                new_value_lst.append(new_value)
                                break
                            else:    
                                new_value = input(f"Enter new {new_attribute}: ").lower()
                                new_value_lst.append(new_value)
                                break
                        elif opt == "n":
                            break
                        else:
                            print("Enter Valid Input")
                            opt = input(f"Wanna update {new_attribute.capitalize()} (y/n): ").lower()
                update_contact(contact_id,new_value_lst,new_attribute_lst)
            except Exception as e:
                print(f"Error in updating contact: {e}")

        elif opt == "4":
            print("DELETE CONTACT")
            delete_contact()

        elif opt == "5":
            print("DISPLAY CONTACTS")
            display_contacts()

        elif opt == "6":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please choose from the available options.")

if __name__ == "__main__":
    main()
    connection.close()