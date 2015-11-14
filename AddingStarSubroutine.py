#!/usr/bin/python

"This file will contain the method by which we make a star class object to be added to the database"

starDict = {}

from StarExtension import *

def addStar(starType):
    while True:
        try:
            starName = str(raw_input("Please give the star a name: "))
            break
        except ValueError:
            print("Please give me a name!")
            
    while True:
        try:
            starWordRadius = raw_input("Please give the star's radius (in parsecs): ")
            starRadius = float(starWordRadius)
            break
        except ValueError:
            print("Please give me a number!")
    
    while True:
        try:
            starWordMass = raw_input("Please give the star's mass (in solar masses): ")
            starMass = float(starWordMass)
            break
        except ValueError:
            print("Please give me a number!")
    
    while True:
        try:
            starWordRedshift = raw_input("Please give me the star's redshift: ")
            starRedshift = float(starWordRedshift)
            break
        except ValueError:
            print("Please give me a number!")
            
    
    starDict[starName] = Star(starName,starRadius,starMass,starRedshift, starType)
    return starName
    
    
    
    
    