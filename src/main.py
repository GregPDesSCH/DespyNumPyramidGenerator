"""

    DespyNumPyramidGenerator - Main Script

    Starting point for this program.

    Start Date: January 24, 2021
    End Date:

    File Name: main.py

"""

from conditions import numberIsAWholeNumber
from inputs import getNumberOfLinesFromUser, getStepWidth
from simple import printCommandMenu, getCharacterToPrint, selectPrintCommand, printPyramid

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
