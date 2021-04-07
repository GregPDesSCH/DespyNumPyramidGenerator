"""

    DespyNumPyramidGenerator - Sequences

    Script responsible for printing number triangles

    Start Date: March 18, 2021
    End Date:

    File Name: number_triangles.py

"""

from generator import generateNumberTriangle
from inputs import selectPrintPyramidCommand, getNumberOfLinesFromUser, inputIsGoBackCommand


_fullNamesOfNumberTriangles = {
    "pascal": "Pascal's Triangle",
    "euler": "Euler's Triangle",
    "catalan": "Catalan's Triangle"
}

_triangleLeftAlignMode = "LEFT"
_triangleRightAlignMode = "RIGHT"
_triangleCenterAlignMode = "CENTER"

_optionToPrintUpsidePyramidAlignedLeft = 1
_optionToPrintUpsidePyramidAlignedRight = 2
_optionToPrintFullUpsidePyramid = 3
_optionToPrintUpsideDownPyramidAlignedLeft = 4
_optionToPrintUpsideDownPyramidAlignedRight = 5
_optionToPrintFullUpsideDownPyramid = 6
_optionToPrintAllPyramidTypes = 7
_optionToGoBackToPreviousMenu = 8


def generateNumberTriangleLines(numberTriangle):
    numberTriangleLines = []
    
    for lineIndex in range(len(numberTriangle)):
        currentLine = ""

        for index, elem in enumerate(numberTriangle[lineIndex]):
            currentLine += str(elem)
            if index < len(numberTriangle[lineIndex]) - 1:
                currentLine += " "
        
        numberTriangleLines.append(currentLine)

    return numberTriangleLines


def printPyramid(triangleLines, numberOfLines, alignMode, printInReverse):
    setOfLineNumbers = range(numberOfLines) if printInReverse == False else range(numberOfLines - 1, -1, -1)
    maximumLineLength = len(triangleLines[numberOfLines - 1])

    for lineIndex in setOfLineNumbers:
        pyramidSegment = ""

        if alignMode == _triangleLeftAlignMode:
            pyramidSegment = triangleLines[lineIndex].ljust(maximumLineLength)
        elif alignMode == _triangleRightAlignMode:
            pyramidSegment = triangleLines[lineIndex].rjust(maximumLineLength)
        else:
            pyramidSegment = triangleLines[lineIndex].center(maximumLineLength)

        print(pyramidSegment)

    print()


def printDesiredPyramid(printCommand, triangleLines, numberOfLines):
    if printCommand == _optionToPrintUpsidePyramidAlignedLeft or printCommand == _optionToPrintAllPyramidTypes:
        printPyramid(triangleLines, numberOfLines, _triangleLeftAlignMode, False) # Prints a left pyramid

    if printCommand == _optionToPrintUpsidePyramidAlignedRight or printCommand == _optionToPrintAllPyramidTypes:
        printPyramid(triangleLines, numberOfLines, _triangleRightAlignMode, False) # Prints a right pyramid

    if printCommand == _optionToPrintFullUpsidePyramid or printCommand == _optionToPrintAllPyramidTypes:
        printPyramid(triangleLines, numberOfLines, _triangleCenterAlignMode, False) # Prints a full pyramid

    if printCommand == _optionToPrintUpsideDownPyramidAlignedLeft or printCommand == _optionToPrintAllPyramidTypes:
        printPyramid(triangleLines, numberOfLines, _triangleLeftAlignMode, True) # Prints an upside-down left pyramid

    if printCommand == _optionToPrintUpsideDownPyramidAlignedRight or printCommand == _optionToPrintAllPyramidTypes:
        printPyramid(triangleLines, numberOfLines, _triangleRightAlignMode, True) # Prints an upside-down right pyramid

    if printCommand == _optionToPrintFullUpsideDownPyramid or printCommand == _optionToPrintAllPyramidTypes:
        printPyramid(triangleLines, numberOfLines, _triangleCenterAlignMode, True) # Prints an upside-down full pyramid


def printNumberTrianglePyramids(numberTriangleName):
    triangle = generateNumberTriangle(numberTriangleName)
    triangleLines = generateNumberTriangleLines(triangle)

    while True:
        print("Pyramid: " + _fullNamesOfNumberTriangles[numberTriangleName])
        printCommand = selectPrintPyramidCommand(8, True)

        if printCommand == _optionToGoBackToPreviousMenu:
            break

        numberOfLines = getNumberOfLinesFromUser(len(triangle))
        if inputIsGoBackCommand(numberOfLines):
            continue

        printDesiredPyramid(printCommand, triangleLines, numberOfLines)


# For testing only
if __name__ == "__main__":
    #print("Generating Pascal's Triangle")
    #triangle = generateNumberTriangle("pascal")
    #print("Creating lines of triangle")
    # triangleLines = generateNumberTriangleLines(triangle, 10, False)
    # print("Printing triangle")
    # for line in triangleLines:
    #     print(line)

    #printPyramidCommandMenu()

    # printPyramid(7, triangle, 20)
    # print("End")

    triangle = generateNumberTriangle("pascal")
    printCommand = selectPrintPyramidCommand(8, True)

    if printCommand == 8:
        exit()

    numberOfLines = getNumberOfLinesFromUser(len(triangle))

    printDesiredPyramid(printCommand, triangle, numberOfLines)

    # triangle = generateNumberTriangle("pascal")
    # triangleLines = generateNumberTriangleLines(triangle)
    # printDesiredPyramid(7, triangleLines, 15)