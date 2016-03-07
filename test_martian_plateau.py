#!/usr/bin/env python

""" Test cases for py.test for martian_plateau.py """

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2016 Susan Sim"
__license__ = "MIT License"

from martian_plateau import MartianPlateau


def test_constructor():
    """Tests the constructor for Martian Plateau
    """

    mp = MartianPlateau([0, 0])
    assert mp.get_x() == 0
    assert mp.get_y() == 0

    mp = MartianPlateau([-1, 0])
    assert mp.get_x() == 0
    assert mp.get_y() == 0

    mp = MartianPlateau([0, -1])
    assert mp.get_x() == 0
    assert mp.get_y() == 0

    mp = MartianPlateau([1, 0])
    assert mp.get_x() == 1
    assert mp.get_y() == 0

    mp = MartianPlateau([0, 1])
    assert mp.get_x() == 0
    assert mp.get_y() == 1

    mp = MartianPlateau([1, 1])
    assert mp.get_x() == 1
    assert mp.get_y() == 1

    mp = MartianPlateau([2, 3])
    assert mp.get_x() == 2
    assert mp.get_y() == 3


def test_is_outside():
    """Tests calling inputting invalid coordinates to get_location()
    """

    mp = MartianPlateau([0, 0])
    assert mp.is_outside([0, 0]) is False
    assert mp.is_outside([1, 0]) is True
    assert mp.is_outside([0, 1]) is True
    assert mp.is_outside([2, 2]) is True

    mp = MartianPlateau([5, 5])
    assert mp.is_outside([0, 0]) is False
    assert mp.is_outside([1, 0]) is False
    assert mp.is_outside([0, 1]) is False
    assert mp.is_outside([5, 5]) is False
    assert mp.is_outside([5, 6]) is True
    assert mp.is_outside([6, 5]) is True