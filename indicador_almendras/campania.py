from datetime import date
from decimal import Decimal

from indicador_almendras.variedad import Variedad


class Campania:
    """
    Entidad y raíz del agregado: la campaña de quien vende.

    Va desde que entra su cosecha (inicio) hasta su plazo, el inicio de
    la campaña siguiente. Ambas fechas las da quien vende, porque
    dependen de cuándo entra su cosecha (#8). Es de una sola variedad,
    la que usa la cooperativa para pagarle.

    El plazo tiene que ser posterior al inicio (PlazoNoPosteriorAlInicio;
    se comprueba en el M1).
    """

    def __init__(self, variedad: Variedad, inicio: date, plazo: date) -> None:
        self._variedad = variedad
        self._inicio = inicio
        self._plazo = plazo
        self._publicaciones: dict[date, Decimal | None] = {}
