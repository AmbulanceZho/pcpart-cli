import database_utils
from database_utils import get_database_path, database_connection

part_types = database_utils.tables
cpu_specs = ["brand", "name", "clock", "boost_clock", "core_count", "thread_count", "TDP", "socket"]

def cpu():
    
    with database_connection(get_database_path()) as database:
        for spec in cpu_specs:
            get_spec = input(f"Enter spec for {spec}: ")
            pass
            
        
    
def gpu():
    pass