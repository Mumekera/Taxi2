from Messages import Message
from Car import Car

def main():
    message = Message()
    
    while True:
        choice = message.starting_screen()
        choice = int(choice)

        if choice == 1:
            message.list_of_districts()
        elif choice == 2:
            message.reservation_screen()
        elif choice == 3:
            print("ZAKOŃCZONO PROGRAM")
            break
        else:
            print("Niepoprawny wybór. Wprowadź 1, 2 lub 3.")

if __name__ == "__main__":
    main()