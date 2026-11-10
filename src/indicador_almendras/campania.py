from datetime import date

from indicador_almendras.precio import Precio
from indicador_almendras.publicacion import Publicacion
from indicador_almendras.variedad import Variedad


class Campania:
    """
    Entidad y raíz del agregado: la campaña de quien vende.

    Va desde que entra su cosecha (inicio) hasta su plazo, el inicio de
    la campaña siguiente. Ambas fechas las da quien vende, porque
    dependen de cuándo entra su cosecha (#8). Es de una sola variedad,
    la que usa la cooperativa para pagarle.

    Reúne la última publicación hasta su inicio, que es la vigente cuando
    empieza, y todas las que salen antes de su plazo (#8, #9).

    El plazo tiene que ser posterior al inicio (PlazoNoPosteriorAlInicio;
    se comprueba en el M1).
    """

    def __init__(self, variedad: Variedad, inicio: date, plazo: date) -> None:
        self._variedad = variedad
        self._inicio = inicio
        self._plazo = plazo
        self._publicaciones: list[Publicacion] = []

    def registrar_publicacion(self, publicacion: Publicacion) -> None:
        """
        Añade a la campaña una publicación de la Lonja.

        Se rechaza si es de otra variedad (VariedadDistintaDeLaCampania)
        o si no forma parte de la campaña: posterior al plazo o anterior
        a la vigente al inicio (PublicacionFueraDeCampania).
        """
        raise NotImplementedError

    def precio_vigente(self, fecha: date) -> Precio:
        """
        Precio al que se puede vender en una fecha de la campaña.

        Es el de la última publicación hasta esa fecha, sea el día que
        sea (#9). Si es «–» o aún no hay ninguna, no se puede vender
        (SinPrecioVigente, #7). La fecha tiene que estar dentro de la
        campaña (FechaFueraDeCampania).
        """
        raise NotImplementedError
