import uuid

from storing.ports.contract_api import ContractApi


class Aannemer:
    """Entity — vertegenwoordigt de aannemer die een storing oplost."""

    def __init__(self, aannemer: str, contract_api: ContractApi):
        self.__aannemer = aannemer
        self.__contract_api = contract_api

    def haal_aannemer_op_voor_kunstwerk(self, kunstwerk_id: uuid.UUID) -> str:
        # Vraagt via de ContractAPI op welke aannemer verantwoordelijk is voor dit kunstwerk
        return self.__contract_api.haal_aannemer_op(kunstwerk_id)

    def get_naam(self) -> str:
        return self.__aannemer
