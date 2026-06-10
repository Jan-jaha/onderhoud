import requests

from storing.domain.storing_rapport import StoringRapport


class BeheerApi:
    """Port — stuurt een storingsrapport naar de externe BeheerAPI."""

    def __init__(self, base_url: str, api_key: str):
        self.__base_url = base_url
        self.__api_key = api_key

    def verstuur_rapport(self, rapport: StoringRapport) -> bool:
        # Verstuurt het storingsrapport naar de BeheerAPI
        response = requests.post(
            f"{self.__base_url}/rapporten",
            json={
                "storing_id": str(rapport.get_storing_id()),
                "kunstwerk_id": str(rapport.get_kunstwerk_id()),
                "beschrijving": rapport.get_beschrijving(),
            },
            headers={"Authorization": f"Bearer {self.__api_key}"},
        )
        return response.status_code == 200
