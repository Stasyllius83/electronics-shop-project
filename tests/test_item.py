"""Здесь надо написать тесты с использованием pytest для модуля item"""
import pytest

from src.item import Item


# Tests
@pytest.fixture
def test_item():
    return Item("Смартфон", 10000, 20)


def test_fix_calculate_total_price(test_item):
    assert test_item.calculate_total_price() == 200000


def test_fix_change_pay_rate(test_item):
    assert test_item.pay_rate == 0.8


def test_fix_is_none_apply_discount(test_item):
    assert test_item.apply_discount() is None


def test_fix_apply_discount(test_item):
    assert int(test_item.price * test_item.pay_rate) == 8000


def test_fix_pay_rate(test_item):
    assert test_item.pay_rate == 0.8


item1 = Item("Смартфон", 10000, 20)


def test_calculate_total_price():
    assert item1.calculate_total_price() == 200000


def test_is_none_apply_discount():
    assert item1.apply_discount() is None


def test_apply_discount():
    assert int(item1.price * item1.pay_rate) == 8000


Item.pay_rate = 0.8


def test_pay_rate():
    assert item1.pay_rate == 0.8


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5


def test_name():
    item = Item('Смартфон', 10000, 5)
    item.name = "Суперсмартфон"
    assert len(item.name) <= 10
    assert item.name == "Суперсмарт"


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('9.0') == 9
    assert Item.string_to_number('11.2') == 11


def test_rer():
    item1 = Item('Смартфон', 10000, 5)
    assert repr(item1) == "Item('Смартфон', 10000, 5)"


def test_str():
    assert str(item1) == 'Смартфон'