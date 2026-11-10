# Situaciones inválidas del dominio de la HU001

# Se declaran en el M0; el código que las comprueba se escribe en el M1


class PrecioNoPositivo(ValueError):
    """Un precio de la Lonja tiene que ser mayor que 0 €/kg."""
