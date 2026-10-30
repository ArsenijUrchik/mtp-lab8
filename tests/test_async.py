"""Тестирование асинхронных операций asyncio (Повышенная сложность 7)."""
import asyncio
from src.models import Product
from src.repository import ProductRepository
from src.async_tasks import async_batch_insert, batch_fetch_metrics


def test_batch_fetch_metrics_async():
    p_ids = [1, 2, 3]
    results = asyncio.run(batch_fetch_metrics(p_ids))
    assert len(results) == 3
    for res, expected_id in zip(results, p_ids):
        assert res["product_id"] == expected_id
        assert "views_count" in res
        assert isinstance(res["in_stock"], bool)


def test_async_batch_insert_to_repository():
    repo = ProductRepository()
    items = [
        Product(101, "Клавиатура", 3000.0),
        Product(102, "Мышь", 1500.0),
    ]
    total = asyncio.run(async_batch_insert(repo, items))
    assert total == 2
    assert repo.get(101) is not None
    assert repo.get(102) is not None
