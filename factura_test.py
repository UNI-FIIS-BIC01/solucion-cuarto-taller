from unittest import TestCase

from factura import Factura


class FacturaTest(TestCase):

    def test_factura_adecuada(self):
        una_factura: Factura = Factura("1", "Laptop", 10, 3000.987)

        self.assertEquals(una_factura.codigo_producto, "1")
        self.assertEquals(una_factura.descripcion_producto, "Laptop")
        self.assertEquals(una_factura.cantidad, 10)
        self.assertAlmostEqual(una_factura.precio_unitario, 3000.987, places=4)
        self.assertAlmostEqual(una_factura.calcular_total_factura(), 30009.87, places=4)

        self.assertEquals(str(una_factura), "Codigo: 1\nDescripcion: Laptop\nCantidad: 10\nPrecio Unitario: 3000.99"
                                            "\nTotal Factura: 30009.87")

    def test_cantidad_negativa(self):
        with self.assertRaises(Exception) as context:
            _ = Factura("1", "Laptop", -2, 3000.987)

        self.assertEquals(ValueError, type(context.exception))
        self.assertEquals("La cantidad debe ser un entero positivo", str(context.exception))

    def test_precio_negativo(self):
        with self.assertRaises(Exception) as context:
            _ = Factura("1", "Laptop", 2, -3000.987)

        self.assertEquals(ValueError, type(context.exception))
        self.assertEquals("El precio unitario debe ser un decimal positivo", str(context.exception))
