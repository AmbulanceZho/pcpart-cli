import database_utils, sqlite3
from database_utils import get_database_path, database_connection
from spec_utils import *

spec_lookup = {
    "cpu": cpu_specs,
    "gpu": gpu_specs,
    "mobo": mobo_specs,
    "psu": psu_specs,
    "ram": ram_specs,
    "pc_case": case_specs,
    "mouse": mouse_specs,
    "keyboard": keyboard_specs,
    "monitor": monitor_specs,
    "headset": headset_specs,
    "m2": m2_specs,
    "hdd": hdd_specs,
    "sata_ssd": sata_ssd_specs,
    "mouse_pad": mouse_pad_specs,
}

def add_part(part_type: str):
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

    with database_connection(get_database_path()) as db:
        try:
            cursor = db.cursor()
            cursor.execute(sql, values)
            db.commit()
            print("Success! Added:")
            for k, v in part_data.items():
                print(f"| {k} | {v} |")
            print("to the database.")
        except sqlite3.IntegrityError:
            unique_key = f"{part_data['brand']} {part_data['model']}" if part_type == "gpu" else f"{part_data['manufacturer']} {part_data['model']}"
            print(f"{unique_key} already exists.")
        except Exception as e:
            print(f"Unexpected error: {e}")