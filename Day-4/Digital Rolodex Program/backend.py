contacts = {}
print("=== Digital Rolodex Setup ===")

num_contacts = int(input("How many contacts would you like to add initially? "))
for i in range(num_contacts):
    print(f"\nContact {i+1}:")
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    contacts[name] = phone

print("\n" + "="*40)
print("=== Digital Rolodex Menu ===")

while True:
    print("\nOptions:")
    print("1. View all contacts")
    print("2. Add/Update a contact")
    print("3. Look up a contact")
    print("4. Exit")
    
    choice = input("\nEnter your choice (1-4): ")
    
    if choice == '1':
        print("\n" + "="*40)
        print("ALL CONTACTS:")
        if contacts:
            for name, phone in contacts.items():
                print(f"Contact: {name} | Phone: {phone}")
        else:
            print("No contacts yet!")
        print("="*40)
    
    elif choice == '2':
        print("\n" + "="*40)
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
        print(f"✓ Contact '{name}' saved/updated!")
        print("="*40)
    
    elif choice == '3':
        print("\n" + "="*40)
        name = input("Enter name to look up: ")
        result = contacts.get(name, "Contact not found")
        
        if result == "Contact not found":
            print(result)
        else:
            print(f"Contact: {name} | Phone: {result}")
        print("="*40)
    
    elif choice == '4':
        print("\n" + "="*40)
        print("Goodbye! Here are your final contacts:")
        if contacts:
            for name, phone in contacts.items():
                print(f"Contact: {name} | Phone: {phone}")
        else:
            print("No contacts saved.")
        print("="*40)
        break
    
    else:
        print("Invalid choice! Please enter 1-4.")