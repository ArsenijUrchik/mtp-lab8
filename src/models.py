"""Модуль моделей данных (Задание средней сложности 9)."""


class Product:
    """Модель товара с инкапсулированными свойствами через декоратор @property."""

    def __init__(self, product_id: int, name: str, price: float, rating: float = 5.0) -> None:
        if not isinstance(product_id, int) or product_id <= 0:
            raise ValueError("ID товара должен быть положительным целым числом.")
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Название товара не может быть пустой строкой.")

        self._id: int = product_id
        self._name: str = name.strip()
        self.price = price
        self.rating = rating

    @property
    def id(self) -> int:
        """Уникальный идентификатор товара (только для чтения)."""
        return self._id

    @property
    def name(self) -> str:
        """Название товара."""
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Название товара не может быть пустым.")
        self._name = value.strip()

    @property
    def price(self) -> float:
        """Стоимость товара."""
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError("Стоимость должна быть числовым значением.")
        if value < 0:
            raise ValueError("Стоимость товара не может быть отрицательной.")
        self._price = float(value)

    @property
    def rating(self) -> float:
        """Рейтинг товара от 0.0 до 5.0."""
        return self._rating

    @rating.setter
    def rating(self, value: float) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError("Рейтинг должен быть числом.")
        if not (0.0 <= value <= 5.0):
            raise ValueError("Рейтинг должен находиться в диапазоне от 0.0 до 5.0.")
        self._rating = float(value)

    def __repr__(self) -> str:
        return f"Product(id={self.id}, name='{self.name}', price={self.price:.2f}, rating={self.rating:.1f})"
