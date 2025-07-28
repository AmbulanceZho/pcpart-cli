import sqlite3
from database_utils import database_connection, get_database_path, tables
from part_utils import add_part

actions = ["enter", "read", "exit"]

def get_part_type() -> None:
    print("Parts: ")
    for part in tables:
        print(f" -> {part}")
    part_type = input("What part are you entering specs for: ").strip().lower()
    try:
        if part_type in tables:
            add_part(part_type)
        else: #user error handling typos
            print(f"{part_type} is not valid.")
    except sqlite3.Error as e:
        print(f"Unexpected Sqlite3 Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")

def read(part_type: str = "", part_name: str = "") -> None:
    with database_connection(get_database_path()) as database:
        
        if part_type not in tables:
            print(f"Part | \"{part_type}\" | is invalid.")
            return

        try:
            database_cursor = database.execute(f"PRAGMA table_info({part_type});")
            existing_columns = [row[1] for row in database_cursor.fetchall()]
            
            searchable_fields = [field for field in ["name", "model", "brand", "manufacturer"] if field in existing_columns]

            if not searchable_fields:
                print(f"No searchable fields found in '{part_type}' table.")
                return
            
            like_clauses = " OR ".join(f"{field} LIKE ?" for field in searchable_fields)
            query = f"SELECT * FROM {part_type} WHERE {like_clauses}"
            params = tuple(f"%{part_name}%" for _ in searchable_fields)
            
            database_cursor = database.execute(query, params)
            results = database_cursor.fetchall()

            if not results:
                print(f"No matching part found for: | \"{part_name}\" |.")
                return

            columns = [desc[0] for desc in database_cursor.description]
            for row in results:
                print("─" * 40)
                for col, val in zip(columns, row):
                    print(f"{col:<15}: {val}")
                print("─" * 40)

        except sqlite3.Error as e:
            print(f"Unexpected Sqlite error: {e}")
        except Exception as e:
            print(f"Unexpected Error: {e}")
