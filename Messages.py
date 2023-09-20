from District import District
import time
import keyboard

class Message:
    def __init__(self):
        self.start_district = District()

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
        userchoice = input(" WYBIERZ 1, 2 LUB 3:")
        clear_screen()
        return userchoice
        
    def list_of_districts(self):
        districts = self.start_district.Districts
        for numeral, key in enumerate(districts.keys(), start=1):
            print (f"{numeral}. {key}")

    def reservation_screen(self):
        print()
        print("PROSZĘ PODAĆ NUMER DZIELNICY DO KTÓREJ CHCESZ WEZWAĆ TAKSÓWKĘ:")
        self.list_of_districts()
        userchoice = input("\nTaksówka już do ciebie jedzie")
        self.clear_screen_after_delay_or_input()
        return userchoice

def clear_screen():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def clear_screen_after_delay_or_input(self):
        delay = 5  # 5 seconds delay
        start_time = time.time()
        while True:
            current_time = time.time()
            if current_time - start_time >= delay:
                self.clear_screen()
                break
            if keyboard.is_pressed('enter'):  # Check if Enter key is pressed
                self.clear_screen()
                break
            time.sleep(0.1)