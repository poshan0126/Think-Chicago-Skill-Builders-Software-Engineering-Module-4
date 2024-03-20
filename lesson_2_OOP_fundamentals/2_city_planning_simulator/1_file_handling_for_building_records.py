import json

class Building:
    def __init__(self, name, floors):
        self.name = name
        self.floors = floors

    def to_dict(self):
        return {
            'name': self.name,
            'floors': self.floors
        }

    
    def from_dict(source):
        return Building(source['name'], source['floors'])

    
    def save_to_file(buildings, filename):
        data = [building.to_dict() for building in buildings]
        with open(filename, 'w') as f:
            json.dump(data, f)

    
    def load_from_file(filename):
        with open(filename, 'r') as f:
            data = json.load(f)
        return [Building.from_dict(building) for building in data]
def main():
    # Create some buildings
    buildings = [
        Building("Building A", 10),
        Building("Building B", 20),
        Building("Building C", 30),
    ]

    # Save buildings to a file
    Building.save_to_file(buildings, 'buildings.json')

    # Load buildings from a file
    loaded_buildings = Building.load_from_file('buildings.json')

    # Print loaded buildings
    for building in loaded_buildings:
        print(f"Name: {building.name}, Floors: {building.floors}")

if __name__ == "__main__":
    main()
