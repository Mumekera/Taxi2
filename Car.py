import random

class Car:
    def __init__(self, brand):
        self.brand = brand
        self.status = True  # True = wolny, False = zajęty
        self.district = ""
        
    district_distances = {
        "Retkinia": -4,
        "Łódź Kaliska": -2,
        "Śródmieście": 0,
        "Widzew": 5,
        "Janów": 7
    }

    def assign_districts(self, districts):
        self.district = random.choice(districts)
        

    # Losowo przypisuje dzielnice do auta

    def assign_random_district():
        brands = [
                "Ford Mondeo",
                "Dacia Logan",
                "Toyota Avensis",
                "Mercedes E220",
                "Hyundai Lantra"
        ]
        districts = list(Car.district_distances.keys())
        cars = [Car(brand) for brand in brands]
        
        for car in cars:
            car.assign_districts(districts)

        return cars


    def compare_distance(car, customer_district):
        if car.status and car.district:
            distance = Car.district_distances[car.district]
            customer_distance = Car.district_distances[customer_district]
            return abs(distance - customer_distance)
        
        
    # 1 km = 4 minuty, 0 km = 3 minuty
        
    def calculate_time_of_arrival(distance):
        if distance == 0:
            return 3  
        else:
            return abs(distance) * 4  