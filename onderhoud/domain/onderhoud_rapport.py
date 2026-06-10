import uuid
from typing import List

from onderhoud.domain.kunstwerk import Kunstwerk


class OnderhoudRapport:
    """Entity — rapportage van een uitgevoerd onderhoud."""

    def __init__(
        self,
        onderhoud_id: uuid.UUID,
        kunstwerk: Kunstwerk,
        beschrijving: str,
        aannemer: str,
        type: str,
    ):
        self.__id = uuid.uuid4()
        self.__onderhoud_id = onderhoud_id
        self.__kunstwerk = kunstwerk
        self.__beschrijving = beschrijving
        self.__aannemer = aannemer
        self.__type = type

    def get_id(self) -> uuid.UUID:
        return self.__id

    def get_naam(self) -> str:
        return self.__kunstwerk.get_naam()

    def get_aannemer(self) -> str:
        return self.__aannemer

    def get_locatie(self) -> List:
        return self.__kunstwerk.get_locatie()

    def get_beschrijving(self) -> str:
        return self.__beschrijving
