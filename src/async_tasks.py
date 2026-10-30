"""Модуль асинхронной обработки данных (Задание повышенной сложности 7)."""
import asyncio
from typing import Any
from src.models import Product
from src.repository import ProductRepository


async def fetch_product_stats(product_id: int, latency: float = 0.05) -> dict[str, Any]:
    """Имитирует асинхронный сетевой запрос за метриками товара."""
    await asyncio.sleep(latency)
    return {
        "product_id": product_id,
        "views_count": (product_id * 137) % 850 + 50,
        "in_stock": product_id % 2 == 1,
    }


async def batch_fetch_metrics(product_ids: list[int]) -> list[dict[str, Any]]:
    """Параллельно выполняет асинхронные запросы метрик через asyncio.gather."""
    tasks = [fetch_product_stats(pid) for pid in product_ids]
    return await asyncio.gather(*tasks)


async def async_batch_insert(repository: ProductRepository, items: list[Product]) -> int:
    """Асинхронная вставка пакета товаров с конкурентной обработкой."""
    async def _insert_one(prod: Product) -> None:
        await asyncio.sleep(0.01)
        repository.add(prod)

    await asyncio.gather(*[_insert_one(p) for p in items])
    return repository.count()
