import requests

from onderhoud.domain.kunstwerk import Kunstwerk


class BeheerApi:
    """Port — haalt kunstwerkgegevens op uit de externe BeheerAPI."""

    def __init__(self, base_url: str, api_key: str):
        self.__base_url = base_url
        self.__api_key = api_key

    def haal_kunstwerk_op(self, kunstwerk_id: str) -> Kunstwerk:
        # Vraagt kunstwerkgegevens op via de BeheerAPI en zet ze om naar een Kunstwerk object
        response = requests.get(
            f"{self.__base_url}/kunstwerken/{kunstwerk_id}",
            headers={"Authorization": f"Bearer {self.__api_key}"},
        )
        response.raise_for_status()
        return Kunstwerk.verwerken(response.json())
