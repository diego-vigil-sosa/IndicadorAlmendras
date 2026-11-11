from enum import Enum


class Variedad(Enum):
    """
    Objeto valor: variedad con la que la cooperativa paga la almendra.

    La Lauranne se paga como Comuna, así que no es una variedad del modelo.
    Crear una variedad que no esté aquí lanza ValueError (lo hace Enum).
    """

    COMUNA = "Comuna"
    GUARA = "Guara"
