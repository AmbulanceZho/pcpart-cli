from database_utils import get_database_path, database_connection, tables
import sqlite3, part_utils

actions = ["enter", "read", "exit"] #read is just for testing the enter action, this interface is for my eyes and use only. 

def get_part_type():
    print("Parts: ")
    for part in tables:
        print(f" -> {part}")
    part_type = input("What part are you entering specs for: ").strip().lower()
    try:
        if part_type == "cpu":
            part_utils.cpu()
        elif part_type == "gpu":
            part_utils.gpu()
        elif part_type == "mobo":
            pass # fill in the rest of the logic later
    except sqlite3.Error as e:
        print(f"sqlite3 Error: {e}")
    except Exception as e:
        print(f"Error: {e}")

def read(part_type: str = "", part_name: str = "") -> None:
    with database_connection(get_database_path()) as database:
    
        if part_type not in tables:
            print(f"Part | \"{part_type}\" | is invalid.")
        
        query = f"SELECT * FROM {part_type} WHERE name LIKE ?"
        try:
            database_cursor = database.execute(query, (f"%{part_name}%",))
            result = database_cursor.fetchall()
            
            if not result:
                print(f"No matching part found for: | \"{part_name}\" | .")
            else:
                columns = [desc[0] for desc in database_cursor.description]
                for row in result:
                    print("─" * 40)
                    for col, val in zip(columns, row):
                        print(f"{col:<15}: {val}")
                    print("─" * 40)
                
        except sqlite3.Error as e:
            print(f"Sqlite3 Error: {e}")
        except Exception as e:
            print(f"Error: {e}")