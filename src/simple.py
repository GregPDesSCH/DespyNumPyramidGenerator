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

_optionToPrintUpsidePyramidAlignedLeft = 1
_optionToPrintUpsidePyramidAlignedRight = 2
_optionToPrintFullUpsidePyramid = 3
_optionToPrintFullUpsideSilhouettePyramid = 4
_optionToPrintUpsideDownPyramidAlignedLeft = 5
_optionToPrintUpsideDownPyramidAlignedRight = 6
_optionToPrintFullUpsideDownPyramid = 7
_optionToPrintFullUpsideDownSilhouettePyramid = 8
_optionToPrintAllPyramidTypes = 9
_optionToGoBackToPreviousMenu = 10


def getCharacterToPrint():
    characterToPrint = ""

    while len(characterToPrint) != 1 and not inputIsGoBackCommand(characterToPrint):
        print("Enter a character to create the triangle out of, or type -- to go back to the previous menu.")

        characterToPrint = input('Character? ')
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
    if printCommand == _optionToPrintUpsidePyramidAlignedLeft or printCommand == _optionToPrintAllPyramidTypes:
        for lineIndex in range(numberOfLines):
            pyramidSegment = "".ljust(stepWidth * (lineIndex + 1), characterToPrint).ljust(stepWidth * numberOfLines)
            print(pyramidSegment)

    # Right Pyramid
    if printCommand == _optionToPrintUpsidePyramidAlignedRight or printCommand == _optionToPrintAllPyramidTypes:
        for lineIndex in range(numberOfLines):
            pyramidSegment = "".ljust(stepWidth * (lineIndex + 1), characterToPrint).rjust(stepWidth * numberOfLines)
            print(pyramidSegment)

    # Full Pyramid
    if printCommand == _optionToPrintFullUpsidePyramid or printCommand == _optionToPrintAllPyramidTypes:
        for lineIndex in range(numberOfLines):
            pyramidLeftSegment = "".ljust(stepWidth * (lineIndex + 1), characterToPrint).rjust(stepWidth * numberOfLines)
            pyramidRightSegment = "".rjust(stepWidth * (lineIndex + 1), characterToPrint).ljust(stepWidth * numberOfLines)
            print(pyramidLeftSegment + pyramidRightSegment)

    # Silhouette Pyramid
    if printCommand == _optionToPrintFullUpsideSilhouettePyramid or printCommand == _optionToPrintAllPyramidTypes:
        for lineIndex in range(numberOfLines):
            pyramidLeftSegment = "".ljust(stepWidth * (numberOfLines - (lineIndex)), characterToPrint).ljust(stepWidth * numberOfLines)
            pyramidRightSegment = "".rjust(stepWidth * (numberOfLines - (lineIndex)), characterToPrint).rjust(stepWidth * numberOfLines)
            print(pyramidLeftSegment + pyramidRightSegment)

    # Upside Down Left Pyramid
    if printCommand == _optionToPrintUpsideDownPyramidAlignedLeft or printCommand == _optionToPrintAllPyramidTypes:
        for lineIndex in range(numberOfLines):
            pyramidSegment = "".ljust(stepWidth * (numberOfLines - (lineIndex)), characterToPrint).ljust(stepWidth * numberOfLines)
            print(pyramidSegment)

    # Upside Down Right Pyramid
    if printCommand == _optionToPrintUpsideDownPyramidAlignedRight or printCommand == _optionToPrintAllPyramidTypes:
        for lineIndex in range(numberOfLines):
            pyramidSegment = "".rjust(stepWidth * (numberOfLines - (lineIndex)), characterToPrint).rjust(stepWidth * numberOfLines)
            print(pyramidSegment)

    # Upside Down Pyramid
    if printCommand == _optionToPrintFullUpsideDownPyramid or printCommand == _optionToPrintAllPyramidTypes:
        for lineIndex in range(numberOfLines):
            pyramidLeftSegment = "".ljust(stepWidth * (numberOfLines - (lineIndex)), characterToPrint).rjust(stepWidth * numberOfLines)
            pyramidRightSegment = "".rjust(stepWidth * (numberOfLines - (lineIndex)), characterToPrint).ljust(stepWidth * numberOfLines)
            print(pyramidLeftSegment + pyramidRightSegment)

    # Silhouette Pyramid (Upside Down)
    if printCommand == _optionToPrintFullUpsideDownSilhouettePyramid or printCommand == _optionToPrintAllPyramidTypes:
        for lineIndex in range(numberOfLines):
            pyramidLeftSegment = "".ljust(stepWidth * (lineIndex + 1), characterToPrint).ljust(stepWidth * numberOfLines)
            pyramidRightSegment = "".rjust(stepWidth * (lineIndex + 1), characterToPrint).rjust(stepWidth * numberOfLines)
            print(pyramidLeftSegment + pyramidRightSegment)


def printSimplePyramids():
    while True:
        print("Pyramid: Simple")
        printCommand = selectPrintPyramidCommand()

        if printCommand == _optionToGoBackToPreviousMenu:
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
    printPyramid(9, 10, '5', 2)