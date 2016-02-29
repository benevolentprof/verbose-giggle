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
import re


class Usage(Exception):
    def __init(self, message):
        self.message = message


def get_instruction(prompt):
    """
    Prompts the user to enter instructions to the rover. Inputs must consist of a sequence of Ls, Rs, and Ms in
    any order.
    :return: a list of strings, each consisting of one character that is an L, R, or M
    """

    output = []

    input_string = raw_input(prompt)
    match_obj = re.match(r'^[LMR]*$', input_string)

    if match_obj is None:
        raise Usage("Instructions must consist of L, M, or R")
    else:
        for char in match_obj.group():
            output.append(char)

    return output


def get_landing(lander):
    """
     Prompts the user to enter coordinates and a facing. They must be two positive integers
    and a facing separated by spaces. Facing must be one of N,E,S, or W.
    :param lander: The number of the lander being prompted
    :return: A list containing the inputs
    """

    output = []

    input_string = raw_input("Rover" + lander +" Landing:")
    # Looking for a number whitespace number
    # This will match 0,
    match_obj = re.match(r'^(\d+)\s+(\d+)\s+([NSEW]{1})$', input_string)

    if match_obj is None :
        raise Usage("Landing coordinates must be two positive integers and a facing (NESW).")
    else:
        output.append(int(match_obj.group(1)))
        output.append(int(match_obj.group(2)))
        output.append(match_obj.group(3))

    return output

def get_plateau():
    """
    Prompts the user to enter plateau coordinates. They must be positive integers
    separated by spaces.
    :return: a list of two ints containing the x and y coordinates specifying the plateau
    """

    output = []

    input_string = raw_input("Plateau:")
    # Looking for a number whitespace number
    # This will match 0,
    match_obj = re.match(r'^(\d+)\s+(\d+)$', input_string)

    if match_obj is None :
        raise Usage("Input coordinates must be two positive integers")
    else:
        output.append(int(match_obj.group(1)))
        output.append(int(match_obj.group(2)))

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
        plateau = get_plateau()
        landing = get_landing("Rover1")
        instruction = get_instruction("Rover1 Instructions:")

if __name__ == "__main__":
    main()


