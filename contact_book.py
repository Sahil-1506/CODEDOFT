import json

def load_contacts():
    try:
        with open('contacts.json', 'r') as f:
            contacts = json.load(f)
    except FileNotFoundError:
        contacts = {}
    return contacts

def save_contacts(contacts):
    with open('contacts.json', 'w') as f:
        json.dump(contacts, f, indent=4)

def add_contact(name, phone, email, contacts):
    contacts[name] = {'phone': phone, 'email': email}
    save_contacts(contacts)

def delete_contact(name, contacts):
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"{name} has been deleted from contacts.")
    else:
        print(f"{name} not found in contacts.")

def list_contacts(contacts):
    print("Contacts:")
    for name, info in contacts.items():
        print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")

def main():
    contacts = load_contacts()

    while True:
        print("\n1. Add Contact")
        print("2. Delete Contact")
        print("3. List Contacts")
        print("4. Exit")
        choice = input("Enter your choice : ")

        if choice == '1':
            name = input("Enter name : ")
            phone = input("Enter phone number : ")
            email = input("Enter email : ")
            add_contact(name, phone, email, contacts)
        elif choice == '2':
            name = input("Enter name to delete : ")
            delete_contact(name, contacts)
        elif choice == '3':
            list_contacts(contacts)
        elif choice == '4':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
