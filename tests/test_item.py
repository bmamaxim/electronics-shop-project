"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


def test_main():
    item1 = Item("Смартфон", 10000, 20)
    assert item1.price == 10000
    assert item1.calculate_total_price() == 200000
    assert item1.pay_rate == 1.0
    assert item1.name == "Смартфон"
    assert item1.quantity == 20
    assert isinstance(item1.all, list)
    item1.name = 'СуперСмартфон'
    assert item1.name == 'СуперСмарт'

def test_apply_discount():
    10000 * 0.85 == 8500.0

def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5

