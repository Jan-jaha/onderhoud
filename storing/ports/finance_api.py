import requests

from storing.domain.factuur import Factuur


class FinanceApi:
    """Port — verwerkt facturen via de externe FinanceAPI."""

    def __init__(self, base_url: str, api_key: str):
        self.__base_url = base_url
        self.__api_key = api_key

    def sla_factuur_op(self, factuur: Factuur) -> bool:
        # Stuurt de factuur naar de FinanceAPI voor verwerking
        response = requests.post(
            f"{self.__base_url}/facturen",
            json=factuur.to_dict(),
            headers={"Authorization": f"Bearer {self.__api_key}"},
        )
        return response.status_code == 200
