import database_utils, sqlite3
from database_utils import get_database_path, database_connection
from spec_utils import *

part_types = database_utils.tables

def cpu():   
    with database_connection(get_database_path()) as database:
        cpuspecs = {}
        for spec in cpu_specs:
            get_spec = input(f"Enter spec for {spec}: ")
            cpuspecs[spec] = get_spec
        
        columns = ", ".join(cpuspecs.keys())
        place_holders = ", ".join("?" for _ in cpuspecs)
        values = tuple(cpuspecs.values())
        
        sql = f"INSERT INTO cpu ({columns}) VALUES ({place_holders})"
        try:
            database_cursor = database.cursor()
            database_cursor.execute(sql, values)
            database.commit()
            print(f"Success! Added: ")
            for key, value in cpuspecs.items():
                print(f"| {key} | {value} |")
            print("to the data base.")
        except sqlite3.IntegrityError:
            print(f"{cpuspecs['name']} already exists.")
    
def gpu():
    with database_connection(get_database_path()) as database:
        gpuspecs = {}
        for spec in gpu_specs:
            get_spec = input(f"Enter spec for {spec}: ")
            gpuspecs[spec] = get_spec
        
        columns = ", ".join(gpuspecs.keys())
        place_holders = ", ".join("?" for _ in gpuspecs)
        values = tuple(gpuspecs.values())
        
        sql = f"INSERT INTO gpu ({columns}) VALUES ({place_holders})"
        try:
            database_cursor = database.cursor()
            database_cursor.execute(sql, values)
            database.commit()
            print(f"Success! Added: ")
            for key, value in gpuspecs.items():
                print(f"| {key} | {value} |")
            print("to the data base.")
        except sqlite3.IntegrityError:
            print(f"{gpuspecs['name']} already exists.")

# implement rest of commands later.