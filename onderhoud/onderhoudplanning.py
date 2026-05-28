import uuid
from typing import List
import datetime

class OnderhoudPlanning:
    def __init__(self, id: uuid.UUID, kunstwerk_id: uuid.UUID, frequentie: int, onderhoudeisen: List[str], laatste_uitgevoerd: datetime, volgende_uitvoering: datetime, status: str):
        self.__id = id
        self.__kunstwerk_id = kunstwerk_id
        self.__frequentie = frequentie
        self.__onderhoudeisen = onderhoudeisen
        self.__laatste_uitgevoerd = laatste_uitgevoerd
        self.__volgende_uitvoering = volgende_uitvoering
        self.__status = status

        @classmethod
        def is_het_tijd(datum: datetime):
            datum = datetime.datetime.now()
            return True
        
        def update_na_uitgevoerd(self, datum: datetime):
            