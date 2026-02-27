import json
import os

DATA_DIR = "data"
CONTACTS_FILE = os.path.join(DATA_DIR, "contacts.json")


def load_contacts():
    if not os.path.exists(CONTACTS_FILE):
        return []
    with open(CONTACTS_FILE, "r") as f:
        return json.load(f)


def save_contacts(contacts):
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f, indent=2)


def add_contact(contacts):
    name = input("Name: ")
    phone = input("Phone number: ")
    email = input("Email address: ")
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print("Contact added.")


def list_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    for contact in contacts:
        print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")


def main():
    contacts = load_contacts()
    while True:
        print("\n1. Add a contact")
        print("2. List all contacts")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            list_contacts(contacts)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
