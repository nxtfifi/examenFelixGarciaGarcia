class Areas:
    def __init__(self):
        pass
    def area_triangulo(self, base, altura):
        """Calcula el área de un triángulo dado la base y la altura."""
        return (base * altura) / 2
    def area_rectangulo(self, base, altura):
        """Calcula el área de un rectángulo dado la base y la altura."""
        return base * altura
    def area_circulo(self, radio):
        """Calcula el área de un círculo dado el radio."""
        import math
        return math.pi * (radio ** 2)