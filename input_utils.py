from database_utils import get_database_path, database_connection
import sqlite3, database_utils, part_utils

# Actions = Enter, Update, Read, Exit

database = database_connection(get_database_path())

def get_part_type():
    global database
    part_type = input("What part are you entering specs for: | cpu, gpu, mobo, psu, ram, case, mouse, keyboard, monitor, headset, laptop, m.2, hdd, sata_ssd, mouse_pad |").strip().lower()
    try:
        if part_type == "cpu":
            pass
        elif part_type == "gpu":
            pass
        elif part_type == "mobo":
            pass
    except sqlite3.Error as e:
        print(f"sqlite3 Error: {e}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        database.close()

def enter():
    pass

def update():
    pass

def read(part_type: str = "", part_name: str = ""):
    global database
    
    if part_type not in database_utils.tables:
        print(f"Part | \"{part_type}\" | is invalid.")
        return
    
    query = f"SELECT * FROM {part_type} WHERE name = ?"
    try:
        database_cursor = database.execute(query, (part_name,))
        result = database_cursor.fetchall()
        
        if not result:
            print(f"No matching part found for: | \"{part_name}\" | .")
        else:
            for row in result:
                print(f"{row}\n")
    except sqlite3.Error as e:
        print(f"Sqlite3 Error: {e}")  