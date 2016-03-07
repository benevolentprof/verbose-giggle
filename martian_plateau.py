#!/usr/bin/env python

""" MartianPlateau class

    Use by the mars program to define a plateau
"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2016 Susan Sim"
__license__ = "MIT License"

from martian_exceptions import ImproperPlateau
import re

class MartianPlateau():
    def __init__(self, input_string):
        """
            :param corner: A string with x,y coordinates of top right corner of Martian plateau
        """
        # Looking for a number whitespace number
        # This will match 0,
        match_obj = re.match(r'^(\d+)\s+(\d+)$', input_string)

        if match_obj is None :
            raise ImproperPlateau("Input coordinates must be two positive integers")
        else:
            self.max_x = int(match_obj.group(1))
            self.max_y = int(match_obj.group(2))


    def get_x(self):
        return self.max_x

    def get_y(self):
        return self.max_y

    def is_outside(self, cell):
        """
        Returns true if an xy-coordinate is outside the MartianPlateau
        """
        if cell[0] > self.max_x or cell[1] > self.max_y:
            return True
        else:
            return False

    def is_inside(self, cell):
        """
        Returns true if an xy-coordinate is inside the MartianPlateau
        :param cell: list of two integers
        :return: Boolean
        """
        return not self.is_outside(cell)