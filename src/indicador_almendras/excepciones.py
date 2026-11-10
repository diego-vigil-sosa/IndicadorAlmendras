# Situaciones inválidas del dominio de la HU001

# Se declaran en el M0; el código que las comprueba se escribe en el M1


class PrecioNoPositivo(ValueError):
    """Un precio de la Lonja tiene que ser mayor que 0 €/kg."""


class SinPrecioVigente(LookupError):
    """No se puede vender: la publicación vigente es «–» o aún no hay
    ninguna."""


class PlazoNoPosteriorAlInicio(ValueError):
    """El plazo de una campaña tiene que ser posterior a su inicio."""


class VariedadDistintaDeLaCampania(ValueError):
    """Una campaña solo reúne publicaciones de su variedad."""


class PublicacionFueraDeCampania(ValueError):
    """Al registrar: publicación posterior al plazo o anterior a la vigente
    al inicio."""


class FechaFueraDeCampania(ValueError):
    """Al preguntar: la fecha tiene que estar entre el inicio y el plazo."""
