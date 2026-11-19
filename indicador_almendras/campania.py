from dataclasses import dataclass
from datetime import date

from indicador_almendras.variedad import Variedad


@dataclass(frozen=True)
class Campania:
    variedad: Variedad
    inicio: date
    plazo: date
