import pytest
import datetime
from main import filter_product_data, get_last_month_changes

@pytest.fixture
def sample_data():
    """Фікстура з тестовими даними"""
    return [
        ("Молоко", "2026-03-15", "25.5"),
        ("Молоко", "2026-04-01", "27.0"),
        ("Хліб", "2026-04-05", "18.0"),
    ]

@pytest.mark.parametrize("product_name,expected_count", [
    ("Молоко", 2),
    ("Хліб", 1),
    ("Сир", 0),
])
def test_filter_product_data(sample_data, product_name, expected_count):
    """Перевірка фільтрації даних по товару"""
    result = filter_product_data(sample_data, product_name)
    assert len(result) == expected_count

def test_get_last_month_changes(sample_data):
    """Перевірка вибірки даних за останній місяць"""
    product_data = filter_product_data(sample_data, "Молоко")
    changes = get_last_month_changes(product_data)
    assert all(date >= datetime.datetime.today() - datetime.timedelta(days=30) for date, _ in changes)
