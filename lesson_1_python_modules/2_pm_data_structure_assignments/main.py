from contacts_manager import ContactManager
from datetime import datetime

def display_current_month_and_year():
    now = datetime.now()
    print(f"Current month: {now.strftime('%B')} {now.year}")

def parse_date_string(date_string):
    try:
        parsed_date = datetime.strptime(date_string, "%Y-%m-%d")
        print("Parsed date:", parsed_date)
    except ValueError:
        print("Invalid date!")

def datetimeMain():
    display_current_month_and_year()
    date_string = input("Enter a date (YYYY-MM-DD): ")
    parse_date_string(date_string)

def contactMain():
    contact_manager = ContactManager()
    while True:
        print("\nMenu:")
        print("1. Add Contact")
        print("2. Remove Contact")
        print("3. Display Contacts")
        print("4. Quit")
        choice = input("Enter your choice: ")
        if choice == '1':
            name = input("Enter contact name: ")
            phone_number = input("Enter phone number: ")
            contact_manager.add_contact(name, phone_number)
        elif choice == '2':
            name = input("Enter contact name to remove: ")
            contact_manager.remove_contact(name)
        elif choice == '3':
            contact_manager.display_contacts()
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")
def main():
    contactMain()
    datetimeMain()
if __name__ == "__main__":
    main()
