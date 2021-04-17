"""

    DespyNumPyramidGenerator - Sequences

    Script responsible for printing sequences as triangles

    Initial Version
    Start Date: March 6, 2021
    End Date: April 17, 2021

    File Name: sequences.py

"""

from conditions import numberOfCharactersToPrintIsTooHigh
from inputs import (
    selectPrintPyramidCommand,
    getNumberOfLinesFromUser,
    getStepWidth,
    inputIsGoBackCommand,
    getErrorMessagePrefix
)
from generator import generateSequence, getListOfSequenceNames


# Sequence name dictionary
_FULL_NAMES_OF_SEQUENCES = {
    getListOfSequenceNames()[0]: "Fibonacci Sequence",
    getListOfSequenceNames()[1]: "Triangular Number Sequence",
    getListOfSequenceNames()[2]: "Alternating Bit Sequence",
    getListOfSequenceNames()[3]: "Sequence of Squares",
    getListOfSequenceNames()[4]: "Sequence of Powers of Twos"
}


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



def createLineSegment(sequence, maxLineSegmentLength, sequenceStringIndex):
    """
    Creates a segment of the pyramid on one line.

    Params:
    sequence - Full string representing the sequence.
    maxLineSegmentLength - Maximum length of one line segment
    sequenceStringIndex - A reference to an index for fetching sequence
    characters.

    Returns:
    currentLineSegment - A segment that will be part of the current line to
    print.
    """
    currentLineSegment = ""
    for _ in range(maxLineSegmentLength):
        currentLineSegment += sequence[sequenceStringIndex[0]]
        sequenceStringIndex[0] += 1
    return currentLineSegment


def generateSequenceLines( \
        sequence, numberOfLines, stepWidth, \
        pyramidIsUpsideDown, pyramidIsFull, pyramidIsSilhouette):
    """
    Generates all the lines to be printed in order based on sequence and other
    options chosen by the user.

    Params:
    sequence - Full string representing the sequence.
    numberOfLines - Number of lines the pyramid will be printed out of.
    stepWidth - The width of each step of the pyramid.
    pyramidIsUpsideDown - Flag to have the lines be for an upside down pyramid
    pyramidIsFull - Flag to have the lines be for a full pyramid.
    pyramidIsSilhouette - Flag to have lines be for a pyramid as a silhouette.

    Returns:
    sequenceLines - List of lines representing the pyramid to print in order.
    """
    sequenceLines = []
    sequenceStringIndex = [0]
    maxLineSegmentLength = 0

    if not pyramidIsSilhouette and not pyramidIsFull:
        # Pyramid is a triangle with a right angle
        if pyramidIsUpsideDown:
            maxLineSegmentLength = (numberOfLines + 1) * stepWidth

        for _ in range(numberOfLines):
            currentLine = ""

            maxLineSegmentLength += stepWidth \
                    * (-1 if pyramidIsUpsideDown else 1)
            pyramidSegment = createLineSegment(sequence, \
                    maxLineSegmentLength, sequenceStringIndex)

            sequenceLines.append(pyramidSegment)

    else:
        # Pyramid is either an inverse silhouette or a real one
        for lineNumber in range(numberOfLines):
            currentLine = []

            if not pyramidIsSilhouette and pyramidIsUpsideDown \
                    or pyramidIsSilhouette \
                    and not pyramidIsUpsideDown:
                maxLineSegmentLength = stepWidth * numberOfLines - lineNumber \
                        * stepWidth
            else:
                maxLineSegmentLength = (lineNumber + 1) * stepWidth

            pyramidLeftSegment = createLineSegment(sequence, \
                    maxLineSegmentLength, sequenceStringIndex)
            pyramidRightSegment = createLineSegment(sequence, \
                    maxLineSegmentLength, sequenceStringIndex)

            currentLine.append(pyramidLeftSegment)
            currentLine.append(pyramidRightSegment)

            sequenceLines.append(currentLine)

    return sequenceLines


def printPyramid(printCommand, sequence, numberOfLines, stepWidth):
    """
    Prints the pyramid out to the console.

    Params:
    printCommand
    sequence - Full string representing the sequence.
    numberOfLines - Number of lines the pyramid will be printed out of.
    stepWidth - The width of each step of the pyramid.
    """

    if numberOfCharactersToPrintIsTooHigh(
            printCommand, numberOfLines,
            stepWidth):
        # Only if any of the lines in the pyramid to print has too many
        # characters
        print(getErrorMessagePrefix() + "Maximum number of characters to be "
              "printed on the screen is 160. Please enter again.")
        return 

    if printCommand == _OPTION_TO_PRINT_UPSIDE_PYRAMID_ALIGNED_LEFT \
            or printCommand == _OPTION_TO_PRINT_ALL_PYRAMID_TYPES:
        # Pyramid with right angle on bottom left
        pyramidLines = generateSequenceLines(
                sequence, numberOfLines, stepWidth, False, False, False)

        for lineIndex in range(numberOfLines):
            leftPyramidLine = pyramidLines[lineIndex].ljust(stepWidth
                    * numberOfLines)
            print(leftPyramidLine)

    if printCommand == _OPTION_TO_PRINT_UPSIDE_PYRAMID_ALIGNED_RIGHT \
            or printCommand == _OPTION_TO_PRINT_ALL_PYRAMID_TYPES:
        # Pyramid with right angle on bottom right
        pyramidLines = generateSequenceLines(
                sequence, numberOfLines, stepWidth, False, False, False)

        for lineIndex in range(numberOfLines):
            rightPyramidLine = pyramidLines[lineIndex].rjust(stepWidth
                    * numberOfLines)
            print(rightPyramidLine)

    if printCommand == _OPTION_TO_PRINT_FULL_UPSIDE_PYRAMID \
            or printCommand == _OPTION_TO_PRINT_ALL_PYRAMID_TYPES:
        # Pyramid with base on the bottom side and made up of two joined
        # triangles
        pyramidLines = generateSequenceLines(
                sequence, numberOfLines, stepWidth, False, True, False)

        for lineIndex in range(numberOfLines):
            pyramidLeftSegment = pyramidLines[lineIndex][0].rjust(stepWidth
                    * numberOfLines)
            pyramidRightSegment = pyramidLines[lineIndex][1].ljust(stepWidth
                    * numberOfLines)
            print(pyramidLeftSegment + pyramidRightSegment)

    if printCommand == _OPTION_TO_PRINT_FULL_UPSIDE_SILHOUETTE_PYRAMID \
            or printCommand == _OPTION_TO_PRINT_ALL_PYRAMID_TYPES:
        # Pyramid is a silhouette made up of spaces with filled characters
        # outside it, with base on bottom
        pyramidLines = generateSequenceLines(
                sequence, numberOfLines, stepWidth, False, False, True)

        for lineIndex in range(numberOfLines):
            pyramidLeftSegment = pyramidLines[lineIndex][0].ljust(stepWidth
                    * numberOfLines)
            pyramidRightSegment = pyramidLines[lineIndex][1].rjust(stepWidth
                    * numberOfLines)
            print(pyramidLeftSegment + pyramidRightSegment)

    if printCommand == _OPTION_TO_PRINT_UPSIDE_DOWN_PYRAMID_ALIGNED_LEFT \
            or printCommand == _OPTION_TO_PRINT_ALL_PYRAMID_TYPES:
        # Pyramid with right angle on top left
        pyramidLines = generateSequenceLines(
                sequence, numberOfLines, stepWidth, True, False, False)

        for lineIndex in range(numberOfLines):
            leftPyramidLine = pyramidLines[lineIndex].ljust(stepWidth
                    * numberOfLines)
            print(leftPyramidLine)

    if printCommand == _OPTION_TO_PRINT_UPSIDE_DOWN_PYRAMID_ALIGNED_RIGHT \
            or printCommand == _OPTION_TO_PRINT_ALL_PYRAMID_TYPES:
        # Pyramid with right angle on top right
        pyramidLines = generateSequenceLines(
                sequence, numberOfLines, stepWidth, True, False, False)

        for lineIndex in range(numberOfLines):
            rightPyramidLine = pyramidLines[lineIndex].rjust(stepWidth
                    * numberOfLines)
            print(rightPyramidLine)

    if printCommand == _OPTION_TO_PRINT_FULL_UPSIDE_DOWN_PYRAMID \
            or printCommand == _OPTION_TO_PRINT_ALL_PYRAMID_TYPES:\
        # Pyramid with base on the top side and made up of two joined
        # triangles
        pyramidLines = generateSequenceLines(
                sequence, numberOfLines, stepWidth, True, True, False)

        for lineIndex in range(numberOfLines):
            pyramidLeftSegment = pyramidLines[lineIndex][0].rjust(stepWidth
                    * numberOfLines)
            pyramidRightSegment = pyramidLines[lineIndex][1].ljust(stepWidth
                    * numberOfLines)
            print(pyramidLeftSegment + pyramidRightSegment)

    if printCommand == _OPTION_TO_PRINT_FULL_UPSIDE_DOWN_SILHOUETTE_PYRAMID \
            or printCommand == _OPTION_TO_PRINT_ALL_PYRAMID_TYPES:
        # Pyramid is a silhouette made up of spaces with filled characters
        # outside it, with base on top
        pyramidLines = generateSequenceLines(
                sequence, numberOfLines, stepWidth, True, False, True)

        for lineIndex in range(numberOfLines):
            pyramidLeftSegment = pyramidLines[lineIndex][0].ljust(stepWidth
                    * numberOfLines)
            pyramidRightSegment = pyramidLines[lineIndex][1].rjust(stepWidth
                    * numberOfLines)
            print(pyramidLeftSegment + pyramidRightSegment)


def printSequencePyramids(sequenceName):
    """
    Loop for interacting with sequence-based pyramids.

    Params:
    sequenceName - The name of the sequence to generate the full sequence
    string.
    """
    sequence = generateSequence(sequenceName)

    while True:
        print("Pyramid: " + _FULL_NAMES_OF_SEQUENCES[sequenceName])
        printCommand = selectPrintPyramidCommand()

        if printCommand == _OPTION_TO_GO_BACK_TO_PREVIOUS_MENU:
            break

        numberOfLines = getNumberOfLinesFromUser()
        if inputIsGoBackCommand(numberOfLines):
            continue

        stepWidth = getStepWidth()
        if inputIsGoBackCommand(stepWidth):
            continue

        printPyramid(printCommand, sequence, numberOfLines, stepWidth)
        print()


# For testing only
if __name__ == "__main__":
    # print("Generating alternatingBits sequence")
    # sequence = generateSequence("fibonacci")
    # printPyramid(9, sequence, 10, 1)
    printSequencePyramids("fibonacci")
