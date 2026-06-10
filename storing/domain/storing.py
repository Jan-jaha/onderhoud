import uuid

from shared.domain.enums import PrioriteitStatus, StatusStatus
from storing.domain.storing_inspectie import StoringInspectie
from storing.domain.storing_rapport import StoringRapport
from storing.domain.kunstwerk import Kunstwerk


class Storing:
    """Aggregate Root — beheert de volledige afhandeling van een storing aan een kunstwerk."""

    def __init__(
        self,
        id: uuid.UUID,
        inspectie: StoringInspectie,
        kunstwerk: Kunstwerk,
        beschrijving: str,
    ):
        self.__id = id
        self.__storing_inspectie_id = inspectie.get_id()
        self.__kunstwerk = kunstwerk
        self.__beschrijving = beschrijving
        self.__prioriteit = inspectie.get_prioriteit()
        self.__status = StatusStatus.WORDT_VERWERKT
        self.__rapport: StoringRapport | None = None

    def maak_rapport(self) -> StoringRapport:
        # Maakt een rapport aan nadat de storing is afgehandeld
        self.__rapport = StoringRapport(
            id=uuid.uuid4(),
            storing_id=self.__id,
            kunstwerk_id=self.__kunstwerk.get_id(),
            beschrijving=self.__beschrijving,
        )
        return self.__rapport

    def set_status(self, status: StatusStatus) -> None:
        self.__status = status

    def get_id(self) -> uuid.UUID:
        return self.__id

    def get_beschrijving(self) -> str:
        return self.__beschrijving

    def get_status(self) -> StatusStatus:
        return self.__status

    def get_kunstwerk(self) -> Kunstwerk:
        return self.__kunstwerk

    def get_rapport(self) -> StoringRapport | None:
        return self.__rapport
