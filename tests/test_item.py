"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
from src.keyboard import Keyboard
from src.phone import Phone


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


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5

    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert str(phone1) == 'iPhone 14'
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"
    assert phone1.number_of_sim == 2

    item1 = Item("Смартфон", 10000, 20)
    assert item1 + phone1 == 25

    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert str(kb) == "Dark Project KD87A"
    assert str(kb.language) == "EN"
    kb.change_lang()
    assert str(kb.language) == "RU"
