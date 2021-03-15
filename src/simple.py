"""

    DespyNumPyramidGenerator - Conditions

    Performs simple pyramid prints.

    Start Date: March 9, 2021
    End Date:

    File Name: simple.py

"""

from conditions import numberIsAWholeNumber
from inputs import printCommandMenu, getNumberOfLinesFromUser, getStepWidth



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

def printPyramid(printCommand, numberOfLines, characterToPrint, stepWidth):
    if numberOfLines * stepWidth > 160:
        print("ERROR - Maximum number of characters to be printed on the screen is 160. Please enter again.")
    else:
        if printCommand == 1 or printCommand == 9:
            # Left Pyramid
            for lineIndex in range(numberOfLines):
                print("".ljust(stepWidth * (lineIndex + 1), characterToPrint).ljust(stepWidth * numberOfLines))

        if printCommand == 2 or printCommand == 9:
            # Right Pyramid
            for lineIndex in range(numberOfLines):
                print("".ljust(stepWidth * (lineIndex + 1), characterToPrint).rjust(stepWidth * numberOfLines))

        if printCommand == 3 or printCommand == 9:
            # Full Pyramid
            for lineIndex in range(numberOfLines):
                print("".ljust(stepWidth * (lineIndex + 1), characterToPrint).rjust(stepWidth * numberOfLines) + \
                    "".rjust(stepWidth * (lineIndex + 1), characterToPrint).ljust(stepWidth * numberOfLines))

        if printCommand == 4 or printCommand == 9:
            # Silhouette Pyramid
            for lineIndex in range(numberOfLines):
                print("".ljust(stepWidth * (numberOfLines - (lineIndex)), characterToPrint).ljust(stepWidth * numberOfLines) + \
                    "".rjust(stepWidth * (numberOfLines - (lineIndex)), characterToPrint).rjust(stepWidth * numberOfLines))

        if printCommand == 5 or printCommand == 9:
            # Upside Down Left Pyramid
            for lineIndex in range(numberOfLines):
                print("".ljust(stepWidth * (numberOfLines - (lineIndex)), characterToPrint).ljust(stepWidth * numberOfLines))

        if printCommand == 6 or printCommand == 9:
            # Upside Down Right Pyramid
            for lineIndex in range(numberOfLines):
                print("".rjust(stepWidth * (numberOfLines - (lineIndex)), characterToPrint).rjust(stepWidth * numberOfLines))

        if printCommand == 7 or printCommand == 9:
            # Upside Down Pyramid
            for lineIndex in range(numberOfLines):
                print("".ljust(stepWidth * (numberOfLines - (lineIndex)), characterToPrint).rjust(stepWidth * numberOfLines) + \
                    "".rjust(stepWidth * (numberOfLines - (lineIndex)), characterToPrint).ljust(stepWidth * numberOfLines))

        if printCommand == 8 or printCommand == 9:
            # Silhouette Pyramid (Upside Down)
            for lineIndex in range(numberOfLines):
                print("".ljust(stepWidth * (lineIndex + 1), characterToPrint).ljust(stepWidth * numberOfLines) + \
                    "".rjust(stepWidth * (lineIndex + 1), characterToPrint).rjust(stepWidth * numberOfLines))

def printSimplePyramids():
    while True:
        printCommand = selectPrintCommand()

        if printCommand == 10:
            break

        numberOfLines = getNumberOfLinesFromUser()
        characterToPrint = getCharacterToPrint()
        stepWidth = getStepWidth()

        printPyramid(printCommand, numberOfLines, characterToPrint, stepWidth)