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
    print("\nGreat! Let's add a new contact.")
    name = input("What's their name? ")
    phone = input("What's their phone number? ")
    email = input("And their email address? ")
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print(f"Got it! {name} has been added to your contacts.")


def list_contacts(contacts):
    if not contacts:
        print("Your contact list is empty. Add someone to get started!")
        return
    print("\nHere are all your contacts:")
    for contact in contacts:
        print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")


def main():
    contacts = load_contacts()
    while True:
        print("\nWhat would you like to do?")
        print("  1. Add a contact")
        print("  2. List all contacts")
        print("  3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            list_contacts(contacts)
        elif choice == "3":
            break
        else:
            print("That's not a valid option. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
