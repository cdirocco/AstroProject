#!/usr/bin/python

"""This file will contain the basic class structure of my astronomical bodies including extension of the classes to categorise planets, galaxies and stars"""

import math

class AstronomicalObject(object):
    def __init__(self, bodyName, bodyRadius, bodyMass, bodyRedshift, bodyKind):
        self.name = bodyName
        self.radius = bodyRadius
        self.mass = bodyMass
        self.redshift = bodyRedshift
        self.kind = bodyKind
    
    def numberFormat(number):
        if number < 10 ** 4 and number > 10 ** -2:
            return '%.4g'
        else:
            return '%.3e'
        
    
    def getName(self):
        print self.name
    
    def getRadius(self):
        print "The size of %s is " %(self.name) + numberFormat(self.radius) %self.radius + " parsecs"
        
    def getMass(self):
        print "The mass of %s is " %(self.name) + numberFormat(self.mass) %self.mass + " solar masses"
    
    def resdhift(self):
        print "%s has a redshift of " %(self.name) + numberFormat(self.redshift) %self.redshift 