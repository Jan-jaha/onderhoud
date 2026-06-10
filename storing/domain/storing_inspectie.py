import uuid

from shared.domain.enums import PrioriteitStatus


class StoringInspectie:
    """Entity — vastlegging van een geconstateerde storing bij inspectie."""

    def __init__(
        self,
        id: uuid.UUID,
        kunstwerk_id: uuid.UUID,
        prioriteit: PrioriteitStatus,
        beschrijving: str,
    ):
        self.__id = id
        self.__kunstwerk_id = kunstwerk_id
        self.__prioriteit = prioriteit
        self.__beschrijving = beschrijving

    @classmethod
    def verwerken(cls, data: dict) -> "StoringInspectie":
        # Zet een dict om naar een StoringInspectie object
        return cls(
            id=uuid.UUID(data["id"]),
            kunstwerk_id=uuid.UUID(data["kunstwerk_id"]),
            prioriteit=PrioriteitStatus(data["prioriteit"]),
            beschrijving=data["beschrijving"],
        )

    def get_id(self) -> uuid.UUID:
        return self.__id

    def get_kunstwerk_id(self) -> uuid.UUID:
        return self.__kunstwerk_id

    def get_prioriteit(self) -> PrioriteitStatus:
        return self.__prioriteit

    def get_beschrijving(self) -> str:
        return self.__beschrijving
