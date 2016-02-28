#!/usr/bin/env python

"""py.test cases for inputs to rover.py

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2016 Susan Sim"
__license__ = "MIT License"

from rover import main, Usage, get_plateau
import mock


# def test_cli_noargs(capsys):
#     """Tests calling main from the command line with no arguments.
#     """
#     # Create argument list
#     args = ["rover.py"]
#     # Call function
#     main(args)
#     (out, err) = capsys.readouterr();
#     # Check output
#     assert out == "Plateau:"


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

def test_get_plateau_error():
    top_corners=["a", "a b", "a, b", "1", "1,2", "1, 2", "-1 -3"]
    # Call function:
    for corner in top_corners:
        with mock.patch("__builtin__.raw_input", return_value=corner):
            try:
                get_plateau()
            except Usage:
                assert True
            else:
                assert False


def test_get_plateau_correct():
    top_corners=["1 1", "2 5", "9223372036854775807 9223372036854775807"]
    # Call function:
    for corner in top_corners:
        with mock.patch("__builtin__.raw_input", return_value=corner):
            try:
                xy = get_plateau()
            except Usage as u:
                print u.message
                assert False

