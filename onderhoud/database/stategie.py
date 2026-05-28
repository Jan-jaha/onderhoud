from config.database import Base, SessionLocal
from sqlalchemy import Column, String, Integer, JSON
import uuid

class Strategie(Base):
    __tablename__ = "onderhoudStategie"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    kunstwerk_id = Column(String(36), nullable=False)
    frequentie = Column(Integer, nullable=False)
    onderhoudeisen = Column(JSON)

    def toevoegen(self, kunstwerk_id: str, frequentie: int, onderhoudeisen: list):
        with SessionLocal() as session:
            session.add(self)
            session.commit()

    def get_all(self):
        with SessionLocal() as session:
            return session.query(Strategie).all()