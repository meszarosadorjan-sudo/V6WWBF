import os

def terminal_torles():
    # Windows esetén 'cls', Linux/Mac esetén 'clear' parancsot futtat
    os.system('cls' if os.name == 'nt' else 'clear')

class Autokolcsonzo:
    def __init__(self, name):
        self._name = name
        self._autok = []

    @property
    def name(self):
        return self._name

    @property
    def foglalasok(self):
        return self._foglalasok
    
    @property
    def autok(self):
        for car in self._autok:
            print(f"Rendszám: {car.rendszam}\t| Típus: {car.tipus}\t| Bérleti díj: {car.berleti_dij}")
            if not car.foglalasok:
                print("Jelenleg nincs foglalás a gépjárműre!")
                print("-\t-\t-\t-\t-\t-\t-\t-\t-")
            else:
                print(f"A következő foglalások vannak rögzítve:")
                for lista in car.foglalasok:
                    print(lista)
                print("-\t-\t-\t-\t-\t-\t-\t-\t-")
# Adatfeltöltéshez szükséges
    @autok.setter
    def autok(self, new_cars):
        self._autok.append(new_cars)
        
    def upload_foglalas(self, rendszam):
        for car in self._autok:
            if car.rendszam == rendszam:
                car.upload()
                
    def booking_by_license_plate(self, rendszam):
        for car in self._autok:
            if car.rendszam == rendszam:
                car.booking_car()
                break
        else:
            terminal_torles()
            print("Helytelen adatbevitel / nem létező rendszám!")
            
    def unbooking_by_license_plate(self, rendszam):
        for car in self._autok:
            if car.rendszam == rendszam:
                car.unbooking_car()
                break
        else:
            terminal_torles()
            print("Helytelen adatbevitel / nem létező rendszám!")           

