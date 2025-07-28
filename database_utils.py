import sqlite3, os
from tenacity import retry, stop_after_attempt, wait_fixed, retry_if_exception_type #Mobil friendliness and discord.py friendly
from dotenv import load_dotenv
from contextlib import contextmanager #discord.py async/await friendly using 'with'

#TODO add function that updates tables dynamically to insert more columns in future and a second sub command to update old entries with NULL in newly added fields


load_dotenv(dotenv_path="/storage/emulated/0/pcparts/.env")

tables = ["cpu", "gpu", "mobo", "psu", "ram", "pc_case", "mouse", "keyboard", "monitor", "headset", "laptop", "m2", "hdd", "sata_ssd", "mouse_pad"] # add support for more parts later

def get_database_path() -> str:
    database_path = os.getenv("DataBase")
    
    if not os.path.exists(database_path):
        raise FileNotFoundError(f"Database not found at {database_path}")
    
    return database_path

@contextmanager
@retry(stop=stop_after_attempt(3), wait=wait_fixed(2), retry=retry_if_exception_type(sqlite3.OperationalError))
def database_connection(database_path: str) -> sqlite3.Connection:
    connection = sqlite3.connect(database_path)
    try:
        yield connection
    except sqlite3.Error as e:
        print(f"Unexpected Sqlite3 Error: {e}.")
    except Exception as e:
        print(f"Unexpected Error: {e}")
    finally:
        connection.close()

def create_tables_if_not_exist(table_specs: dict) -> None:
    with database_connection(get_database_path()) as database:
        try:
            database_cursor = database.cursor()
            for table, columns in table_specs.items():
                unique_columns = list(dict.fromkeys(columns))
                sql_fields = []

                for col in unique_columns:
                    sql_fields.append(f"{col} TEXT")
                    
                constraints = ""
                if "brand" in unique_columns and "model" in unique_columns:
                    constraints = ", UNIQUE(brand, model)" # constraint for gpus, to allow multiple Nvidia GTX/RTX series gpus from AIB partners. 
                elif "manufacturer" in unique_columns and "model" in unique_columns:
                    constraints = ", UNIQUE(manufacturer, model)" # constraints for everything else.

                sql = f"""
                CREATE TABLE IF NOT EXISTS {table} (
                    {", ".join(sql_fields)}{constraints}
                );
                """.strip()

                database_cursor.execute(sql)
                print(sql)
            database.commit()
        except sqlite3.Error as e:
            print(f"Unexpected Sqlite3 Error: {e}")
        except Exception as e:
            print(f"Unexpected Error: {e}")
