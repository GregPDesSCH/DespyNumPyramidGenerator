"""

    DespyNumPyramidGenerator - Main Script

    Starting point for this program.

    Start Date: January 24, 2021
    End Date:

    File Name: main.py

"""

from conditions import numberIsAWholeNumber
from inputs import getNumberOfLinesFromUser
from simple import printCommandMenu, getCharacterToPrint, selectPrintCommand, printPyramid


def getStepWidth():
    rawStepWidth = ""
    stepWidth = 0

    while len(rawStepWidth) == 0 or stepWidth < 1 or stepWidth > 10 or not numberIsAWholeNumber(rawStepWidth):
        rawStepWidth = input("Width of each step? ")
        if len(rawStepWidth) == 0:
            print("ERROR - Input must not be empty.")
        elif not numberIsAWholeNumber(rawStepWidth):
            print("ERROR - Input must be a whole positive number.")
        else:
            stepWidth = int(rawStepWidth)
            if stepWidth < 1 or stepWidth > 10:
                print("ERROR - Step width must be in the range [1-10].")

    return stepWidth



def main():
    while True:
        printCommand = selectPrintCommand()

        if printCommand == 10:
            break

        numberOfLines = getNumberOfLinesFromUser()
        characterToPrint = getCharacterToPrint()
        stepWidth = getStepWidth()

        printPyramid(printCommand, numberOfLines, characterToPrint, stepWidth)


if __name__ == "__main__":
    main()
