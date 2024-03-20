class Bus:
    city = "Default City"
    base_fare = 2.00

    def __init__(self, route_number, passenger_capacity):
        self.route_number = route_number
        self.passenger_capacity = passenger_capacity

def main():
    # Create bus instances
    bus1 = Bus(101, 50)
    bus2 = Bus(102, 60)

    # Access class and instance attributes
    print(f"Bus1 - City: {Bus.city}, Base Fare: {Bus.base_fare}, Route Number: {bus1.route_number}, Passenger Capacity: {bus1.passenger_capacity}")
    print(f"Bus2 - City: {Bus.city}, Base Fare: {Bus.base_fare}, Route Number: {bus2.route_number}, Passenger Capacity: {bus2.passenger_capacity}")

if __name__ == "__main__":
    main()

