# Situaciones inválidas del dominio de la HU001

# Se declaran en el M0; el código que las comprueba se escribe en el M1


class PlazoNoPosteriorAlInicio(ValueError):
    """El plazo de una campaña tiene que ser posterior a su inicio."""
