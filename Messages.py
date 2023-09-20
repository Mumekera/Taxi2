from Car import Car

class Message:
    def __init__(self):
        self.start_car = Car()

    def starting_screen(self):
        print()
        print("WYBIERZ OPCJĘ:")
        print()
        print("1 => LISTA WSZYSTKICH DZIELNIC I TAKSÓWEK")
        print()
        print("2 => ZAMÓW TAKSÓWKĘ")
        print()
        print("3 => ZAKOŃCZ PROGRAM")
        print()
        userchoice = input(" WYBIERZ 1, 2 LUB 3: ")
        clear_screen()
        return userchoice
        
    def list_of_districts(self):
        districts = self.start_car.District
        for numeral, key in enumerate(districts.keys(), start=1):
            print (f"{numeral}. {key}")

    def reservation_screen(self):
        print()
        print("PROSZĘ PODAĆ NUMER DZIELNICY DO KTÓREJ CHCESZ WEZWAĆ TAKSÓWKĘ:")
        self.list_of_districts()
        userchoice = input()
        clear_screen()
        return userchoice

def clear_screen():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')