import uuid
import requests


class BudgetApi:
    """Port — haalt het beschikbare budget op voor een kunstwerk via de BudgetAPI."""

    def __init__(self, base_url: str, api_key: str):
        self.__base_url = base_url
        self.__api_key = api_key

    def haal_budget_op(self, kunstwerk_id: uuid.UUID) -> float:
        # Haalt het resterende budget op voor het opgegeven kunstwerk
        response = requests.get(
            f"{self.__base_url}/budget/{kunstwerk_id}",
            headers={"Authorization": f"Bearer {self.__api_key}"},
        )
        response.raise_for_status()
        return response.json()["budget"]
