class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone_number):
        self.contacts.append({"Name": name, "Phone Number": phone_number})
        print("Contact added successfully.")

    def remove_contact(self, name):
        for contact in self.contacts:
            if contact["Name"] == name:
                self.contacts.remove(contact)
                print("Contact removed successfully.")
                return
        print("Contact not found.")

    def display_contacts(self):
        if self.contacts:
            print("Contacts:")
            for contact in self.contacts:
                print(f"Name: {contact['Name']}, Phone Number: {contact['Phone Number']}")
        else:
            print("No contacts found.")
