from clases.areas import Areas
def main():
    areas = Areas()
    print("Área de un triángulo con base 5 y altura 10:", areas.area_triangulo(5, 10))
    print("Área de un rectángulo con base 5 y altura 10:", areas.area_rectangulo(5, 10))
    print("Área de un círculo con radio 7:", areas.area_circulo(7))
if __name__ == "__main__":
    main()  