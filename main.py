import input_utils, database_utils
actions = ["enter", "read", "update", "exit"]
def main():
    run = True
    while run:
        print("Welcome to pcparts database user interface! available actions: ")
        for act in actions:
            print(f"-> {act}")
        action = input("Choose an action: ").strip().lower()
        
        if action == "enter":
            input_utils.get_part_type()
        
        elif action == "read":
            print("Parts:")
            for part in database_utils.tables:
                print(f" -> {part}")
            part_type = input(f"Enter part type: ").strip().lower()
            part_name = input("Part name: ").strip().lower()
            input_utils.read(part_type, part_name)
        
        elif action == "update":
            pass
        
        elif action == "exit":
            run = False
        
        else:
            print(f"\"{action}\" is invalid.")

if __name__ == '__main__':
    main()