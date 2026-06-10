import uuid
import requests


class ContractApi:
    """Port — haalt de verantwoordelijke aannemer op via de ContractAPI."""

    def __init__(self, base_url: str, api_key: str):
        self.__base_url = base_url
        self.__api_key = api_key

    def haal_aannemer_op(self, kunstwerk_id: uuid.UUID) -> str:
        # Vraagt op welke aannemer contractueel verantwoordelijk is voor dit kunstwerk
        response = requests.get(
            f"{self.__base_url}/contracten/{kunstwerk_id}/aannemer",
            headers={"Authorization": f"Bearer {self.__api_key}"},
        )
        response.raise_for_status()
        return response.json()["aannemer"]
