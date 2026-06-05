def save_contacts():
    file=open("contacts.txt", "w")
    for contact in contacts:
        file.write(
            contact["name"] + ","+
str(contact["phone"]) + "," +
contact["email"] + "\n"
        )
    file.close()
    print("Contacts saved!")

contacts=[]
def add_contact():
    name =input("Enter name: ")
    try:
        phone=int(input("Enter phone no: "))
    except:
        print("Invalid number!")
        return
    email = input("Enter email address: ")
    contact={
        "name" : name,
        "phone" : phone,
        "email" : email
    }
    contacts.append(contact)
    print("Contact added successfully!")
def view_contacts():
    for contact in contacts:
        print(
            "Name: ", contact["name"],
            "| Phone no: ", contact["phone"],
            "| Email: ", contact["email"]
        )
def search_contact():
    name = input("Enter contact name: ")
    for contact in contacts:
        if contact["name"] == name:
            print( "Name: ", contact["name"],
            "| Phone no: ", contact["phone"],
            "| Email: ", contact["email"]
        )
            return
    print("Contact not found!")
def delete_contact():
    name= input("Enter contact name to delete: ")
    for contact in contacts:
        if contact["name"] == name:
            contacts.remove(contact)
            print("Contact deleted successfully!")
            return
    print("Contact not found!")
def load_contacts():
    file=open("contacts.txt", "r")
    for line in file:
        data=line.strip().split(",")
        contact={
            "name" : data[0],
            "phone" : int(data[1]),
            "email" : data[2]
             }
        contacts.append(contact)
    file.close()
load_contacts()
while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Save Contact")
    print("6. Exit")

    choice = input("Enter choice: ")
    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        save_contacts()
    elif choice == "6":    
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")