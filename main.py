import input_utils, database_utils

def main():
    run = True
    while run:
        try:
            print("Welcome to pcparts database user interface! available actions: ")
            for act in input_utils.actions:
                print(f"-> {act}")
            action = input("Choose an action: ").strip().lower()
            
            if action == "enter":
                input_utils.get_part_type()
            
            elif action == "read":
                print("Parts:")
                for part in database_utils.tables:
                    print(f" -> {part}")
                part_type = input(f"Enter part type: ").strip().lower()
                part_name = input("Enter part name: ").strip().lower()
                input_utils.read(part_type, part_name)
        
            elif action == "update":
                pass
            
            elif action == "exit":
                run = False
            
            else:
                print(f"\"{action}\" is invalid. try an available action")
        
        except Exception as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    main()