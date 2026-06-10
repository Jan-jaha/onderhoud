class Verbund:
    """Value Object — beschrijft een gebruikte verbund (materiaal/onderdeel) bij een storing."""

    def __init__(self, naam: str, aantal: int, prijs_per_eenheid: float):
        self.__naam = naam
        self.__aantal = aantal
        self.__prijs_per_eenheid = prijs_per_eenheid

    @classmethod
    def verwerken(cls, data: dict) -> "Verbund":
        # Zet een dict om naar een Verbund object
        return cls(
            naam=data["naam"],
            aantal=data["aantal"],
            prijs_per_eenheid=data["prijs_per_eenheid"],
        )

    def get_naam(self) -> str:
        return self.__naam

    def get_totaalprijs(self) -> float:
        # Berekent de totaalprijs (aantal × prijs per eenheid)
        return self.__aantal * self.__prijs_per_eenheid

    def to_dict(self) -> dict:
        return {
            "naam": self.__naam,
            "aantal": self.__aantal,
            "prijs_per_eenheid": self.__prijs_per_eenheid,
            "totaalprijs": self.get_totaalprijs(),
        }
