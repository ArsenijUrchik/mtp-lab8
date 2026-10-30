"""Тестирование шаблона проектирования Repository (Повышенная сложность 3)."""
import pytest
from src.models import Product
from src.repository import ProductRepository


def test_repository_lifecycle():
    repo = ProductRepository()
    p1 = Product(1, "Товар 1", 100.0)
    p2 = Product(2, "Товар 2", 200.0)

    repo.add(p1)
    repo.add(p2)
    assert repo.count() == 2
    assert repo.get(1) == p1
    assert repo.get(999) is None

    p1_updated = Product(1, "Товар 1 Обновлен", 150.0)
    repo.update(p1_updated)
    assert repo.get(1).name == "Товар 1 Обновлен"
    assert repo.get(1).price == 150.0

    repo.delete(2)
    assert repo.count() == 1
    assert repo.get(2) is None


def test_repository_exceptions():
    repo = ProductRepository()
    prod = Product(1, "Товар", 100.0)
    repo.add(prod)

    with pytest.raises(ValueError, match="уже зарегистрирован"):
        repo.add(prod)

    with pytest.raises(KeyError, match="не найден"):
        repo.update(Product(404, "Не существует", 10.0))

    with pytest.raises(KeyError, match="не найден"):
        repo.delete(404)
