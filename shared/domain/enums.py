from enum import Enum


class OnderhoudStatus(Enum):
    INGEPLAND = "INGEPLAND"
    WORDT_UITGEVOERD = "WORDT_UITGEVOERD"
    IS_UITGEVOERD = "IS_UITGEVOERD"


class StatusStatus(Enum):
    WORDT_VERWERKT = "WORDT_VERWERKT"
    WORDT_UITGEVOERD = "WORDT_UITGEVOERD"
    IS_UITGEVOERD = "IS_UITGEVOERD"


class PrioriteitStatus(Enum):
    LAAG = "LAAG"
    MIDDEL = "MIDDEL"
    HOOG = "HOOG"
    KRITIEK = "KRITIEK"
