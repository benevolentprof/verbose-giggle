#!/usr/bin/env python

"""Mars Rover

Command-line program to place and move a rover on a Martian Plateau

Configuration Input: The first line of input is the upper-right
coordinates of the plateau, the lower-left coordinates are assumed to
be 0,0. Per Rover. Test Input:8 4

Input 1: Landing co-ordinates for the Rover The position is made up of
two integers and a letter separated by spaces, corresponding to the
x and y co-ordinates and the rover's orientation. Test Input:1 2 N

Input 2: Navigation instructions i.e a string containing ('L', 'R',
'M'). Test Input:LMLMLMLMM

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2016 Susan Sim"
__license__ = "MIT License"

import sys
import textwrap
from martian_plateau import MartianPlateau
from rover import Rover

def main(argv=None):

    if argv is None:
        argv = sys.argv
    # parse command line options

    if len(argv) > 1:
        if argv[1] == "-h" or argv[1] == "--help":
            print (textwrap.dedent(__doc__))
        else:
            print "Invalid syntax: " + "".join((" "+s) for s in argv)
    else:
        try:
            plateau = MartianPlateau(raw_input("Plateau:"))
            rover = Rover(raw_input("Rover1 Landing:"), plateau)
            output = rover.instruct(raw_input("Rover 1 Instructions:"))

            print output
        except Exception as e:
            print e.message
            raise e


if __name__ == "__main__":
    main()


