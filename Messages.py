from Car import district_distances, get_closest_car

class Messages:
    MAIN_MENU = """
    Taxi Reservation System
    1. Show list of districts
    2. Show list of cars
    3. Show reservation screen
    4. Exit
    Enter your choice: """

    district_list = """
    List of Districts:
    1. Retkinia (4 km from the center)
    2. Łódź Kaliska (2 km from the center)
    3. Śródmieście (0 km from the center)
    4. Widzew (5 km from the center)
    5. Janów (7 km from the center)
    """

    reservation_screen = "Reservation Screen"

    def show_districts():
        print(Messages.district_list)

    def show_reservation_screen(cars):
        print(Messages.reservation_screen)
        
        while True:
            district_choice_input = input("Enter the district number you want to reserve a taxi in: ")
            if not district_choice_input.isdigit():
                print("Please enter a number between 1 and 5.")
                continue
            
            district_choice = int(district_choice_input)
            
            if 1 <= district_choice <= 5:
                chosen_district = list(district_distances.keys())[district_choice - 1]
                closest_car = get_closest_car(cars, chosen_district)
                if closest_car:
                        print(f"Taxi reserved in {chosen_district} district. Closest available car: {closest_car.brand}")
                        break
                else:
                        print(f"No available cars")
                        break
            else:
                    print("Invalid district choice.")
                

    
    def show_available_cars(cars):
        print("Available Cars and Their Locations:")
        for car in cars:
            status = "Free" if car.status else "Busy"
            print(f"Car: {car.brand}, District: {car.district}, Distance from center: {district_distances[car.district]} km, Status: {status}")