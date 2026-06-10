import uuid

from storing.domain.verbund import Verbund


class Factuur:
    """Entity — financiële afrekening van een storing, inclusief uren en verbund."""

    def __init__(
        self,
        id: uuid.UUID,
        kunstwerk_id: uuid.UUID,
        uur: float,
        verbund: Verbund,
    ):
        self.__id = id
        self.__kunstwerk_id = kunstwerk_id
        self.__uur = uur
        self.__verbund = verbund

    @classmethod
    def verwerken(cls, data: dict) -> "Factuur":
        # Zet een dict om naar een Factuur object inclusief Verbund
        return cls(
            id=uuid.UUID(data["id"]),
            kunstwerk_id=uuid.UUID(data["kunstwerk_id"]),
            uur=data["uur"],
            verbund=Verbund.verwerken(data["verbund"]),
        )

    def get_id(self) -> uuid.UUID:
        return self.__id

    def get_totaalbedrag(self) -> float:
        # Totaalbedrag = verbund kosten + uren (tarief wordt buiten domein bepaald)
        return self.__verbund.get_totaalprijs() + self.__uur

    def to_dict(self) -> dict:
        return {
            "id": str(self.__id),
            "kunstwerk_id": str(self.__kunstwerk_id),
            "uur": self.__uur,
            "verbund": self.__verbund.to_dict(),
        }
