import uuid
from datetime import date

from shared.domain.enums import OnderhoudStatus
from onderhoud.domain.onderhoud import Onderhoud
from onderhoud.domain.onderhoud_planning import OnderhoudPlanning
from onderhoud.ports.beheer_api import BeheerApi
from onderhoud.ports.keuring_api import KeuringApi


class OnderhoudService:
    """Domain Service — coördineert de aanmaak en afronding van onderhoud."""

    def __init__(self, beheer_api: BeheerApi, keuring_api: KeuringApi):
        self.__beheer_api = beheer_api
        self.__keuring_api = keuring_api

    def start_onderhoudplanning(self, planning: OnderhoudPlanning) -> Onderhoud:
        # Haalt het kunstwerk op en maakt een Onderhoud aggregate aan op basis van de planning
        kunstwerk = self.__beheer_api.haal_kunstwerk_op(str(planning.get_kunstwerk_id()))
        self.__keuring_api.vraag_keuring_aan(planning.get_kunstwerk_id())

        onderhoud = Onderhoud(
            id=uuid.uuid4(),
            strategie=None,
            kunstwerk=kunstwerk,
            startdatum=date.today(),
            einddatum=None,
            aannemer=kunstwerk.get_aannemer(),
            type=kunstwerk.get_type(),
        )
        onderhoud.set_status(OnderhoudStatus.WORDT_UITGEVOERD)
        return onderhoud

    def sla_uitgevonderhoud(self, onderhoud: Onderhoud, datum: date, beschrijving: str) -> None:
        # Markeert het onderhoud als uitgevoerd en maakt het rapport aan
        onderhoud.set_status(OnderhoudStatus.IS_UITGEVOERD)
        onderhoud.maak_rapport(beschrijving)
