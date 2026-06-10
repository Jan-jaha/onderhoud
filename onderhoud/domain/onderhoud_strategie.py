import uuid
from typing import List


class OnderhoudStrategie:
    """Entity — bevat de strategie (frequentie + eisen) voor onderhoud aan een kunstwerk."""

    def __init__(self, id: uuid.UUID, kunstwerk_id: uuid.UUID, frequentie: int, onderhoudeisen: List[str]):
        self.__id = id
        self.__kunstwerk_id = kunstwerk_id
        self.__frequentie = frequentie
        self.__onderhoudeisen = onderhoudeisen

    @classmethod
    def verwerken(cls, data: dict) -> "OnderhoudStrategie":
        # Zet een dict om naar een OnderhoudStrategie object
        return cls(
            id=uuid.UUID(data["id"]),
            kunstwerk_id=uuid.UUID(data["kunstwerk_id"]),
            frequentie=data["frequentie"],
            onderhoudeisen=data["onderhoudeisen"],
        )

    def get_id(self) -> uuid.UUID:
        return self.__id

    def get_kunstwerk_id(self) -> uuid.UUID:
        return self.__kunstwerk_id

    def get_frequentie(self) -> int:
        return self.__frequentie

    def get_onderhoudeisen(self) -> List[str]:
        return self.__onderhoudeisen
