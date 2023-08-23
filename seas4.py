#YOUR Python Code...
class FlightDetails:
    def __init__(self, flight_id, source, destination, price):
        self.flight_id = flight_id
        self.source = source
        self.destination = destination
        self.price = price

class FlightTable:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def search_by_city(self, city):
        result = []
        for flight in self.flights:
            if flight.source == city or flight.destination == city:
                result.append(flight)
        return result

    def search_by_source(self, source):
        result = []
        for flight in self.flights:
            if flight.source == source:
                result.append(flight)
        return result

    def search_between_cities(self, source, destination):
        result = []
        for flight in self.flights:
            if flight.source == source and flight.destination == destination:
                result.append(flight)
        return result

def main():
    flight_table = FlightTable()

    # Adding flights to the flight table
    flight_table.add_flight(FlightDetails("AI161E90", "BLR", "BOM", 5600))
    flight_table.add_flight(FlightDetails("BR161F91", "BOM", "BBI", 6750))
    flight_table.add_flight(FlightDetails("AI161F99", "BBI", "BLR", 8210))
    flight_table.add_flight(FlightDetails("VS171E20", "JLR", "BBI", 5500))
    flight_table.add_flight(FlightDetails("AS171G30", "HYD", "JLR", 4400))
    flight_table.add_flight(FlightDetails("AI131F49", "HYD", "BOM", 3499))

    while True:
        print("Flight Search Options:")
        print("1. Search flights for a specific city")
        print("2. Search flights departing from a city")
        print("3. Search flights between two cities")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            city = input("Enter the city name: ")
            result = flight_table.search_by_city(city)
            print("\nSearch Results:")
            for flight in result:
                print(f"Flight ID: {flight.flight_id}, From: {flight.source}, To: {flight.destination}, Price: {flight.price}")
        
        elif choice == 2:
            source = input("Enter the source city: ")
            result = flight_table.search_by_source(source)
            print("\nSearch Results:")
            for flight in result:
                print(f"Flight ID: {flight.flight_id}, From: {flight.source}, To: {flight.destination}, Price: {flight.price}")
        
        elif choice == 3:
            source = input("Enter the source city: ")
            destination = input("Enter the destination city: ")
            result = flight_table.search_between_cities(source, destination)
            print("\nSearch Results:")
            for flight in result:
                print(f"Flight ID: {flight.flight_id}, From: {flight.source}, To: {flight.destination}, Price: {flight.price}")
        
        elif choice == 4:
            break
        
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
