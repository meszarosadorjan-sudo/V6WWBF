from Auto import Auto
from datetime import datetime
from datetime import date
import os

def terminal_torles():
    # Windows esetén 'cls', Linux/Mac esetén 'clear' parancsot futtat
    os.system('cls' if os.name == 'nt' else 'clear')

class Szemelyauto(Auto):

    def __init__(self, rendszam, tipus, berleti_dij):
        super().__init__(rendszam, tipus, berleti_dij)
        
    @property
    def rendszam(self):
        return self._rendszam
    
    @property
    def tipus(self):
        return self._tipus
    
    @property
    def berleti_dij(self):
        return self._berleti_dij
    
    @property
    def kiadva(self):
        return self._kiadva
 
    @property
    def foglalasok(self):
        return self._foglalasok

        
    def booking_car(self):
        while True:
            try:
                datum_szoveg = input("Adj meg egy dátumot (ÉÉÉÉHHNN formátumban, pl. 20260525): ")
                datum_ellenorzes = datetime.strptime(datum_szoveg, "%Y%m%d")
        
                # Mai dátum lekérése számként az összehasonlításhoz
                mai_datum_szam = int(datetime.now().strftime("%Y%m%d"))
                megadott_datum_szoveg = int(datum_szoveg)
        
                if megadott_datum_szoveg >= mai_datum_szam:
                    # Ellenőrzés, hogy szerepel-e foglalások között a dátum
                    mar_foglalt = any(lista[0] == datum_szoveg for lista in self._foglalasok)
            
                    if not mar_foglalt:
                        ugyfel = input("Adja meg az ügyfél nevét: ")
                        self._foglalasok.append([datum_szoveg, ugyfel])
                
                        terminal_torles()
                        print("Sikeresen lefoglalta a gépjárművet!")
                        break
                    else:
                        print("Ez a dátum már foglalt! Kérjük, válasszon másikat.")
                
                else:
                    print("A megadott dátum korábbi a mai napnál!")
            
            except ValueError:
                print("Hibás adatbevitel / dátumformátum! Használja az ÉÉÉÉHHNN formátumot!")

    def unbooking_car(self):
        if not self._foglalasok:
            terminal_torles()
            print("Jelenleg nincs foglalás erre a gépjárműre!")
            
        else:
            n = 0
            for lista in self._foglalasok:
                print(f"{n}.\t{lista}")
                n = n+1
            print("-----------------------------")
            while True:
                try:
                    valasztas = int(input("Melyik foglalást szeretné törölni? "))
                    if 0 <= valasztas <= n:
                        del self._foglalasok[valasztas]
                        terminal_torles()
                        print("Sikeresen törölte a foglalást a gépjárműröl!")
                        break
                except ValueError:
                    print("Hiba: Nem megfelelő érték, válassz újra!")
    
    def upload(self):
        if self._rendszam == "RFV100":
            self._foglalasok.append(["20261010", "Józsi bácsi"])
        if self._rendszam == "RFV101":
            self._foglalasok.append(["20261010", "Béla bácsi"])
            self._foglalasok.append(["20261110", "Jani bácsi"])

