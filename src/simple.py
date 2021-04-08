"""

    DespyNumPyramidGenerator - Conditions

    Performs simple pyramid prints.

    Start Date: March 9, 2021
    End Date:

    File Name: simple.py

"""

from conditions import numberOfCharactersToPrintIsTooHigh
from inputs import ( 
    selectPrintPyramidCommand,
    getNumberOfLinesFromUser, 
    getStepWidth, 
    inputIsGoBackCommand, 
    getErrorMessagePrefix, 
    getInputEmptyErrorMessage 
)


_OPTION_TO_PRINT_UPSIDE_PYRAMID_ALIGNED_LEFT = 1
_OPTION_TO_PRINT_UPSIDE_PYRAMID_ALIGNED_RIGHT = 2
_OPTION_TO_PRINT_FULL_UPSIDE_PYRAMID = 3
_OPTION_TO_PRINT_FULL_UPSIDE_SILHOUETTE_PYRAMID = 4
_OPTION_TO_PRINT_UPSIDE_DOWN_PYRAMID_ALIGNED_LEFT = 5
_OPTION_TO_PRINT_UPSIDE_DOWN_PYRAMID_ALIGNED_RIGHT = 6
_OPTION_TO_PRINT_FULL_UPSIDE_DOWN_PYRAMID = 7
_OPTION_TO_PRINT_FULL_UPSIDE_DOWN_SILHOUETTE_PYRAMID = 8
_OPTION_TO_PRINT_ALL_PYRAMID_TYPES = 9
_OPTION_TO_GO_BACK_TO_PREVIOUS_MENU = 10


def getCharacterToPrint():
    characterToPrint = ""

    while len(characterToPrint) != 1 and not inputIsGoBackCommand(characterToPrint):
        print("Enter a character to create the triangle out of, or type -- to go back to the previous menu.")

        characterToPrint = input("Character? ")
        if len(characterToPrint) == 0:
            print(getInputEmptyErrorMessage())
        elif len(characterToPrint) > 1 and not inputIsGoBackCommand(characterToPrint):
            print(getErrorMessagePrefix() + "Input must be exactly one character long.")

        print()

    return characterToPrint


def printPyramid(printCommand, numberOfLines, characterToPrint, stepWidth):
    if numberOfCharactersToPrintIsTooHigh(printCommand, numberOfLines, stepWidth):
        print(getErrorMessagePrefix() + "Maximum number of characters to be printed on the screen is 160. Please enter again.")
        return

    # Left Pyramid
    if printCommand == _OPTION_TO_PRINT_UPSIDE_PYRAMID_ALIGNED_LEFT or printCommand == _OPTION_TO_PRINT_ALL_PYRAMID_TYPES:
        for lineIndex in range(numberOfLines):
            pyramidSegment = "".ljust(stepWidth * (lineIndex + 1), characterToPrint).ljust(stepWidth * numberOfLines)
            print(pyramidSegment)

    # Right Pyramid
    if printCommand == _OPTION_TO_PRINT_UPSIDE_PYRAMID_ALIGNED_RIGHT or printCommand == _OPTION_TO_PRINT_ALL_PYRAMID_TYPES:
        for lineIndex in range(numberOfLines):
            pyramidSegment = "".ljust(stepWidth * (lineIndex + 1), characterToPrint).rjust(stepWidth * numberOfLines)
            print(pyramidSegment)

    # Full Pyramid
    if printCommand == _OPTION_TO_PRINT_FULL_UPSIDE_PYRAMID or printCommand == _OPTION_TO_PRINT_ALL_PYRAMID_TYPES:
        for lineIndex in range(numberOfLines):
            pyramidLeftSegment = "".ljust(stepWidth * (lineIndex + 1), characterToPrint).rjust(stepWidth * numberOfLines)
            pyramidRightSegment = "".rjust(stepWidth * (lineIndex + 1), characterToPrint).ljust(stepWidth * numberOfLines)
            print(pyramidLeftSegment + pyramidRightSegment)

    # Silhouette Pyramid
    if printCommand == _OPTION_TO_PRINT_FULL_UPSIDE_SILHOUETTE_PYRAMID or printCommand == _OPTION_TO_PRINT_ALL_PYRAMID_TYPES:
        for lineIndex in range(numberOfLines):
            pyramidLeftSegment = "".ljust(stepWidth * (numberOfLines - (lineIndex)), characterToPrint).ljust(stepWidth * numberOfLines)
            pyramidRightSegment = "".rjust(stepWidth * (numberOfLines - (lineIndex)), characterToPrint).rjust(stepWidth * numberOfLines)
            print(pyramidLeftSegment + pyramidRightSegment)

    # Upside Down Left Pyramid
    if printCommand == _OPTION_TO_PRINT_UPSIDE_DOWN_PYRAMID_ALIGNED_LEFT or printCommand == _OPTION_TO_PRINT_ALL_PYRAMID_TYPES:
        for lineIndex in range(numberOfLines):
            pyramidSegment = "".ljust(stepWidth * (numberOfLines - (lineIndex)), characterToPrint).ljust(stepWidth * numberOfLines)
            print(pyramidSegment)

    # Upside Down Right Pyramid
    if printCommand == _OPTION_TO_PRINT_UPSIDE_DOWN_PYRAMID_ALIGNED_RIGHT or printCommand == _OPTION_TO_PRINT_ALL_PYRAMID_TYPES:
        for lineIndex in range(numberOfLines):
            pyramidSegment = "".rjust(stepWidth * (numberOfLines - (lineIndex)), characterToPrint).rjust(stepWidth * numberOfLines)
            print(pyramidSegment)

    # Upside Down Pyramid
    if printCommand == _OPTION_TO_PRINT_FULL_UPSIDE_DOWN_PYRAMID or printCommand == _OPTION_TO_PRINT_ALL_PYRAMID_TYPES:
        for lineIndex in range(numberOfLines):
            pyramidLeftSegment = "".ljust(stepWidth * (numberOfLines - (lineIndex)), characterToPrint).rjust(stepWidth * numberOfLines)
            pyramidRightSegment = "".rjust(stepWidth * (numberOfLines - (lineIndex)), characterToPrint).ljust(stepWidth * numberOfLines)
            print(pyramidLeftSegment + pyramidRightSegment)

    # Silhouette Pyramid (Upside Down)
    if printCommand == _OPTION_TO_PRINT_FULL_UPSIDE_DOWN_SILHOUETTE_PYRAMID or printCommand == _OPTION_TO_PRINT_ALL_PYRAMID_TYPES:
        for lineIndex in range(numberOfLines):
            pyramidLeftSegment = "".ljust(stepWidth * (lineIndex + 1), characterToPrint).ljust(stepWidth * numberOfLines)
            pyramidRightSegment = "".rjust(stepWidth * (lineIndex + 1), characterToPrint).rjust(stepWidth * numberOfLines)
            print(pyramidLeftSegment + pyramidRightSegment)


def printSimplePyramids():
    while True:
        print("Pyramid: Simple")
        printCommand = selectPrintPyramidCommand()

        if printCommand == _OPTION_TO_GO_BACK_TO_PREVIOUS_MENU:
            break

        characterToPrint = getCharacterToPrint()
        if inputIsGoBackCommand(characterToPrint):
            continue

        numberOfLines = getNumberOfLinesFromUser()
        if inputIsGoBackCommand(numberOfLines):
            continue

        stepWidth = getStepWidth()
        if inputIsGoBackCommand(stepWidth):
            continue

        printPyramid(printCommand, numberOfLines, characterToPrint, stepWidth)
        print()


# For testing only
if __name__ == "__main__":
    printPyramid(9, 10, "5", 2)