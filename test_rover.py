#!/usr/bin/env python

""" Test suite using py.test for rover.py"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2016 Susan Sim"
__license__ = "MIT License"

from rover import Rover
from martian_plateau import MartianPlateau
from martian_exceptions import ImproperLanding


def test_rover_constructor_error():
    """Tests calling inputting invalid coordinates to get_location()
    """
    landing_strings = ["a", "a a", "a a a",
                       "1", "1 1", "1 1 1",
                       "2 2 n", "2 2 N "]
    plateau = MartianPlateau("5 5")
    for landing in landing_strings:
        try:
            rvr = Rover(landing, plateau)
        except ImproperLanding:
            assert True
        else:
            print landing
            assert False


def test_rover_constructor_correct():
    """Tests calling inputting invalid coordinates to get_location()
    """
    landing_strings = ["02 2 N", "0 0 S", "33 44 E", "777 888 W"]
    landing_list = [[2, 2, "N"], [0, 0, "S"], [33, 44, "E"], [777, 888, "W"]]
    plateau = MartianPlateau("1000 1000")
    # Call function:
    for landing, landing_l in zip(landing_strings, landing_list):
        try:
            rvr = Rover(landing, plateau)
            assert rvr.get_x() == landing_l[0]
            assert rvr.get_y() == landing_l[1]
            assert rvr.get_facing() == landing_l[2]
        except ImproperLanding:
            print landing
            assert False
