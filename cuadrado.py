from math import sqrt


class Cuadrado(object):

    def __init__(self, longitud_lado, unidad_medida):
        self.longitud_lado = longitud_lado
        self.unidad_medida = unidad_medida

    def calcular_perimetro(self):
        return 4 * self.longitud_lado

    def calcular_area(self):
        return self.longitud_lado ** 2

    def calcular_diagonal(self):
        return sqrt(2 * self.longitud_lado ** 2)

    def __str__(self):
        return f"Lado: {self.longitud_lado} {self.unidad_medida}\nPerimetro: {self.calcular_perimetro()} {self.unidad_medida}\n" \
               f"Area: {self.calcular_area()} {self.unidad_medida}**2\nDiagonal: {round(self.calcular_diagonal(), 2)} " \
               f"{self.unidad_medida}"


if __name__ == "__main__":
    un_cuadrado = Cuadrado(1, "m")
    print(un_cuadrado)
