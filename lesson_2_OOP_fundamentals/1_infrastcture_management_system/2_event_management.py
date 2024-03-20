class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participant_count = 0

    def add_participant(self):
        self.participant_count += 1
        print(f"A participant has been added to the event {self.name}. Total participants: {self.participant_count}")

    def get_participant_count(self):
        return self.participant_count
def main():
    # Create an event
    event = Event("Lolapolaoza", "2024-07-10")

    # Add participants
    event.add_participant()
    event.add_participant()

    # Get participant count
    print(f"Participant count for {event.name}: {event.get_participant_count()}")

if __name__ == "__main__":
    main()
