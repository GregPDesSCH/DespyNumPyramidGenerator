"""

    DespyNumPyramidGenerator - Conditions

    Performs simple pyramid prints.

    Start Date: March 9, 2021
    End Date:

    File Name: simple.py

"""

from conditions import numberIsAWholeNumber

def printCommandMenu():
    print("Pick an option from one of the following:", "1 - Left Pyramid", "2 - Right Pyramid", "3 - Full Pyramid",
        "4 - Silhouette Pyramid", "5 - Upside Down Left Pyramid", "6 - Upside Down Right Pyramid", 
        "7 - Upside Down Pyrmaid", "8 - Silhouette Pyramid (Upside Down)", "9 - All Options", "10 - Quit", sep="\n")

def getCharacterToPrint():
    characterToPrint = ""
    while len(characterToPrint) != 1:
        characterToPrint = input('Character to print pyramids? ')
        if len(characterToPrint) == 0:
            print("ERROR - Input must not be empty.")
        elif len(characterToPrint) > 1:
            print("ERROR - Input must be exactly one character long.")

    return characterToPrint

def selectPrintCommand():
    rawPrintCommand = ""
    printCommand = 0
    while len(rawPrintCommand) < 0 or len(rawPrintCommand) > 2 or printCommand < 1 or printCommand > 10 \
        or not numberIsAWholeNumber(rawPrintCommand):
        printCommandMenu()
        rawPrintCommand = input('Select option [1-10]: ')
        if len(rawPrintCommand) == 0:
            print("ERROR - Input must not be empty.")
        elif not numberIsAWholeNumber(rawPrintCommand):
            print("ERROR - Input must be a whole positive number.")
        else:
            printCommand = int(rawPrintCommand)
            if printCommand < 1 or printCommand > 10:
                print("ERROR - Command must be in the range [1-8].")
    
    return printCommand

