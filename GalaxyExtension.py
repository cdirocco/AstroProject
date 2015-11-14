#!/usr/bin/python

from AstronomicalObjects import *

class Galaxy(AstronomicalObject):
    
    def __init__(self, bodyName, bodyRadius, bodyMass, bodyRedshift, galaxyType):
        AstronomicalObject.__init__(self, bodyName, bodyRadius, bodyMass, bodyRedshift, 'Galaxy')
        self.name = bodyName
        self.radius = bodyRadius
        self.
    