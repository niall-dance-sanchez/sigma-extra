from main import count_items, heaviest_load, instruction_set_heaviest_load
import pytest


def test_count_items1():

    assert count_items("^^^....v..^.v") == 2


def test_count_items2():

    assert count_items(".................^") == 1


def test_count_items3():

    assert count_items(".^.^.^.^.^") == 5


def test_count_items4():

    assert count_items("vvv...^") == 1


def test_count_items5():

    with pytest.raises(ValueError):
        count_items(".^.^.^.^.^.^")


def test_heaviest_load1():

    assert heaviest_load("^^") == 2


def test_heaviest_load2():

    assert heaviest_load("^v^") == 1


def test_heaviest_load3():

    assert heaviest_load("^^^^^vvvvv") == 5


def test_heaviest_load4():

    assert heaviest_load("vvvv^^") == 2


def test_instruction_set_heaviest_load1():

    assert instruction_set_heaviest_load(["^^", "^"]) == 0


def test_instruction_set_heaviest_load2():

    assert instruction_set_heaviest_load(["^v^", "^^", "^^^^^vvvvv"]) == 2


def test_instruction_set_heaviest_load3():

    assert instruction_set_heaviest_load(["^^^^^^", "^^^^", "vvvv^^"]) == 1
