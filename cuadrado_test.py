from unittest import TestCase

from cuadrado import Cuadrado


class CuadradoTest(TestCase):

    def test_cuadrado(self):
        un_cuadrado = Cuadrado(4, "cm")

        self.assertEquals(un_cuadrado.longitud_lado, 4)
        self.assertEquals(un_cuadrado.calcular_perimetro(), 16)
        self.assertEquals(un_cuadrado.calcular_area(), 16)
        self.assertAlmostEqual(un_cuadrado.calcular_diagonal(), 5.656854249, places=3)

        self.assertEquals(str(un_cuadrado), "Lado: 4 cm\nPerimetro: 16 cm\nArea: 16 cm**2\nDiagonal: 5.66 cm")
