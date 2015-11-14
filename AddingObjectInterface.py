#!/usr/bin/python

"""
This file will be the main way the user interacts with the database in adding objects to the database.
It will also structure the information into an SQL query so that the information can be added by the Database Manipulation script
"""

from AddingStarSubroutine import *



objectCategories = ['Star', 'Galaxy']
galaxyCategories = ['Spiral', 'Elliptical', 'Other']
spiralGalaxyCategories = ['Barred', 'Barless', 'Other']
starCategories = ['Red Giant' , 'White Dwarf' , 'Neutron' , 'Main Sequence', 'Other']
starCategoriesSize = len(starCategories)


def addCategory(CategoryVariable, listCategoriesVariable):
    listCategoriesVariable.insert(-1 , CategoryVariable)
    listCategoriesVariable = set(listCategoriesVariable)

#starTypeStatement = """Please select the number that corresponds to the type of your s, if you want to add another s type, please type in 0\n"""
    
#print starTypeStatement


def selectOrAddCategory(categoryList):
    while True:
        for category in categoryList:
            print "[" + str(categoryList.index(category) + 1) + "] " + category
        selectionInput = raw_input("Please give me the number of your selection (or type 0 to add a new type): ")
        try:
            selection = int(selectionInput)
            if selection in range(1,len(categoryList) + 1): 
                objectType = categoryList[selection - 1]
                break
            elif selection == 0:
                while True:
                    try:
                        newObjectType = str(raw_input("Please give me the name of your new type: " ))
                        addCategory(newStarType, starCategories)
                        break
                    except ValueError:
                        print("Give me an actual name for the type!")
            else:
                print("Please give me a number in the specified range")
        except ValueError:
            print("Please give me a natural number in the range sepcified")
        
         
    return objectType


def addObject():
    print "Are you going to add a star or a galaxy today?\n"

    newAddition = selectOrAddCategory(objectCategories)

    if newAddition == 'Star':
        print "What kind of star are you adding today?"
        starType = selectOrAddCategory(starCategories)
        print "You decided to add a %s star" % (starType)
        starName = addStar(starType)
        sqlstatement = '''
        INSERT INTO celestialEntities
        (Name, Kind, Radius, Mass, Redshift)
        VALUES 
        ("%s", "%s", %f, %f, %f);
        ''' % (starName, newAddition, starDict[starName].radius, starDict[starName].mass, starDict[starName].redshift)
        return sqlstatement
    elif newAddition == 'Galaxy':
        print "What kind of galaxy are you adding today?"
        galaxyType = selectOrAddCategory(galaxyCategories)
        if galaxyType == 'Spiral':
            print "What kind of spiral galaxy are you adding today?"
            spiralGalaxyType = selectOrAddCategory(spiralGalaxyCategories)
            print "You decided to add a %s %s galaxy" % (spiralGalaxyType, galaxyType)
        elif galaxyType == 'Elliptical':
            print "You decided to add a %s galaxy" % (galaxyType)