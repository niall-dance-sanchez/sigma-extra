"""Tests for the presents puzzle solution."""

import pytest

from workshop import get_surface_area, extract_dimensions


# Aim for 3-4 tests per function initially, focussed on reasonable input


def test_get_surface_area_for_normal_input_1():

    assert get_surface_area([2, 3, 4]) == 52


def test_get_surface_area_for_normal_input_2():

    assert get_surface_area([1, 1, 10]) == 42


def test_get_surface_area_for_extreme_input_1():

    assert get_surface_area([100])


def test_get_surface_area_rejects_infinitesimal_present():

    with pytest.raises(ValueError):
        get_surface_area([0, 0, 0])
