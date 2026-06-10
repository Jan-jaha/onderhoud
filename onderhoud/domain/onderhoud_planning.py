import uuid
from datetime import date
from typing import List

from shared.domain.enums import OnderhoudStatus
from onderhoud.domain.onderhoud_strategie import OnderhoudStrategie
from onderhoud.domain.kunstwerk import Kunstwerk


class OnderhoudPlanning:
    """Entity — houdt bij wanneer onderhoud gepland is en wanneer het uitgevoerd moet worden."""

    def __init__(
        self,
        id: uuid.UUID,
        strategie: OnderhoudStrategie,
        kunstwerk: Kunstwerk,
        frequentie: int,
        onderhoudeisen: List[str],
        laatste_uitvoering: date,
    ):
        self.__id = id
        self.__kunstwerk_id = kunstwerk.get_id()
        self.__strategie_id = strategie.get_id()
        self.__frequentie = frequentie
        self.__onderhoudeisen = onderhoudeisen
        self.__laatste_uitvoering = laatste_uitvoering
        self.__volgende_uitvoering = self.bereken_volgende_datum(laatste_uitvoering, frequentie)
        self.__status = OnderhoudStatus.INGEPLAND

    def is_het_tijdstip(self, vandaag: date) -> bool:
        # Geeft True als de geplande uitvoerdatum bereikt of verstreken is
        return vandaag >= self.__volgende_uitvoering

    def update_na_uitvoering(self, uitvoerdatum: date) -> date:
        # Werkt de planning bij na uitvoering en berekent de volgende datum
        self.__laatste_uitvoering = uitvoerdatum
        self.__volgende_uitvoering = self.bereken_volgende_datum(uitvoerdatum, self.__frequentie)
        self.__status = OnderhoudStatus.IS_UITGEVOERD
        return self.__volgende_uitvoering

    @staticmethod
    def bereken_volgende_datum(laatste_uitvoering: date, frequentie_dagen: int) -> date:
        # Berekent de volgende uitvoerdatum op basis van frequentie in dagen
        from datetime import timedelta
        return laatste_uitvoering + timedelta(days=frequentie_dagen)

    def get_id(self) -> uuid.UUID:
        return self.__id

    def get_kunstwerk_id(self) -> uuid.UUID:
        return self.__kunstwerk_id

    def get_strategie_id(self) -> uuid.UUID:
        return self.__strategie_id

    def get_volgende_uitvoering(self) -> date:
        return self.__volgende_uitvoering

    def get_laatste_uitvoering(self) -> date:
        return self.__laatste_uitvoering

    def get_status(self) -> OnderhoudStatus:
        return self.__status

    def get_onderhoudeisen(self) -> List[str]:
        return self.__onderhoudeisen
