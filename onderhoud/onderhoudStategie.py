import uuid
from typing import List
from onderhoud.database.stategie import Strategie

class OnderhoudStrategie:
    def __init__(self, id: uuid.UUID, kunstwerk_id: uuid.UUID, frequentie: int, onderhoudeisen: List[str]):
        self.__id = id
        self.__kunstwerk_id = kunstwerk_id
        self.__frequentie = frequentie
        self.__onderhoudeisen = onderhoudeisen

    @classmethod
    def json_verwerken(cls, data: dict) -> "OnderhoudStrategie":
        return cls(
            id=uuid.UUID(data["id"]),
            kunstwerk_id=uuid.UUID(data["kunstwerk_id"]),
            frequentie=data["frequentie"],
            onderhoudeisen=data["onderhoudeisen"]
        )
    
    def set_database(self, kunstwerk_id: str, frequentie: int, onderhoudeisen: list):
        strategie = Strategie(
            kunstwerk_id=kunstwerk_id,
            frequentie=frequentie,
            onderhoudeisen=onderhoudeisen
        )
        strategie.toevoegen(kunstwerk_id, frequentie, onderhoudeisen)

    def get_id(self) -> uuid.UUID:
        return self.__id

    def get_kunstwerk_id(self) -> uuid.UUID:
        return self.__kunstwerk_id

    def get_onderhoudeisen(self) -> List[str]:
        return self.__onderhoudeisen