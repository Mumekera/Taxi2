from Messages import Messages
from Car import create_random_cars

cars = create_random_cars()

def main():
    
    while True:
        print(Messages.MAIN_MENU)
        choice = input()

        if choice == '1':
            Messages.show_districts()
        elif choice == '2':
            Messages.show_available_cars(cars)
        elif choice == '3':
            Messages.show_reservation_screen(cars)
        elif choice == "4":
            print("Exiting the app.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()