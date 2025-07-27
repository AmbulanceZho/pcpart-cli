import database_utils
from database_utils import get_database_path, database_connection

part_types = database_utils.tables
cpu_specs = ["brand", "name", "clock", "boost_clock", "core_count", "thread_count", "TDP", "socket"]

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
        
        database_cursor = database.cursor()
        database_cursor.execute(sql, values)
        database.commit()     
    
def gpu():
    pass