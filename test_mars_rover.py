#!/usr/bin/env python

"""py.test cases for inputs to mars_rover.py

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2016 Susan Sim"
__license__ = "MIT License"

import mock

from mars_rover import main


def test_cli_help(capsys):
    """ Tests calling main with -h or --help for instructions
    """
    options = ["-h", "--help"]
    for opt in options:
        # Create argument list
        args = ["mars_rover.py", opt]
        # Call function
        main(args)
        (out, err) = capsys.readouterr()
        # Check output
        assert out.startswith("Mars Rover")


def test_cli_error(capsys):
    """Tests calling main with invalid arguments
    """
    options = ["k", "--l", "-1"]
    for opt in options:
        # Create argument list
        args = ["mars_rover.py", opt]
        # Call function
        main(args)
        (out, err) = capsys.readouterr()
        # Check output
        assert out.startswith("Invalid syntax")

