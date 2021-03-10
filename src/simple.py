"""

    DespyNumPyramidGenerator - Conditions

    Performs simple pyramid prints.

    Start Date: March 9, 2021
    End Date:

    File Name: simple.py

"""

def getCharacterToPrint():
    characterToPrint = ""
    while len(characterToPrint) != 1:
        characterToPrint = input('Character to print pyramids? ')
        if len(characterToPrint) == 0:
            print("ERROR - Input must not be empty.")
        elif len(characterToPrint) > 1:
            print("ERROR - Input must be exactly one character long.")

    return characterToPrint