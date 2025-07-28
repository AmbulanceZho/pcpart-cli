import sqlite3
from database_utils import get_database_path, database_connection, tables
from part_utils import add_part

actions = ["enter", "read", "exit"]

def get_part_type():
    print("Parts: ")
    for part in tables:
        print(f" -> {part}")
    part_type = input("What part are you entering specs for: ").strip().lower()
    try:
        if part_type in tables:
            add_part(part_type)
        else:
            print(f"{part_type} is not valid.")
    except sqlite3.Error as e:
        print(f"sqlite3 Error: {e}")
    except Exception as e:
        print(f"Error: {e}")

def read(part_type: str = "", part_name: str = "") -> None:
    with database_connection(get_database_path()) as database:
        
        if part_type not in tables:
            print(f"Part | \"{part_type}\" | is invalid.")
            return

        try:
            cursor = database.execute(f"PRAGMA table_info({part_type});")
            existing_columns = [row[1] for row in cursor.fetchall()]
            
            searchable_fields = [field for field in ["name", "model", "brand", "manufacturer"] if field in existing_columns]

            if not searchable_fields:
                print(f"No searchable fields found in '{part_type}' table.")
                return
            
            like_clauses = " OR ".join(f"{field} LIKE ?" for field in searchable_fields)
            query = f"SELECT * FROM {part_type} WHERE {like_clauses}"
            params = tuple(f"%{part_name}%" for _ in searchable_fields)
            
            cursor = database.execute(query, params)
            results = cursor.fetchall()

            if not results:
                print(f"No matching part found for: | \"{part_name}\" |.")
                return

            columns = [desc[0] for desc in cursor.description]
            for row in results:
                print("─" * 40)
                for col, val in zip(columns, row):
                    print(f"{col:<15}: {val}")
                print("─" * 40)

        except sqlite3.Error as e:
            print(f"SQLite error: {e}")
        except Exception as e:
            print(f"Error: {e}")
