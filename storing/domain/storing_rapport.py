import uuid


class StoringRapport:
    """Entity — rapportage van een afgehandelde storing."""

    def __init__(
        self,
        id: uuid.UUID,
        storing_id: uuid.UUID,
        kunstwerk_id: uuid.UUID,
        beschrijving: str,
    ):
        self.__id = id
        self.__storing_id = storing_id
        self.__kunstwerk_id = kunstwerk_id
        self.__beschrijving = beschrijving

    def get_id(self) -> uuid.UUID:
        return self.__id

    def get_storing_id(self) -> uuid.UUID:
        return self.__storing_id

    def get_kunstwerk_id(self) -> uuid.UUID:
        return self.__kunstwerk_id

    def get_beschrijving(self) -> str:
        return self.__beschrijving
