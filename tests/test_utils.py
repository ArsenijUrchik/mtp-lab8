"""Тестирование функции расчета цены (Средняя сложность 3)."""
import pytest
from src.utils import calculate_discount


def test_calculate_discount_success():
    assert calculate_discount(100.0, 10.0) == 90.0
    assert calculate_discount(1000.0, 25.5) == 745.0
    assert calculate_discount(50.0, 0.0) == 50.0
    assert calculate_discount(200.0, 100.0) == 0.0


def test_calculate_discount_boundary_exceptions():
    with pytest.raises(ValueError, match="не может быть отрицательной"):
        calculate_discount(-10.0, 15.0)

    with pytest.raises(ValueError, match="в диапазоне от 0 до 100%"):
        calculate_discount(100.0, -1.0)

    with pytest.raises(ValueError, match="в диапазоне от 0 до 100%"):
        calculate_discount(100.0, 101.0)


def test_calculate_discount_type_errors():
    with pytest.raises(TypeError, match="должна быть числом"):
        calculate_discount("100", 10.0)

    with pytest.raises(TypeError, match="должна быть числом"):
        calculate_discount(100.0, "10")
