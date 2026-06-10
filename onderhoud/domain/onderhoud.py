import uuid
from datetime import date

from shared.domain.enums import OnderhoudStatus
from onderhoud.domain.onderhoud_strategie import OnderhoudStrategie
from onderhoud.domain.kunstwerk import Kunstwerk
from onderhoud.domain.onderhoud_rapport import OnderhoudRapport


class Onderhoud:
    """Aggregate Root — beheert de volledige levenscyclus van een onderhoudstaak."""

    def __init__(
        self,
        id: uuid.UUID,
        strategie: OnderhoudStrategie,
        kunstwerk: Kunstwerk,
        startdatum: date,
        einddatum: date,
        aannemer: str,
        type: str,
    ):
        self.__id = id
        self.__strategie = strategie
        self.__kunstwerk = kunstwerk
        self.__startdatum = startdatum
        self.__einddatum = einddatum
        self.__aannemer = aannemer
        self.__type = type
        self.__status = OnderhoudStatus.INGEPLAND
        self.__rapport: OnderhoudRapport | None = None

    def maak_rapport(self, beschrijving: str) -> OnderhoudRapport:
        # Maakt een rapport aan voor dit onderhoud na uitvoering
        self.__rapport = OnderhoudRapport(
            onderhoud_id=self.__id,
            kunstwerk=self.__kunstwerk,
            beschrijving=beschrijving,
            aannemer=self.__aannemer,
            type=self.__type,
        )
        return self.__rapport

    def set_status(self, status: OnderhoudStatus) -> None:
        self.__status = status

    def get_id(self) -> uuid.UUID:
        return self.__id

    def get_status(self) -> OnderhoudStatus:
        return self.__status

    def get_aannemer(self) -> str:
        return self.__aannemer

    def get_kunstwerk(self) -> Kunstwerk:
        return self.__kunstwerk

    def get_strategie(self) -> OnderhoudStrategie:
        return self.__strategie

    def get_rapport(self) -> OnderhoudRapport | None:
        return self.__rapport
