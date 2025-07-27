import sqlite3, os
from tenacity import retry, stop_after_attempt, wait_fixed, retry_if_exception_type
from dotenv import load_dotenv

load_dotenv(dotenv_path="/storage/emulated/0/pcparts/.env")

tables = ["cpu", "gpu", "mobo", "psu", "ram", "case", "mouse", "keyboard", "monitor", "headset", "laptop", "m.2", "hdd", "sata_ssd", "mouse_pad"] # add support for more parts later

def get_database_path() -> str:
    database_path = os.getenv("DataBase")
    return database_path

@retry(stop=stop_after_attempt(3), wait=wait_fixed(2), retry=retry_if_exception_type(sqlite3.OperationalError))
def database_connection(database_path):
    connection = sqlite3.connect(database_path)
    return connection