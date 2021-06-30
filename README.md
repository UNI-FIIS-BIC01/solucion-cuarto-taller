# BIC01: Cuarto Taller

## Primera Pregunta

En el archivo `cuadrado.py`, complete la implementación de la clase `Cuadrado`, que representa a la correspondiente
figura geométrica. Esta clase debe tener los siguientes atributos:

* El campo `longitud_lado`, un número entero cuyo valor proviene del método `__init__`. Representa la longitud del lado
  del cuadrado.

* El campo `unidad_medida`, una cadena de caracteres cuyo valor proviene del método `__init__`. Representa la unidad de
  medida del campo `longitud_lado`.

* El método `calcular_perimetro` retorna un número entero, correspondiente al perímetro del cuadrado representado.

* El método `calcular_area` retorna un número entero, correspondiente al área del cuadrado representado.

* El método `calcular_diagonal`, retorna un número real, correspondiente a la longitud de la diagonal del cuadrado
  representado.

La clase `Cuadrado` puede usarse de la siguiente manera:

```python
un_cuadrado = Cuadrado(1, "m")
print(un_cuadrado.longitud_lado)  # En consola: 1
print(un_cuadrado.unidad_medida)  # En consola: m
print(un_cuadrado.calcular_perimetro())  # En consola: 4
print(un_cuadrado.calcular_area())  # En consola: 1
print(un_cuadrado.calcular_diagonal())  # En consola: 1.4142135623730951
```

Además, al utilizar `print` sobre instancias de `Cuadrado` debe mostrarse esta información. Por ejemplo, al
ejecutar `print(Cuadrado(1, "m"))` se debe mostrar en consola:

```commandline
Lado: 1 m
Perimetro: 4 m
Area: 1 m**2
Diagonal: 1.41 m
```

Nótese que los números reales se muestran redondeados a 2 decimales.

## Segunda Pregunta

En el archivo `factura.py`, complete la implementación de la clase `Factura`. Esta clase puede usarse en tiendas para
representar las facturas a emitir por la venta de un producto. Esta clase debe tener los siguientes atributos:

* El campo `codigo_producto`, una cadena de caracteres cuyo valor proviene del método `__init__`.

* El campo `descripcion_producto`, una cadena de caracteres cuyo valor proviene del método `__init__`.

* El campo `cantidad`, un número entero positivo cuyo valor proviene del método `__init__`. En caso este valor sea
  negativo, lanzar una excepción del tipo `ValueError` con el mensaje *La cantidad debe ser un entero positivo*.

* El campo `precio_unitario`, un número decimal positivo cuyo valor proviene del método `__init__`. En caso este valor
  sea negativo, lanzar una excepción del tipo `ValueError` con el mensaje *El precio unitario debe ser un decimal
  positivo*.

* El método `calcular_total_factura`, retorna un número decimal correspondiente al total a pagar por la factura.

La clase `Factura` puede usarse de la siguiente manera:

  ```python
  una_factura = Factura("1", "Laptop", 10, 3000.987)
print(una_factura.codigo_producto)  # En consola: 1
print(una_factura.descripcion_producto)  # En consola: Laptop
print(una_factura.cantidad)  # En consola: 10
print(una_factura.precio_unitario)  # En consola: 3000.987
print(una_factura.calcular_total_factura())  # En consola: 30009.870000000003
  ```

Además, al utilizar `print` sobre instancias de `Factura`, deben mostrarse los valores de todos los campos junto al
total a pagar. Por ejemplo, al ejecutar `print(Factura("1", "Laptop", 10, 3000.987))
` se debe mostrar en consola:

```commandline
Codigo: 1
Descripcion: Laptop
Cantidad: 10
Precio Unitario: 3000.99
Total Factura: 30009.87
```

Nótese que los números reales se muestran redondeados a 2 decimales. En caso los valores iniciales no sean válidos, como
en `Factura("1", "Laptop", -2, 3000.987)`, la instancia no debe generarse, mostrando en consola un mensaje de error
similar al siguiente:

```commandline
Traceback (most recent call last):
  File "/Users/cgc87/git-bic01/taller-cuarta-practica/factura.py", line 42, in <module>
    una_factura = Factura("1", "Laptop", -2, 3000.987)
  File "/Users/cgc87/git-bic01/taller-cuarta-practica/factura.py", line 6, in __init__
    raise ValueError("La cantidad debe ser un entero positivo")
ValueError: La cantidad debe ser un entero positivo
```