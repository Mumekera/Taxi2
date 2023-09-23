from Car import Car


class Messages:
    main_menu = """
Program do rezerwacji taxi
1. Pokaż listę dzielnic
2. Pokaż listę taksówek
3. Ekran rezerwacji
4. Wyjście
Twój wybór: 
"""

    district_list = """
Lista dzielnic
1. Retkinia (4 km od centrum)
2. Łódź Kaliska (2 km od centrum)
3. Śródmieście (0 km od centrum)
4. Widzew (5 km od centrum)
5. Janów (7 km od centrum)
"""

    reservation_screen = "EKRAN REZERWACJI"

    def show_districts():
        print(Messages.district_list)


    #Lista dostępnych samochodów
    
    def show_available_cars(cars):
        print("Dostępne taksówki i ich lokalizacja:")
        for car in cars:
            status = "Wolny" if car.status else "Zajęty"
            print(f"Taxi: {car.brand}, Dzielnica: {car.district}, Dystans od centrum: {Car.district_distances[car.district]} km, Status: {status}")
            
            
    #Ekran rezerwacji
        
    def show_reservation_screen(cars):
        print(Messages.reservation_screen)
        print("""
    Lista dzielnic
    1. Retkinia 
    2. Łódź Kaliska 
    3. Śródmieście 
    4. Widzew 
    5. Janów 
    """)

        while True:
            district_choice_input = input("Proszę podać numer dzielnicy do której zamawiana jest taksówka: ")

            if not district_choice_input.isdigit():
                print("Proszę podać liczbę od 1 do 5.")
                continue

            district_choice = int(district_choice_input)
            
            if 1 <= district_choice <= 5:
                chosen_district = list(Car.district_distances.keys())[district_choice - 1]
                closest_car = min(cars, key=lambda car: Car.compare_distance(car, chosen_district))
                if closest_car:
                    print(f"Taxi zarezerwowana do {chosen_district}. Najbliższy dostępny samochód: {closest_car.brand}")
                    time_to_arrival = Car.calculate_time_of_arrival(Car.compare_distance(closest_car, chosen_district))
                    print(f"Do celu: {time_to_arrival} minut/y")
                    closest_car.status = False
                else:
                    print("Brak dostępnych samochodów")
                break
            else:
                print("Proszę podać liczbę od 1 do 5.")