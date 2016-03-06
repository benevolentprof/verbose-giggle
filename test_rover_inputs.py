#!/usr/bin/env python

"""py.test cases for inputs to rover.py

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2016 Susan Sim"
__license__ = "MIT License"

from rover import main, Usage, ImproperLanding, get_top_right_corner, get_landing, get_instruction
import mock

def test_cli_help(capsys):
    """ Tests calling main with -h or --help for instructions
    """
    options = ["-h", "--help"]
    for opt in options:
        # Create argument list
        args = ["rover.py", opt]
        # Call function
        main(args)
        (out, err) = capsys.readouterr();
        # Check output
        assert out.startswith("Mars Rover")


def test_cli_error(capsys):
    """Tests calling main with invalid arguments
    """
    options = ["k", "--l", "-1"]
    for opt in options:
        # Create argument list
        args = ["rover.py", opt]
        # Call function
        main(args)
        (out, err) = capsys.readouterr();
        # Check output
        assert out.startswith("Invalid syntax")


def test_cli_plateau(capsys):
    """Tests calling main from the command line with no arguments, and plateau coordinates.
    """
    # Create argument list
    args = ["rover.py"]

    coordinates=["a", "a b", "a, b", "1", "1,2", "1, 2"]
    # Call function:
    for plateau in coordinates:
        with mock.patch("__builtin__.raw_input", return_value=plateau):
            try:
                main(args)
            except Usage:
                assert True
            else:
                assert False


def test_get_top_right_corner_error():
    """Tests calling inputting invalid coordinates to get_location()
    """
    top_corners=["a", "a b", "a, b", "1", "1,2", "1, 2", "-1 -3"]
    # Call function:
    for corner in top_corners:
        with mock.patch("__builtin__.raw_input", return_value=corner):
            try:
                get_top_right_corner()
            except Usage:
                assert True
            else:
                assert False


def test_get_top_right_corner_correct():
    """Tests calling inputting valid coordinates to get_location()
    """
    top_corners=["1 1", "2 5", "9223372036854775807 9223372036854775807"]
    xy_list = [[1, 1], [2, 5], [9223372036854775807, 9223372036854775807]]
    # Call function:
    for corner, xy in zip(top_corners, xy_list):
        with mock.patch("__builtin__.raw_input", return_value=corner):
            try:
                input_loc = get_top_right_corner()
                assert input_loc == xy
            except Usage as u:
                print u.message
                assert False


def test_get_landing_error():
    """Tests calling inputting invalid coordinates to get_location()
    """
    landing_strings = ["a", "a a", "a a a",
                       "1", "1 1", "1 1 1",
                       "2 2 n", "2 2 N "]
    # Call function:
    for landing in landing_strings:
        with mock.patch("__builtin__.raw_input", return_value=landing):
            try:
                input_list = get_landing("1")
            except ImproperLanding:
                assert True
            else:
                print input_list
                assert False

def test_get_landing_correct():
    """Tests calling inputting invalid coordinates to get_location()
    """
    landing_strings = ["02 2 N", "0 0 S", "33 44 E", "777 888 W"]
    landing_list = [[2, 2, "N"], [0, 0, "S"], [33, 44, "E"], [777, 888, "W"]]
    # Call function:
    for landing, landing_l in zip(landing_strings, landing_list):
        with mock.patch("__builtin__.raw_input", return_value=landing):
            try:
                input_list = get_landing("1")
                assert input_list == landing_l
            except ImproperLanding:
                print landing_list
                assert False



def test_get_instruction_error():
    """Tests calling inputting invalid coordinates to get_location()
    """
    instr_strings =["l", "m", "r", "La", "L M", "M R", " LM ", "aM", "q    R"]
    # Call function:
    for instr in instr_strings:
        with mock.patch("__builtin__.raw_input", return_value=instr):
            try:
                instr_list = get_instruction("Instruction:")
            except Usage:
                assert True
            else:
                print instr_list
                assert False


def test_get_instruction_correct():
    """Tests calling inputting invalid coordinates to get_location()
    """
    instr_strings =["L", "M", "R",
                    "LM", "LR", "MR", "ML", "RL", "RM",
                    "LMR", "LRM", "MRL", "MLR", "RLM", "RML"]
    instr_lists =[
        ["L"], ["M"], ["R"],
        ["L", "M"], ["L", "R"], ["M", "R"], ["M", "L"], ["R", "L"], ["R", "M"],
        ["L", "M", "R"], ["L", "R", "M"], ["M", "R", "L"], ["M", "L", "R"], ["R", "L", "M"], ["R", "M", "L"]
    ]
    # Call function:
    for instr, instr_l in zip(instr_strings, instr_lists):
        with mock.patch("__builtin__.raw_input", return_value=instr):
            try:
                input_list = get_instruction("Instruction:")
                assert input_list == instr_l
            except Usage as u:
                print u.message
                assert False
