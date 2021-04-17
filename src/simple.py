"""

    DespyNumPyramidGenerator - Conditions

    Performs simple pyramid prints.

    Initial Version
    Start Date: March 9, 2021
    End Date: April 17, 2021

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


# Constants for different pyramid orientation options
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
    """
    Reads in user input for selecting the character to fill the pyramid with.

    Returns:
    characterToPrint - User's selection of a character.
    """
    characterToPrint = ""

    while len(characterToPrint) != 1 \
            and not inputIsGoBackCommand(characterToPrint):
        print("Enter a character to create the triangle out of, or type -- to "
              "go back to the previous menu.")

        characterToPrint = input("Character? ")
        if len(characterToPrint) == 0:
            print(getInputEmptyErrorMessage())
        elif len(characterToPrint) > 1 \
                and not inputIsGoBackCommand(characterToPrint):
            print(getErrorMessagePrefix() + "Input must be exactly one "
                  "character long.")

        print()

    return characterToPrint


def printPyramid(printCommand, numberOfLines, characterToPrint, stepWidth):
    """
    Prints the pyramid out to the console.

    Params:
    printCommand - User's choice for pyramid orientation.
    numberOfLines - Number of lines the pyramid will be printed out of.
    characterToPrint - The character to fill the pyramid with.
    stepWidth - The width of each step of the pyramid.
    """

    if numberOfCharactersToPrintIsTooHigh(
                printCommand, numberOfLines, stepWidth):
        # Only if any of the lines in the pyramid to print has too many
        # characters
        print(getErrorMessagePrefix() + "Maximum number of characters to be "
              "printed on the screen is 160. Please enter again.")
        return

    if printCommand == _OPTION_TO_PRINT_UPSIDE_PYRAMID_ALIGNED_LEFT \
            or printCommand == _OPTION_TO_PRINT_ALL_PYRAMID_TYPES:
        # Pyramid with right angle on bottom left
        for lineIndex in range(numberOfLines):
            pyramidSegment = "".ljust(stepWidth * (lineIndex + 1), 
                    characterToPrint).ljust(stepWidth * numberOfLines)
            print(pyramidSegment)

    if printCommand == _OPTION_TO_PRINT_UPSIDE_PYRAMID_ALIGNED_RIGHT \
            or printCommand == _OPTION_TO_PRINT_ALL_PYRAMID_TYPES:
        # Pyramid with right angle on bottom right
        for lineIndex in range(numberOfLines):
            pyramidSegment = "".ljust(stepWidth * (lineIndex + 1), 
                    characterToPrint).rjust(stepWidth * numberOfLines)
            print(pyramidSegment)

    if printCommand == _OPTION_TO_PRINT_FULL_UPSIDE_PYRAMID \
            or printCommand == _OPTION_TO_PRINT_ALL_PYRAMID_TYPES:
        # Pyramid with base on the bottom side and made up of two joined
        # triangles
        for lineIndex in range(numberOfLines):
            pyramidLeftSegment = "".ljust(stepWidth * (lineIndex + 1), 
                    characterToPrint).rjust(stepWidth * numberOfLines)
            pyramidRightSegment = "".rjust(stepWidth * (lineIndex + 1), 
                    characterToPrint).ljust(stepWidth * numberOfLines)
            print(pyramidLeftSegment + pyramidRightSegment)

    if printCommand == _OPTION_TO_PRINT_FULL_UPSIDE_SILHOUETTE_PYRAMID \
            or printCommand == _OPTION_TO_PRINT_ALL_PYRAMID_TYPES:
        # Pyramid is a silhouette made up of spaces with filled characters
        # outside it, with base on bottom
        for lineIndex in range(numberOfLines):
            pyramidLeftSegment = "".ljust(stepWidth * (numberOfLines \
                    - (lineIndex)), characterToPrint).ljust(stepWidth \
                    * numberOfLines)
            pyramidRightSegment = "".rjust(stepWidth * (numberOfLines \
                    - (lineIndex)), characterToPrint).rjust(stepWidth \
                    * numberOfLines)
            print(pyramidLeftSegment + pyramidRightSegment)

    if printCommand == _OPTION_TO_PRINT_UPSIDE_DOWN_PYRAMID_ALIGNED_LEFT \
            or printCommand == _OPTION_TO_PRINT_ALL_PYRAMID_TYPES:
        # Pyramid with right angle on top left
        for lineIndex in range(numberOfLines):
            pyramidSegment = "".ljust(stepWidth * (numberOfLines - \
                    (lineIndex)), characterToPrint).ljust(stepWidth \
                    * numberOfLines)
            print(pyramidSegment)

    if printCommand == _OPTION_TO_PRINT_UPSIDE_DOWN_PYRAMID_ALIGNED_RIGHT \
            or printCommand == _OPTION_TO_PRINT_ALL_PYRAMID_TYPES:
        # Pyramid with right angle on top right
        for lineIndex in range(numberOfLines):
            pyramidSegment = "".rjust(stepWidth * (numberOfLines - \
                    (lineIndex)), characterToPrint).rjust(stepWidth \
                    * numberOfLines)
            print(pyramidSegment)

    if printCommand == _OPTION_TO_PRINT_FULL_UPSIDE_DOWN_PYRAMID \
            or printCommand == _OPTION_TO_PRINT_ALL_PYRAMID_TYPES:
        # Pyramid with base on the top side and made up of two joined
        # triangles
        for lineIndex in range(numberOfLines):
            pyramidLeftSegment = "".ljust(stepWidth * (numberOfLines - \
                    (lineIndex)), characterToPrint).rjust(stepWidth 
                    * numberOfLines)
            pyramidRightSegment = "".rjust(stepWidth * (numberOfLines - \
                    (lineIndex)), characterToPrint).ljust(stepWidth \
                    * numberOfLines)
            print(pyramidLeftSegment + pyramidRightSegment)

    if printCommand == _OPTION_TO_PRINT_FULL_UPSIDE_DOWN_SILHOUETTE_PYRAMID \
            or printCommand == _OPTION_TO_PRINT_ALL_PYRAMID_TYPES:
        # Pyramid is a silhouette made up of spaces with filled characters 
        # outside it, with base on top
        for lineIndex in range(numberOfLines):
            pyramidLeftSegment = "".ljust(stepWidth * (lineIndex + 1), \
                    characterToPrint).ljust(stepWidth * numberOfLines)
            pyramidRightSegment = "".rjust(stepWidth * (lineIndex + 1), \
                        characterToPrint).rjust(stepWidth * numberOfLines)
            print(pyramidLeftSegment + pyramidRightSegment)


def printSimplePyramids():
    """Loop for interacting with simple pyramids"""
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