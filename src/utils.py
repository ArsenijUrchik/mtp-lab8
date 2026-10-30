"""Модуль вспомогательных функций (Задание средней сложности 3)."""


def calculate_discount(price: float, discount_percent: float) -> float:
    """Вычисляет итоговую стоимость со скидкой с валидацией входных параметров."""
    if not isinstance(price, (int, float)):
        raise TypeError("Цена должна быть числом.")
    if not isinstance(discount_percent, (int, float)):
        raise TypeError("Скидка должна быть числом.")
    if price < 0:
        raise ValueError("Цена не может быть отрицательной.")
    if not (0.0 <= discount_percent <= 100.0):
        raise ValueError("Скидка должна быть в диапазоне от 0 до 100%.")

    return round(price * (1.0 - discount_percent / 100.0), 2)
