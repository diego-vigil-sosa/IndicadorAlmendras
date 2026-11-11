from dataclasses import dataclass, field
from datetime import date
from decimal import Decimal

from indicador_almendras.variedad import Variedad


@dataclass(eq=False)
class Campania:
    variedad: Variedad
    inicio: date
    plazo: date
    precios_por_fecha: dict[date, Decimal | None] = field(default_factory=dict)
