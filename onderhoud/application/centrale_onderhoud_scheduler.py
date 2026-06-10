from datetime import date

from onderhoud.infrastructure.planning_database import PlanningDatabase
from onderhoud.application.onderhoud_service import OnderhoudService


class CentraleOnderhoudScheduler:
    """Application Service — controleert dagelijks welke onderhouden gestart moeten worden."""

    def __init__(self, planning_database: PlanningDatabase, onderhoud_service: OnderhoudService):
        self.__planning = planning_database
        self.__service = onderhoud_service

    def start_service(self, datum: date) -> None:
        # Haalt alle planningen op die op de gegeven datum uitgevoerd moeten worden en start ze
        planningen = self.__planning.haal_datum_op(datum)
        for planning in planningen:
            if planning.is_het_tijdstip(datum):
                onderhoud = self.__service.start_onderhoudplanning(planning)
                planning.update_na_uitvoering(datum)
                self.__planning.update_planning(planning)
