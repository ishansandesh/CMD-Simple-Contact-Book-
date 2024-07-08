import os

contact_list = {}

def add_contact():
    name = input("Enter contact Name: ")
    number = input("Enter contact Number: ")
    if (len(number) == 10 or number[0] == "+") and (number.isdecimal() or number[1:].isdecimal()):
        if name not in contact_list:
            contact_list[name] = number
            print("Contact saved!\n")
        else:
            print("Name already exists in the contact list.")
    else:
        print("Invalid number format.")

def view_contacts():
    print("\nContact List View --> ")
    for name, number in contact_list.items():
        print(f"{name} -> {number}")

def edit_contact():
    edit_detail = input("Enter Name to edit: ")
    if edit_detail in contact_list:
        print(f"Current name -> {edit_detail}")
        new_name = input("Enter new name: ")
        new_number = input("Enter new number: ")
        if len(new_number) == 10 or new_number[0] == "+":
            contact_list[new_name] = new_number
            if new_name != edit_detail:
                del contact_list[edit_detail]
            print("Edit successful!")
        else:
            print("Invalid number format.")
    else:
        print("Name not found in contacts.")

def delete_contact():
    delete_contact = input("Enter name to delete: ")
    if delete_contact in contact_list:
        del contact_list[delete_contact]
        print("Delete successful!")
    else:
        print("Name not found in contacts.")

def clear_screen():
    # Clear screen based on OS
    os.system('cls' if os.name == 'nt' else 'clear')

# Main loop
while True:
    print("""
   ___         _           _     ___           _   
  / __|___ _ _| |_ __ _ __| |_  | _ ) ___  ___| |__
 | (__/ _ \ ' \  _/ _` / _|  _| | _ \/ _ \/ _ \ / /
  \___\___/_||_\__\__,_\__|\__| |___/\___/\___/_\_\\ """)
    print("\nCommands:")
    print("add contact -> add\nview contact -> view\nedit contact -> edit\ndelete contact -> delete\nexit -> exit\n")
    command = input("Enter command: ").strip().lower()
    
    clear_screen()

    if command == "exit":
        break
    elif command == "add":
        add_contact()
    elif command == "view":
        view_contacts()
    elif command == "edit":
        edit_contact()
    elif command == "delete":
        delete_contact()
    else:
        print("Invalid command!")

print("Have a nice day!")
