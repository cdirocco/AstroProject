#!/usr/bin/python

galaxyDict = {}

def addGalaxy(galaxyType):
     while True:
        try:
            galaxyName = str(raw_input("Please give the galaxy a name: "))
            try:
                float(galaxyName)
                int(galaxyName)
            except ValueError:
                break
        except ValueError:
            print("Please give me a name!")
            
    while True:
        try:
            galaxyWordRadius = raw_input("Please give the galaxy's radius (in parsecs): ")
            galaxyRadius = float(galaxyWordRadius)
            break
        except ValueError:
            print("Please give me a number!")
    
    while True:
        try:
            galaxyWordMass = raw_input("Please give the galaxy's mass (in solar masses): ")
            galaxyMass = float(starWordMass)
            break
        except ValueError:
            print("Please give me a number!")
    
    while True:
        try:
            galaxyWordRedshift = raw_input("Please give me the galaxy's redshift: ")
            galaxyRedshift = float(galaxyWordRedshift)
            break
        except ValueError:
            print("Please give me a number!")
            
            
    galaxyDict[galaxyName] = Galaxy(galaxyName, galaxyRadius, galaxyMass, galaxyRedshift, galaxyType)