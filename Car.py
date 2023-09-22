import random

class Car:
    def __init__(self, brand):
        self.brand = brand
        self.status = True  # True for free, False for busy
        self.district = ""

    def assign_districts(self, districts):
        self.district = random.choice(districts)

def get_closest_car(cars, district):
    closest_car = None
    min_distance = float('inf')

    for car in cars:
        if car.status and car.district:
            distance = district_distances[car.district]
            if distance < min_distance:
                min_distance = distance
                closest_car = car

    if closest_car:
        closest_car.status = False

    return closest_car


district_distances = {
    "Retkinia": -4,
    "Łódź Kaliska": -2,
    "Śródmieście": 0,
    "Widzew": 5,
    "Janów": 7
}


def create_random_cars():
    brands = [
            "Ford Mondeo",
            "Dacia Logan",
            "Toyota Avensis",
            "Mercedes E220",
            "Hyundai Lantra"
    ]
    districts = list(district_distances.keys())
    cars = [Car(brand) for brand in brands]

    for car in cars:
        car.assign_districts(districts)

    return cars
