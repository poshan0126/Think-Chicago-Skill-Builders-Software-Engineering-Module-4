
from user_interface import UserInterface

def main():
    while True:
        city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
        if city.lower() == 'exit':
            break
        detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
        if detailed == 'yes':
            forecast = UserInterface.get_detailed_forecast(city)
        else:
            forecast = UserInterface.display_weather(city)
        print(forecast)

if __name__ == "__main__":
    main()
