from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()  # Laad .env bestand

engine = create_engine(os.getenv("DB_URL"))  # Maak verbinding met de database
Base = declarative_base()  # Basisklasse voor alle ORM-modellen
SessionLocal = sessionmaker(bind=engine)  # Sessie-fabriek

def get_session():
    # Maakt een sessie aan, geeft het terug en sluit het daarna
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()