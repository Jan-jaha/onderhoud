from shared.domain.enums import StatusStatus
from storing.domain.storing import Storing
from storing.domain.factuur import Factuur
from storing.ports.beheer_api import BeheerApi
from storing.ports.finance_api import FinanceApi


class StoringService:
    """Domain Service — coördineert de afhandeling van een storing en het versturen van facturen."""

    def __init__(self, beheer_api: BeheerApi, finance_api: FinanceApi):
        self.__beheer_api = beheer_api
        self.__finance_api = finance_api

    def markeer_uitgeverd(self, storing: Storing) -> None:
        # Markeert de storing als uitgevoerd, maakt rapport aan en stuurt het naar BeheerAPI
        storing.set_status(StatusStatus.IS_UITGEVOERD)
        rapport = storing.maak_rapport()
        self.__beheer_api.verstuur_rapport(rapport)

    def verstuur_factuur(self, factuur: Factuur) -> bool:
        # Stuurt de factuur voor de afgehandelde storing naar de FinanceAPI
        return self.__finance_api.sla_factuur_op(factuur)
