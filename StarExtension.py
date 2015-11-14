#!/usr/bin/python

"This file will contain the star extension"


from AstronomicalObjects import *


starCategories = ['Red Giant' , 'White Dwarf' , 'Neutron' , 'Main Sequence', 'Other']
starCategoriesSelection = list(enumerate(starCategories, start = 1))

class Star(AstronomicalObject):
    
    def __init__(self, bodyName, bodyRadius, bodyMass, bodyRedshift, starType):
        AstronomicalObject.__init__(self, bodyName, bodyRadius, bodyMass, bodyRedshift, 'Star')
        self.name = bodyName
        self.radius = bodyRadius
        self.mass = bodyMass
        self.redshift = bodyRedshift
        self.stype = starType
        self.volume = 4.0/3.0 * math.pi * (self.radius) ** 3
        self.density = self.mass/self.volume
        if self.mass < 0.43 and self.mass > 0:
            self.luminosity = 0.23 * self.mass ** 2.3
        elif self.mass >= 0.43 and self.mass < 2.0:
            self.luminosity = self.mass ** 4.0
        elif self.mass >= 2.0 and self.mass < 20.0:
            self.luminosity = 1.5 * self.mass ** 3.5
        elif self.mass >= 20.0:
            self.luminosity = 3200 * self.mass
        
        
