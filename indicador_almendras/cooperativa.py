from dataclasses import dataclass, field
from datetime import date
from decimal import Decimal

from indicador_almendras.campania import Campania
from indicador_almendras.variedad import Variedad


@dataclass
class Cooperativa:
    precios: dict[Variedad, dict[date, Decimal | None]] = field(default_factory=dict)
    campanias: set[Campania] = field(default_factory=set)
