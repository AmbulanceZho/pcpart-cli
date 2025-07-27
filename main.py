import input_utils, database_utils

def main():
    run = True
    while run:
        action = input("What are you doing?: | [Enter, Read, Update, Exit] | ").strip().lower()
        
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