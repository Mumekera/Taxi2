from Messages import Messages
from Car import Car


def main():
   
    cars = Car.assign_random_district()
    
    while True:
        print(Messages.main_menu)
        choice = input()

        if choice == '1':
            Messages.show_districts()
        elif choice == '2':
            Messages.show_available_cars(cars)
        elif choice == '3':
            Messages.show_reservation_screen(cars)
        elif choice == "4":
            print("Wychodzenie z aplikacji.")
            break
        else:
            print("Niepoprawny wybór. Proszę wcisnąc poprawny klawisz")

if __name__ == "__main__":
    main()