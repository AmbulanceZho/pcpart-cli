import sqlite3
from database_utils import get_database_path, database_connection
from spec_utils import spec_lookup

def add_part(part_type: str = None) -> None:
    part_type = part_type.lower()
    
    if part_type not in spec_lookup:
        print(f"Part type '{part_type}' is not supported.")
        return

    specs = spec_lookup[part_type]

    part_data = {}
    for spec in specs:
        value = input(f"Enter spec for {spec}: ")
        part_data[spec] = value

    columns = ", ".join(part_data.keys())
    placeholders = ", ".join("?" for _ in part_data)
    values = tuple(part_data.values())

    sql = f"INSERT INTO {part_type} ({columns}) VALUES ({placeholders})"

    with database_connection(get_database_path()) as database:
        try:
            database_cursor = database.cursor()
            database_cursor.execute(sql, values)
            database.commit()
            print("Success! Added:")
            for k, v in part_data.items():
                print(f"| {k} | {v} |")
            print("to the database.")
        except sqlite3.IntegrityError:
            unique_key = f"{part_data['brand']} {part_data['model']}" if part_type == "gpu" else f"{part_data['manufacturer']} {part_data['model']}"
            print(f"{unique_key} already exists.")
        except Exception as e:
            print(f"Unexpected Error: {e}")