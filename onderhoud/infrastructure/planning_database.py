import uuid
from datetime import date
from typing import List

from config.database import SessionLocal
from onderhoud.domain.onderhoud_planning import OnderhoudPlanning


class PlanningDatabase:
    """Repository — beheert de opslag en ophaling van OnderhoudPlanning objecten."""

    def sla_op(self, planning: OnderhoudPlanning) -> None:
        # Slaat een nieuwe planning op in de database
        with SessionLocal() as session:
            session.add(planning)
            session.commit()

    def update_planning(self, planning: OnderhoudPlanning) -> None:
        # Werkt een bestaande planning bij in de database
        with SessionLocal() as session:
            session.merge(planning)
            session.commit()

    def haal_op(self, id: uuid.UUID) -> OnderhoudPlanning:
        # Haalt één planning op via het ID
        with SessionLocal() as session:
            return session.query(OnderhoudPlanning).filter_by(id=str(id)).first()

    def haal_datum_op(self, datum: date) -> List[OnderhoudPlanning]:
        # Haalt alle planningen op die op of voor de gegeven datum uitgevoerd moeten worden
        with SessionLocal() as session:
            return session.query(OnderhoudPlanning).filter(
                OnderhoudPlanning.volgende_uitvoering <= datum
            ).all()
