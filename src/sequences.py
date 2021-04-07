"""

    DespyNumPyramidGenerator - Sequences

    Script responsible for printing triangles as sequences

    Start Date: March 6, 2021
    End Date:

    File Name: sequences.py

"""

from conditions import numberOfCharactersToPrintIsTooHigh
from inputs import selectPrintPyramidCommand, getNumberOfLinesFromUser, getStepWidth, inputIsGoBackCommand, getErrorMessagePrefix
from generator import generateSequence


_fullNamesOfSequences = {
    "fibonacci": "Fibonacci Sequence",
    "triangle": "Triangular Number Sequence",
    "alternatingBits": "Alternating Bit Sequence"
}

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



def createLineSegment(sequence, maxLineSegmentLength, sequenceStringIndex):
    currentLineSegment = ""
    for _ in range(maxLineSegmentLength):
        currentLineSegment += sequence[sequenceStringIndex[0]]
        sequenceStringIndex[0] += 1
    return currentLineSegment


def generateSequenceLines(sequence, numberOfLines, stepWidth, pyramidIsUpsideDown, pyramidIsFull, pyramidIsSilhouette):
    sequenceLines = []
    sequenceStringIndex = [0]
    maxLineSegmentLength = 0

    if pyramidIsSilhouette == False and pyramidIsFull == False:
        if pyramidIsUpsideDown == True:
            maxLineSegmentLength = (numberOfLines + 1) * stepWidth

        for _ in range(numberOfLines):
            currentLine = ""

            maxLineSegmentLength += stepWidth * (-1 if pyramidIsUpsideDown == True else 1)
            pyramidSegment = createLineSegment(sequence, maxLineSegmentLength, sequenceStringIndex)

            sequenceLines.append(pyramidSegment)

    else:
        for lineNumber in range(numberOfLines):
            currentLine = []
            
            if pyramidIsSilhouette == True and pyramidIsUpsideDown == False or pyramidIsSilhouette == False \
                    and pyramidIsUpsideDown == True:
                maxLineSegmentLength = stepWidth * numberOfLines - lineNumber * stepWidth
            else:
                maxLineSegmentLength = (lineNumber + 1) * stepWidth

            pyramidLeftSegment = createLineSegment(sequence, maxLineSegmentLength, sequenceStringIndex)
            pyramidRightSegment = createLineSegment(sequence, maxLineSegmentLength, sequenceStringIndex)

            currentLine.append(pyramidLeftSegment)
            currentLine.append(pyramidRightSegment)

            sequenceLines.append(currentLine)

    return sequenceLines


def printPyramid(printCommand, sequence, numberOfLines, stepWidth):
    if numberOfCharactersToPrintIsTooHigh(printCommand, numberOfLines, stepWidth):
        print(getErrorMessagePrefix() + "Maximum number of characters to be printed on the screen is 160. Please enter again.")
        return 
    
    # Left Pyramid
    if printCommand == _optionToPrintUpsidePyramidAlignedLeft or printCommand == _optionToPrintAllPyramidTypes:
        pyramidLines = generateSequenceLines(sequence, numberOfLines, stepWidth, False, False, False)

        for lineIndex in range(numberOfLines):
            leftPyramidLine = pyramidLines[lineIndex].ljust(stepWidth * numberOfLines)
            print(leftPyramidLine)

    # Right Pyramid
    if printCommand == _optionToPrintUpsidePyramidAlignedRight or printCommand == _optionToPrintAllPyramidTypes:
        pyramidLines = generateSequenceLines(sequence, numberOfLines, stepWidth, False, False, False)

        for lineIndex in range(numberOfLines):
            rightPyramidLine = pyramidLines[lineIndex].rjust(stepWidth * numberOfLines)
            print(rightPyramidLine)

    # Full Pyramid
    if printCommand == _optionToPrintFullUpsidePyramid or printCommand == _optionToPrintAllPyramidTypes:
        pyramidLines = generateSequenceLines(sequence, numberOfLines, stepWidth, False, True, False)

        for lineIndex in range(numberOfLines):
            pyramidLeftSegment = pyramidLines[lineIndex][0].rjust(stepWidth * numberOfLines)
            pyramidRightSegment = pyramidLines[lineIndex][1].ljust(stepWidth * numberOfLines)
            print(pyramidLeftSegment + pyramidRightSegment)

    # Silhouette Pyramid
    if printCommand == _optionToPrintFullUpsideSilhouettePyramid or printCommand == _optionToPrintAllPyramidTypes:
        pyramidLines = generateSequenceLines(sequence, numberOfLines, stepWidth, False, False, True)

        for lineIndex in range(numberOfLines):
            pyramidLeftSegment = pyramidLines[lineIndex][0].ljust(stepWidth * numberOfLines)
            pyramidRightSegment = pyramidLines[lineIndex][1].rjust(stepWidth * numberOfLines)
            print(pyramidLeftSegment + pyramidRightSegment)

    # Upside Down Left Pyramid
    if printCommand == _optionToPrintUpsideDownPyramidAlignedLeft or printCommand == _optionToPrintAllPyramidTypes:
        pyramidLines = generateSequenceLines(sequence, numberOfLines, stepWidth, True, False, False)

        for lineIndex in range(numberOfLines):
            leftPyramidLine = pyramidLines[lineIndex].ljust(stepWidth * numberOfLines)
            print(leftPyramidLine)

    # Upside Down Right Pyramid
    if printCommand == _optionToPrintUpsideDownPyramidAlignedRight or printCommand == _optionToPrintAllPyramidTypes:
        pyramidLines = generateSequenceLines(sequence, numberOfLines, stepWidth, True, False, False)

        for lineIndex in range(numberOfLines):
            rightPyramidLine = pyramidLines[lineIndex].rjust(stepWidth * numberOfLines)
            print(rightPyramidLine)

    # Upside Down Pyramid
    if printCommand == _optionToPrintFullUpsideDownPyramid or printCommand == _optionToPrintAllPyramidTypes:
        pyramidLines = generateSequenceLines(sequence, numberOfLines, stepWidth, True, True, False)

        for lineIndex in range(numberOfLines):
            pyramidLeftSegment = pyramidLines[lineIndex][0].rjust(stepWidth * numberOfLines)
            pyramidRightSegment = pyramidLines[lineIndex][1].ljust(stepWidth * numberOfLines)
            print(pyramidLeftSegment + pyramidRightSegment)

    # Silhouette Pyramid (Upside Down)
    if printCommand == _optionToPrintFullUpsideDownSilhouettePyramid or printCommand == _optionToPrintAllPyramidTypes:
        pyramidLines = generateSequenceLines(sequence, numberOfLines, stepWidth, True, False, True)

        for lineIndex in range(numberOfLines):
            pyramidLeftSegment = pyramidLines[lineIndex][0].ljust(stepWidth * numberOfLines)
            pyramidRightSegment = pyramidLines[lineIndex][1].rjust(stepWidth * numberOfLines)
            print(pyramidLeftSegment + pyramidRightSegment)


def printSequencePyramids(sequenceName):
    sequence = generateSequence(sequenceName)

    while True:
        print("Pyramid: " + _fullNamesOfSequences[sequenceName])
        printCommand = selectPrintPyramidCommand()

        if printCommand == _optionToGoBackToPreviousMenu:
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
