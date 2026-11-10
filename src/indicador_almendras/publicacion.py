from dataclasses import dataclass
from datetime import date

from indicador_almendras.precio import Precio
from indicador_almendras.variedad import Variedad


@dataclass(frozen=True)
class Publicacion:
    """
    Objeto valor: lo que saca la Lonja en una fecha para una variedad.

    Puede traer un precio o «–». Sin precio (precio es None), mientras
    está vigente no se puede vender y no cuenta para el precio más alto
    hasta el plazo (#7).
    """

    fecha: date
    variedad: Variedad
    precio: Precio | None
