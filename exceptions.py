#!/usr/bin/env python

""" Exceptions used by  """

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2016 Susan Sim"
__license__ = "MIT License"


class Usage(Exception):
    def __init__(self, message):
        self.message = message


class InternalError(Exception):
    def __init__(self, message):
        self.message = message


class ImproperInstruction(Exception):
    def __init__(self, message):
        self.message = message


class ImproperPlateau(Exception):
    def __init__(self, message):
        self.message = message


class ImproperLanding(Exception):
    def __init__(self, message):
        self.message = message
