"""Модуль реализации шаблона Repository (Задание повышенной сложности 3)."""
from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar
from src.models import Product

T = TypeVar("T")


class AbstractRepository(ABC, Generic[T]):
    """Абстрактный интерфейс репозитория для управления коллекцией сущностей."""

    @abstractmethod
    def add(self, entity: T) -> None:
        pass

    @abstractmethod
    def get(self, entity_id: int) -> Optional[T]:
        pass

    @abstractmethod
    def list_all(self) -> list[T]:
        pass

    @abstractmethod
    def update(self, entity: T) -> None:
        pass

    @abstractmethod
    def delete(self, entity_id: int) -> None:
        pass


class ProductRepository(AbstractRepository[Product]):
    """Реализация in-memory репозитория для сущностей Product."""

    def __init__(self) -> None:
        self._storage: dict[int, Product] = {}

    def add(self, entity: Product) -> None:
        if not isinstance(entity, Product):
            raise TypeError("Объект должен быть экземпляром Product.")
        if entity.id in self._storage:
            raise ValueError(f"Товар с ID={entity.id} уже зарегистрирован.")
        self._storage[entity.id] = entity

    def get(self, entity_id: int) -> Optional[Product]:
        return self._storage.get(entity_id)

    def list_all(self) -> list[Product]:
        return list(self._storage.values())

    def update(self, entity: Product) -> None:
        if not isinstance(entity, Product):
            raise TypeError("Обновляемый объект должен быть экземпляром Product.")
        if entity.id not in self._storage:
            raise KeyError(f"Товар с ID={entity.id} не найден для обновления.")
        self._storage[entity.id] = entity

    def delete(self, entity_id: int) -> None:
        if entity_id not in self._storage:
            raise KeyError(f"Товар с ID={entity_id} не найден для удаления.")
        del self._storage[entity_id]

    def count(self) -> int:
        return len(self._storage)
