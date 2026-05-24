from abc import ABC,abstractmethod 
# Definiálja az autó alapvető attribútumait (rendszám, típus, bérleti díj).
class Auto(ABC):
    def __init__(self,rendszam, tipus, berleti_dij):
        self._rendszam = rendszam
        self._tipus = tipus
        self._berleti_dij = berleti_dij
        self._berlesek = []
    
@abstractmethod
def book_room(self):
    pass

@abstractmethod
def unbook_room(self):
    pass   