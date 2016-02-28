#!/usr/bin/env python

"""Test File for command line arguments to rover.py

    Runs using py.test framework.

    python py.test

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2016 Susan Sim"
__license__ = "MIT License"

from rover import main




def test_CLI_noargs(capsys):
    """Tests calling main from the command line with no arguments.
    """
    # Create argument list
    args = ["rover.py"]
    # Call function
    main(args)
    (out, err) = capsys.readouterr();
    # Check output
    assert out == "Here!\n"


def test_CLI_help(capsys):
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


def test_CLI_error(capsys):
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
