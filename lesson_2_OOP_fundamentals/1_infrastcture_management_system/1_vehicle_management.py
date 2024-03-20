class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner

    def update_owner(self, new_owner):
        self.owner = new_owner
        print(f"The owner of the vehicle with registration number {self.registration_number} has been updated to {new_owner}.")

def main():
    # Create instances of Vehicle
    vehicle1 = Vehicle("123ABC", "Car", "Jay")
    vehicle2 = Vehicle("456DEF", "Motorcycle", "Poshan")

    # Display initial owners
    print(f"Initial owner of vehicle1: {vehicle1.owner}")
    print(f"Initial owner of vehicle2: {vehicle2.owner}")

    # Update owners
    vehicle1.update_owner("Poshan")
    vehicle2.update_owner("Jay")

    # Display updated owners
    print(f"Updated owner of vehicle1: {vehicle1.owner}")
    print(f"Updated owner of vehicle2: {vehicle2.owner}")

if __name__ == "__main__":
    main()
