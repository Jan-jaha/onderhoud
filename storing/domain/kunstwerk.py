import uuid
from typing import List


class Kunstwerk:
    """Value Object — beschrijft een kunstwerk binnen de storing context."""

    def __init__(self, id: uuid.UUID, naam: str, locatie: List, aannemer: str, type: str):
        self.__id = id
        self.__naam = naam
        self.__locatie = locatie
        self.__aannemer = aannemer
        self.__type = type

    @classmethod
    def verwerken(cls, data: dict) -> "Kunstwerk":
        # Zet een dict (bijv. van BeheerApi) om naar een Kunstwerk object
        return cls(
            id=uuid.UUID(data["id"]),
            naam=data["naam"],
            locatie=data["locatie"],
            aannemer=data["aannemer"],
            type=data["type"],
        )

    def get_id(self) -> uuid.UUID:
        return self.__id

    def get_naam(self) -> str:
        return self.__naam

    def get_locatie(self) -> List:
        return self.__locatie

    def get_aannemer(self) -> str:
        return self.__aannemer
