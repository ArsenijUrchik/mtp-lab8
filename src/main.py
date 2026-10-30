"""Главный модуль запуска приложения (интеграция всех заданий Лабораторной 8)."""
import asyncio
from src.utils import calculate_discount
from src.models import Product
from src.repository import ProductRepository
from src.async_tasks import async_batch_insert, batch_fetch_metrics


async def run_application() -> None:
    print("=== Лабораторная работа № 8 (Вариант 3) ===")
    print("Тема: Экосистемы Python, их использование\n")

    # 1. Функция с валидацией (Средняя 3)
    orig_price = 15000.0
    discount = 12.5
    final_price = calculate_discount(orig_price, discount)
    print(f"[Средняя 3] calculate_discount: {orig_price} руб. со скидкой {discount}% = {final_price:.2f} руб.")

    # 2. Структура проекта (Средняя 5)
    print("[Средняя 5] Исходный код изолирован в каталоге src/, тесты - в tests/.")

    # 3. Класс с property (Средняя 9)
    item = Product(product_id=1, name="Механическая клавиатура", price=7500.0, rating=4.8)
    print(f"[Средняя 9] Создан объект Product: {item}")
    item.price = 6990.0
    print(f"            Обновление цены через setter @price.setter: {item.price:.2f} руб.")

    # 4. Шаблон Repository (Повышенная 3)
    repo = ProductRepository()
    repo.add(item)
    repo.add(Product(product_id=2, name="Беспроводная мышь", price=3400.0, rating=4.7))
    repo.add(Product(product_id=3, name="Игровой монитор 27", price=27900.0, rating=4.9))
    print(f"[Повышенная 3] Инициализирован ProductRepository ({repo.count()} товаров):")
    for prod in repo.list_all():
        print(f"                - {prod}")

    # 5. Асинхронность asyncio (Повышенная 7)
    p_ids = [p.id for p in repo.list_all()]
    print("\n[Повышенная 7] Конкурентный сбор статистики через asyncio.gather...")
    metrics = await batch_fetch_metrics(p_ids)
    for m in metrics:
        print(f"                - Товар #{m['product_id']}: просмотров={m['views_count']}, на складе={m['in_stock']}")

    new_batch = [
        Product(product_id=4, name="USB-C Hub", price=4200.0, rating=4.5),
        Product(product_id=5, name="Коврик для мыши XXL", price=1600.0, rating=4.6),
    ]
    total_count = await async_batch_insert(repo, new_batch)
    print(f"                Пакетная асинхронная вставка завершена. Всего элементов: {total_count}")


def main() -> None:
    asyncio.run(run_application())


if __name__ == "__main__":
    main()
