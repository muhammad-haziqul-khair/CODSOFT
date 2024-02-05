import sqlite3
from datetime import datetime

connection = sqlite3.connect('Task1(to-do-list)/todo_list.db')
cursor = connection.cursor()

def create_table():
    create_table_query =''' CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    task VARCHAR(50) NOT NULL,
                    added_at TIMESTAMP NOT NULL,
                    deadline TIMESTAMP
                )'''
    cursor.execute(create_table_query)
    connection.commit()

def add_task(task, deadline_str):
    try:
        added_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        deadline = datetime.strptime(deadline_str, "%Y-%m-%d").strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute("INSERT INTO tasks (task, added_at, deadline) VALUES (?, ?, ?)", (task, added_at, deadline))
        connection.commit()
        print(f"Task '{task}' added with deadline {deadline}.")
    except Exception as e:
        print(f"Error adding task: {e}")

def view_tasks():
    try:
        cursor.execute("SELECT * FROM tasks")
        tasks = cursor.fetchall()
        if tasks:
            print("Tasks:")
            for task in tasks:
                task_id, task_desc, added_at, deadline = task
                added_time = datetime.strptime(added_at, "%Y-%m-%d %H:%M:%S")
                deadline_time = datetime.strptime(deadline, "%Y-%m-%d %H:%M:%S")
                time_diff = deadline_time - datetime.now()
                print(f"{task_id}. {task_desc} (Added at: {added_at}, Deadline: {deadline}, Time remaining: {time_diff})")
        else:
            print("No tasks in the list.")
    except Exception as e:
        print(f"Error viewing tasks: {e}")

def input_year():
            year = input("Enter year (YYYY): ")
            while len(year) != 4 or not year.isdigit():
                print("Enter valid input")
                year = input("Enter year (YYYY): ")

            month = input("Enter month (MM): ")
            while len(month) != 2 or not month.isdigit() or int(month) < 1 or int(month) > 12:
                print("Enter Valid input.")
                month = input("Enter month (MM): ")
            
            day = input("Enter day (DD): ")
            while len(day) != 2 or not day.isdigit() or int(day) < 1 or int(day) > 31:
                print("Enter Valid Input!")
                day = input("Enter day (DD): ")
            if month in ['04', '06', '09', '11'] and day > 30:
                print("Invalid day for this month.")
                day = input("Enter day (DD): ")
            elif month == '02':
                if int(year) % 4 == 0 and (int(year) % 100 != 0 or int(year) % 400 == 0):
                    if int(day) > 29:
                        print("Invalid day for this month and year (leap year).")
                        day = input("Enter day (DD): ")
                    elif int(day) > 28:
                        print("Invalid day for this month and year.")
                        day = input("Enter day (DD): ")
            year = int(year)
            month = int(month)
            day = int(day)
            global deadline
            deadline = f"{year}-{month}-{day}"
def search_task(value):
        try:
            search_query = f"SELECT id from tasks WHERE task = '{value}'"
            cursor.execute(search_query)
            result = cursor.fetchone()
            if result:
                return result[0]
            else:
                return None
        except Exception as e:
            print(f"Error searching for Contact: ({e})")
def remove_task(task_name):
    try:
        # task_name = input('Enter the taskname you want to remove: ').lower()
        task_id = search_task(task_name)
        if task_id is None:
            print("Task not found")
        else:
            cursor.execute("SELECT task FROM tasks WHERE id = ?", (task_id,))
            task = cursor.fetchone()
            if task:
                cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
                connection.commit()
                print(f"Task '{task[0]}' removed.")
            else:
                print("Task not found.")
    except Exception as e:
        print(f"Error removing task: {e}")


def main():
    create_table()
    while True:
        print("\nTODO LIST")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ").lower()
            input_year()
            current_time = datetime.now()
            deadline_time = datetime.strptime(deadline, "%Y-%m-%d")
            while deadline_time < current_time:
                print("Enter a valid deadline!")
                input_year()
                current_time = datetime.now()
                deadline_time = datetime.strptime(deadline, "%Y-%m-%d")
            add_task(task, deadline)
    
        elif choice == "2":
            pass
            task_name = input("Ente task name to remove: ")
            remove_task(task_name)
        elif choice == "3":
            view_tasks()
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
    connection.close()
