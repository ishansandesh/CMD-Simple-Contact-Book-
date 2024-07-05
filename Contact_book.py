contact_list = {}
value =True

def add():
    global contact_list
    name = input("Enter contact Name: ")
    number = input("Enter contact Number: ")
    if (len(number) == 10 or number[0] == "+") and (number.isdecimal() or number[1:].isdecimal()):
        if name not in contact_list:
            contact_list[name] = number
            print("Contact saved!\n")
        else:
            print("Name already exists in the contact list.")
    else:
        print("\n(Something wrong) Check your number or name.")

def view():
    global contact_list
    print("\nContact List View --> ")
    for name, number in contact_list.items():
        print(f"{name} -> {number}")

def edit():
    global contact_list
    print("\nEdit Details :")
    edit_detail = input("Enter Name :")
    if edit_detail in contact_list:
        print(f"name -> {edit_detail}")
        new_name = input("Enter new name: ")
        new_number = input("Enter new number: ")
        if len(new_number) == 10 or new_number[0] == "+":
            contact_list.pop(edit_detail)
            contact_list[new_name] = new_number
            print("Edit successful!")
        else:
            print("Invalid number format.")
    else:
        print("Invalid name.")

def delete():
    global contact_list
    print("\nDelete name --->")
    delete_contact = input("Enter name to delete: ")
    if delete_contact in contact_list:
        contact_list.pop(delete_contact)
        print("Delete successful!")
    else:
        print("Name is incorrect.")
        
while value:
    print("\nCONTACT BOOK!")
    print("\nCommands:")
    print("""add contact -> add\nview contact -> view\nedit contact -> edit\ndelete contact -> delete\nexit -> exit\n""")
    x = input("Enter : ")
    if x.lower() in ["add", "view", "edit", "delete", "exit"]:
        if x.lower() == "exit":
            value = False
        elif x.lower() == "add":
            add()
        elif x.lower() == "view":
            view()
        elif x.lower() == "edit":
            edit()
        elif x.lower() == "delete":
            delete()
    else:
        print("Wrong command!")

print("Nice day!")
