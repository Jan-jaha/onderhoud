import uuid
import requests


class KeuringApi:
    """Port — vraagt een keuring aan via de externe KeuringAPI."""

    def __init__(self, base_url: str, api_key: str):
        self.__base_url = base_url
        self.__api_key = api_key

    def vraag_keuring_aan(self, kunstwerk_id: uuid.UUID) -> bool:
        # Dient een keuringsverzoek in voor het opgegeven kunstwerk
        response = requests.post(
            f"{self.__base_url}/keuringen",
            json={"kunstwerk_id": str(kunstwerk_id)},
            headers={"Authorization": f"Bearer {self.__api_key}"},
        )
        return response.status_code == 200
