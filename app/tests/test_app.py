
import pytest
from decimal import Decimal

from app import validar_producto


def test_producto_valido():
    datos = {
        "nombre": "Teclado",
        "descripcion": "Teclado inalámbrico",
        "cantidad": "10",
        "precio": "50000"
    }

    resultado = validar_producto(datos)

    assert resultado == (
        "Teclado",
        "Teclado inalámbrico",
        10,
        Decimal("50000")
    )


def test_nombre_vacio():
    datos = {
        "nombre": "",
        "descripcion": "",
        "cantidad": "10",
        "precio": "50000"
    }

    with pytest.raises(ValueError):
        validar_producto(datos)


def test_cantidad_negativa():
    datos = {
        "nombre": "Teclado",
        "descripcion": "",
        "cantidad": "-1",
        "precio": "50000"
    }

    with pytest.raises(ValueError):
        validar_producto(datos)


def test_precio_negativo():
    datos = {
        "nombre": "Teclado",
        "descripcion": "",
        "cantidad": "10",
        "precio": "-500"
    }

    with pytest.raises(ValueError):
        validar_producto(datos)


def test_precio_con_mas_de_dos_decimales():
    datos = {
        "nombre": "Teclado",
        "descripcion": "",
        "cantidad": "10",
        "precio": "500.123"
    }

    with pytest.raises(ValueError):
        validar_producto(datos)
