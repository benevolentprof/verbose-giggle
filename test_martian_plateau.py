#!/usr/bin/env python

""" Test cases for py.test for martian_plateau.py """

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2016 Susan Sim"
__license__ = "MIT License"

from martian_plateau import MartianPlateau
from martian_exceptions import ImproperPlateau


def test_martian_plateau():
    """Tests MartianPlateau constructor with good inputs
    """
    top_corners=["1 1", "2 5", "9223372036854775807 9223372036854775807"]
    xy_list = [[1, 1], [2, 5], [9223372036854775807, 9223372036854775807]]
    # Call function:
    for corner, xy in zip(top_corners, xy_list):
        try:
            mp = MartianPlateau(corner)
            assert mp.get_x() == xy[0]
            assert mp.get_y() == xy[1]
        except ImproperPlateau as i:
            print i.message
            assert False


def test_get_top_right_corner_error():
    """Tests MartianPlateau constructor with bad inputs
    """
    top_corners=["a", "a b", "a, b", "1", "1,2", "1, 2", "-1 -3"]
    # Call function:
    for corner in top_corners:
        try:
           mp = MartianPlateau(corner)
        except ImproperPlateau:
            assert True
        else:
            assert False


def test_is_outside():
    """Tests calling inputting invalid coordinates to get_location()
    """

    mp = MartianPlateau("0 0")
    assert mp.is_outside([0, 0]) is False
    assert mp.is_outside([1, 0]) is True
    assert mp.is_outside([0, 1]) is True
    assert mp.is_outside([2, 2]) is True

    mp = MartianPlateau("5 5")
    assert mp.is_outside([0, 0]) is False
    assert mp.is_outside([1, 0]) is False
    assert mp.is_outside([0, 1]) is False
    assert mp.is_outside([5, 5]) is False
    assert mp.is_outside([5, 6]) is True
    assert mp.is_outside([6, 5]) is True