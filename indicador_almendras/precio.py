from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class Precio:
    """
    Objeto valor: precio de la Lonja de Albacete en €/kg.

    Un precio publicado no cambia; si sale otro, es otro precio.
    Tiene que ser mayor que 0 (PrecioNoPositivo; se comprueba en el M1).
    """

    euros_por_kg: Decimal
