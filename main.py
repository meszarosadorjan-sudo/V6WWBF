from Autokolcsonzo import Autokolcsonzo
from Teherauto import Teherauto
from Szemelyauto import Szemelyauto
import os

def terminal_torles():
    # Windows esetén 'cls', Linux/Mac esetén 'clear' parancsot futtat
    os.system('cls' if os.name == 'nt' else 'clear')

terminal_torles() #Induláskor tiszta képernyő legyen

class KolcsonzoRendszer:
    def __init__(self):
        self._bazis = Autokolcsonzo("5 kerék autó kölcsönző")
        self._init_data()

    def _init_data(self):
        self._bazis.autok = Szemelyauto("RFV100", "OPEL", 10000)
        self._bazis.autok = Szemelyauto("RFV101", "TOYOTA", 20000)
        self._bazis.autok = Teherauto("RTZ100", "UAZ", 30000)
        self._bazis.upload_foglalas("RFV100")
        self._bazis.upload_foglalas("RFV101")
        self._bazis.upload_foglalas("RTZ100")

        
    def user_interact(self):
        while True:
            print("*******************************")
            print("1. Gépjárművek listázása")
            print("2. Gépjármű foglalása")
            print("3. Gépjármű foglalás lemondása")
            print("4. Kilépés")
            print("*******************************")

            menu = input("Válassz a fenti menüpontokból: ")

            if menu == "1":
                terminal_torles()
                self._bazis.autok
            elif menu == "2":
                rendszam = input("Add meg a gépjármű rendszámát: ").upper()
                self._bazis.booking_by_license_plate(rendszam)
            elif menu == "3":
                rendszam = input("Add meg a gépjármű rendszámát: ").upper()
                self._bazis.unbooking_by_license_plate(rendszam)
            elif menu == "4":
                terminal_torles()
                break
            else:
                terminal_torles()
                print("Nem megfelelő menüpontot választott ki!")
        
booking_system = KolcsonzoRendszer()
booking_system.user_interact()
