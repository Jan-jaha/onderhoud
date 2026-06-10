from datetime import date
from typing import List
import requests

from shared.domain.enums import PrioriteitStatus


class AfspraakApi:
    """Port — plant een afspraak in via de externe AfspraakAPI."""

    def __init__(self, base_url: str, api_key: str):
        self.__base_url = base_url
        self.__api_key = api_key

    def afspraak_instellen(
        self,
        aannemer: str,
        locatie: List,
        datum: date,
        prioriteit: PrioriteitStatus,
    ) -> bool:
        # Stuurt een afspraakverzoek naar de API met aannemer, locatie, datum en prioriteit
        response = requests.post(
            f"{self.__base_url}/afspraken",
            json={
                "aannemer": aannemer,
                "locatie": locatie,
                "datum": datum.isoformat(),
                "prioriteit": prioriteit.value,
            },
            headers={"Authorization": f"Bearer {self.__api_key}"},
        )
        return response.status_code == 200
