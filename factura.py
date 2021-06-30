class Factura(object):

    def __init__(self, codigo_producto, descripcion_producto, cantidad, precio_unitario):

        if cantidad < 0:
            raise ValueError("La cantidad debe ser un entero positivo")

        if precio_unitario < 0:
            raise ValueError("El precio unitario debe ser un decimal positivo")

        self.codigo_producto = codigo_producto
        self.descripcion_producto = descripcion_producto
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario

    def calcular_total_factura(self):
        return self.precio_unitario * self.cantidad

    def __str__(self):
        decimales = 2
        return f"Codigo: {self.codigo_producto}\nDescripcion: {self.descripcion_producto}\nCantidad: {self.cantidad}\n" \
               f"Precio Unitario: {round(self.precio_unitario, decimales)}\n" \
               f"Total Factura: {round(self.calcular_total_factura(), decimales)}"


if __name__ == "__main__":
    una_factura = Factura("1", "Laptop", 10, 3000.987)
    print(una_factura.codigo_producto)  # En consola: 1
    print(una_factura.descripcion_producto)  # En consola: Laptop
    print(una_factura.cantidad)  # En consola: 10
    print(una_factura.precio_unitario)  # En consola: 3000.987
    print(una_factura.calcular_total_factura())  # En consola: 30009.870000000003

    # una_factura = Factura("1", "Laptop", -2, 3000.987)

    # una_factura = Factura("1", "Laptop", 2, -3000.987)
