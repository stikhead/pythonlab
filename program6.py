def main():
    phonebook = {}

    while True:
        print("\n" + "="*40)
        print("  DYNAMIC PHONEBOOK & CONTACT MANAGER  ")
        print("="*40)
        print("1. Add New Contact")
        print("2. Search Contacts (Dynamic Lookup using Comprehensions)")
        print("3. Update Existing Contact")
        print("4. Remove Contact")
        print("5. Display All Contacts (using .items())")
        print("6. Show All Contact Names (using .keys())")
        print("7. Extract All Phone Numbers (using .values() & Comprehension)")
        print("8. Exit")
        
        choice = input("\nSelect an option (1-8): ").strip()

        if choice == '1':
            name = input("Enter Name: ").strip()
            if name in phonebook:
                print(f"[Error] Contact '{name}' already exists! Use Option 3 to update.")
            else:
                phone = input("Enter Phone Number: ").strip()
                email = input("Enter Email Address: ").strip()
                group = input("Enter Group (e.g., Family, Work, Friend): ").strip()
                
                phonebook[name] = {'phone': phone, 'email': email, 'group': group}
                print(f"[Success] Contact '{name}' added dynamically.")

        elif choice == '2':
            query = input("Enter search keyword (name, phone, or group): ").strip().lower()
            
            search_results = [
                (k, v) for k, v in phonebook.items()
                if query in k.lower() or query in v['phone'] or query in v['group'].lower()
            ]
            
            if search_results:
                print(f"\n--- Search Results ({len(search_results)} found) ---")
                for contact_name, details in search_results:
                    print(f"Name: {contact_name} | Phone: {details['phone']} | Email: {details['email']} | Group: {details['group']}")
            else:
                print("[Info] No matching contacts found.")

        elif choice == '3':
            name = input("Enter the exact Name of the contact to update: ").strip()
            if name in phonebook:
                print(f"Current details for {name}: {phonebook[name]}")
                print("(Press Enter to keep the current value)")
                
                new_phone = input(f"New Phone [{phonebook[name]['phone']}]: ").strip()
                new_email = input(f"New Email [{phonebook[name]['email']}]: ").strip()
                new_group = input(f"New Group [{phonebook[name]['group']}]: ").strip()
                if new_phone: phonebook[name]['phone'] = new_phone
                if new_email: phonebook[name]['email'] = new_email
                if new_group: phonebook[name]['group'] = new_group
                
                print(f"[Success] Contact '{name}' updated successfully.")
            else:
                print(f"[Error] Contact '{name}' not found in directory.")

        elif choice == '4':
            name = input("Enter the exact Name of the contact to remove: ").strip()
            if name in phonebook:
                removed_data = phonebook.pop(name)
                print(f"[Success] Removed '{name}' from directory. (Data: {removed_data})")
            else:
                print(f"[Error] Contact '{name}' not found.")

        elif choice == '5':
            if not phonebook:
                print("[Info] The phonebook is currently empty.")
                continue
            
            print("\n--- Complete Directory ---")
            for contact_name, info in phonebook.items():
                print(f"{contact_name.ljust(15)} -> Phone: {info['phone']}, Email: {info['email']}, Group: {info['group']}")

        elif choice == '6':
            names = list(phonebook.keys())
            if names:
                print(f"\nSaved Contact Names: {', '.join(names)}")
            else:
                print("[Info] No names to display. Phonebook is empty.")

        elif choice == '7':
            phones = [info['phone'] for info in phonebook.values()]
            if phones:
                print(f"\nExtracted Phone Numbers: {', '.join(phones)}")
            else:
                print("[Info] No phone numbers to display.")

        elif choice == '8':
            print("Exiting Dynamic Phonebook Manager. Goodbye!")
            break

        else:
            print("[Error] Invalid choice. Please select a valid number from 1 to 8.")

if __name__ == "__main__":
    main()