"""Тестирование класса со свойствами @property (Средняя сложность 9)."""
import pytest
from src.models import Product


def test_product_properties_read_and_set():
    prod = Product(product_id=10, name="Клавиатура", price=5000.0, rating=4.5)
    assert prod.id == 10
    assert prod.name == "Клавиатура"
    assert prod.price == 5000.0
    assert prod.rating == 4.5

    prod.price = 4500.0
    prod.rating = 4.9
    assert prod.price == 4500.0
    assert prod.rating == 4.9


def test_product_price_validation():
    prod = Product(product_id=1, name="Мышь", price=1000.0)
    with pytest.raises(ValueError, match="не может быть отрицательной"):
        prod.price = -100.0
    with pytest.raises(TypeError, match="числовым значением"):
        prod.price = "бесплатно"


def test_product_rating_validation():
    prod = Product(product_id=1, name="Мышь", price=1000.0)
    with pytest.raises(ValueError, match="от 0.0 до 5.0"):
        prod.rating = 5.5
    with pytest.raises(ValueError, match="от 0.0 до 5.0"):
        prod.rating = -0.5


def test_product_immutable_id():
    prod = Product(product_id=1, name="Мышь", price=1000.0)
    with pytest.raises(AttributeError):
        prod.id = 99
