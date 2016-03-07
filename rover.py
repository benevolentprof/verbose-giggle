#!/usr/bin/env python

""" Rover class for use with Mars Rover script """

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2016 Susan Sim"
__license__ = "MIT License"

import re
from martian_exceptions import InternalError, ImproperLanding, ImproperInstruction
from martian_plateau import MartianPlateau


class Rover():

    def __init__(self, input_string, plateau):
        # Looking for a number whitespace number
        # This will match 0,
        match_obj = re.match(r'^(\d+)\s+(\d+)\s+([NSEW]{1})$', input_string)

        if match_obj is None:
            raise ImproperLanding("Landing coordinates must be two positive integers and a facing (NESW).")
        else:
            self.x = int(match_obj.group(1))
            self.y = int(match_obj.group(2))
            self.facing = match_obj.group(3)

        if isinstance(plateau, MartianPlateau):
            self.plateau = plateau
        else:
            raise InternalError("Argument was not of type MartianPlateau")

        if plateau.is_outside([self.x, self.y]):
            raise ImproperLanding("Landing coordinates must be inside the plateau.")


    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_facing(self):
        return self.facing

    def __turn_left(self):
        if self.facing == "N":
            self.facing = "W"
        elif self.facing == "E":
            self.facing = "N"
        elif self.facing == "S":
            self.facing = "E"
        elif self.facing == "W":
            self.facing = "S"
        else:
            raise InternalError("Invalid facing: " + self.facing)

    def __turn_right(self):
        if self.facing == "N":
            self.facing = "E"
        elif self.facing == "E":
            self.facing = "S"
        elif self.facing == "S":
            self.facing = "W"
        elif self.facing == "W":
            self.facing = "N"
        else:
            raise InternalError("Invalid facing: " + self.facing)

    def __move(self):
        if self.facing == "N":
            if self.plateau.is_inside([self.x, self.y + 1]):
                self.y += 1
        elif self.facing == "E":
            if self.plateau.is_inside([self.x + 1, self.y]):
                self.x += 1
        elif self.facing == "W":
            if self.plateau.is_inside([self.x - 1, self.y]):
                self.x -= 1
        elif self.facing == "S":
            if self.plateau.is_inside([self.x, self.y - 1]):
                self.y -= 1
        else:
            raise InternalError("Invalid facing: " + self.facing)

    def instruct(self, input_string):

        match_obj = re.match(r'^([LMR])+$', input_string)

        if match_obj is None:
            raise ImproperInstruction("Instructions must consist of L, M, or R")
        else:
            for char in match_obj.group():
                if char == "L":
                    self.__turn_left()
                elif char == "R":
                    self.__turn_right()
                elif char == "M":
                    self.__move()
                else:
                    raise InternalError("Invalid facing: " + self.facing)

            return "%d %d %s" % (self.x, self.y, self.facing)
