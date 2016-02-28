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


class Usage(Exception):
    def __init(self, message):
        self.message = message


def get_instructions(prompt):
    """
    Prompts the user to enter instructions to the rover. Inputs must consist of a sequence of Ls, Rs, and Ms in
    any order.
    :return: a list strings, each consisting of one character that is an L, R, or M
    """

    output = []

    input_string = raw_input(prompt)
    input_list = input_string.split()

    if len(input_list) != 2:
        raise Usage("Coordinates must have an x and a y value")

    for number in input_list:
        if number.isdigit():
            output.append(int(number))
        else:
            raise Usage("Coordinates must be positive integers")

    return output

def get_location(prompt):
    """
    Prompts the user to enter coordinates. They must be positive integers
    separated by spaces.
    :return: a list two ints containing the x and y coordinates specifying the plateau
    """

    output = []

    input_string = raw_input(prompt)
    input_list = input_string.split()

    if len(input_list) != 2:
        raise Usage("Coordinates must have an x and a y value")

    for number in input_list:
        if number.isdigit():
            output.append(int(number))
        else:
            raise Usage("Coordinates must be positive integers")

    return output


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
        plateau = get_location("Plateau:")
        landing = get_location("Rover1 Landing:")
        instructions = get_instructions("Rover1 Instructions:")

if __name__ == "__main__":
    main()


