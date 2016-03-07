#!/usr/bin/env python

""" Test suite using py.test for rover.py"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2016 Susan Sim"
__license__ = "MIT License"

from rover import Rover
from martian_plateau import MartianPlateau
from martian_exceptions import ImproperLanding, ImproperInstruction


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

    for landing, landing_l in zip(landing_strings, landing_list):
        try:
            rvr = Rover(landing, plateau)
            assert rvr.get_x() == landing_l[0]
            assert rvr.get_y() == landing_l[1]
            assert rvr.get_facing() == landing_l[2]
        except ImproperLanding:
            print landing
            assert False


def test_get_instruction_error():
    """Tests calling inputting invalid coordinates to get_location()
    """
    instr_strings =["l", "m", "r", "La", "L M", "M R", " LM ", "aM", "q    R"]
    plateau = MartianPlateau("1000 1000")
    rvr = Rover("100 100 N", plateau)

    for instr in instr_strings:
        try:
            rvr = Rover("100 100 N", plateau)
            rvr.instruct(instr)
        except ImproperInstruction:
            assert True
        else:
            print instr
            assert False


def test_rover_left_turn():
    plateau = MartianPlateau("5 5")
    rvr = Rover("1 1 N", plateau)

    assert rvr.get_facing() == "N"
    rvr.instruct("L")
    assert rvr.get_facing() == "W"
    rvr.instruct("L")
    assert rvr.get_facing() == "S"
    rvr.instruct("L")
    assert rvr.get_facing() == "E"
    rvr.instruct("L")
    assert rvr.get_facing() == "N"


def test_rover_right_turn():
    plateau = MartianPlateau("5 5")
    rvr = Rover("1 1 N", plateau)

    assert rvr.get_facing() == "N"
    rvr.instruct("R")
    assert rvr.get_facing() == "E"
    rvr.instruct("R")
    assert rvr.get_facing() == "S"
    rvr.instruct("R")
    assert rvr.get_facing() == "W"
    rvr.instruct("R")
    assert rvr.get_facing() == "N"


def test_rover_move_single():
    plateau = MartianPlateau("10 10")
    start_locs = ["5 5 N", "5 5 E", "5 5 S", "5 5 W"]
    new_locs = [[5, 6, "N"], [6, 5, "E"], [5, 4, "S"], [4, 5, "W"]]

    for s, n in zip(start_locs, new_locs):
        rvr = Rover(s, plateau)
        output = rvr.instruct("M")
        print output
        assert rvr.get_x() == n[0]
        assert rvr.get_y() == n[1]
        assert rvr.get_facing() == n[2]


def test_rover_move_edge():
    plateau = MartianPlateau("4 4")
    start_locs = ["2 2 N", "2 2 E", "2 2 S", "2 2 W"]
    instructions = "MMMM"
    new_locs = [[2, 4, "N"], [4, 2, "E"], [2, 0, "S"], [0, 2, "W"]]

    for s, n in zip(start_locs, new_locs):
        rvr = Rover(s, plateau)
        rvr.instruct(instructions)

        assert rvr.get_x() == n[0]
        assert rvr.get_y() == n[1]
        assert rvr.get_facing() == n[2]


def test_rover_move_sequence():
    plateau = MartianPlateau("6 6")
    start_locs = ["0 0 N", "3 3 W", ]
    instructions = ["MRMLMRMLMRMLMRMLMRMLMRML","MMMLMMM"]
    new_locs = [[6, 6, "N"], [0, 0, "S"]]

    for s, i, n in zip(start_locs,instructions, new_locs):
        rvr = Rover(s, plateau)
        rvr.instruct(i)

        assert rvr.get_x() == n[0]
        assert rvr.get_y() == n[1]
        assert rvr.get_facing() == n[2]

def test_rover_move_example():
    plateau = MartianPlateau("5 5")
    start_locs = ["1 2 N", "3 3 E", ]
    instructions = ["LMLMLMLMM","MMRMMRMRRM"]
    new_locs = [[1, 3, "N"], [5, 1, "E"]]

    for s, i, n in zip(start_locs,instructions, new_locs):
        rvr = Rover(s, plateau)
        output =rvr.instruct(i)

        assert rvr.get_x() == n[0]
        assert rvr.get_y() == n[1]
        assert rvr.get_facing() == n[2]