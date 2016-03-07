#!/usr/bin/env python

""" MartianPlateau class

    Use by the mars program to define a plateau
"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2016 Susan Sim"
__license__ = "MIT License"


class MartianPlateau():
    def __init__(self, corner):
        """
            :param corner: A list with x,y coordinates of top right corner of Martian plateau
        """
        if isinstance(corner[0], int) and corner[0] >= 0:
            self.max_x = corner[0]
        else:
            self.max_x = 0

        if isinstance(corner[1], int) and corner[1] >= 0:
            self.max_y = corner[1]
        else:
            self.max_y = 0

    def get_x(self):
        return self.max_x

    def get_y(self):
        return self.max_y

    def is_outside(self, cell):
        """
        Returns true if an xy-coordinate is inside the MartianPlateau
        """
        if cell[0] > self.max_x or cell[1] > self.max_y:
            return True
        else:
            return False
