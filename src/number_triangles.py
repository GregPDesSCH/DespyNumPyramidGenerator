"""

    DespyNumPyramidGenerator - Sequences

    Script responsible for printing number triangles

    Start Date: March 18, 2021
    End Date:

    File Name: number_triangles.py

"""

from generator import generateNumberTriangle
from inputs import selectPrintPyramidCommand, getNumberOfLinesFromUser, inputIsGoBackCommand

# Number triangle name dictionary
_FULL_NAMES_OF_NUMBER_TRIANGLES = {
    "pascal": "Pascal's Triangle",
    "euler": "Euler's Triangle",
    "catalan": "Catalan's Triangle"
}

# Constants for alignment mode options
_TRIANGLE_LEFT_ALIGN_MODE = "LEFT"
_TRIANGLE_RIGHT_ALIGN_MODE = "RIGHT"
_TRIANGLE_CENTER_ALIGN_MODE = "CENTER"

# Constants for different pyramid orientation options
_OPTION_TO_PRINT_UPSIDE_PYRAMID_ALIGNED_LEFT = 1
_OPTION_TO_PRINT_UPSIDE_PYRAMID_ALIGNED_RIGHT = 2
_OPTION_TO_PRINT_FULL_UPSIDE_PYRAMID = 3
_OPTION_TO_PRINT_UPSIDE_DOWN_PYRAMID_ALIGNED_LEFT = 4
_OPTION_TO_PRINT_UPSIDE_DOWN_PYRAMID_ALIGNED_RIGHT = 5
_OPTION_TO_PRINT_FULL_UPSIDE_DOWN_PYRAMID = 6
_OPTION_TO_PRINT_ALL_PYRAMID_TYPES = 7
_OPTION_TO_GO_BACK_TO_PREVIOUS_MENU = 8


def generateNumberTriangleLines(numberTriangle):
    """Generate the lines that when printed will give the number triangle appearance."""
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
    """Prints the pyramid out to the console with the specified options."""

    setOfLineNumbers = range(numberOfLines) if not printInReverse else range(numberOfLines - 1, -1, -1)
    maximumLineLength = len(triangleLines[numberOfLines - 1])

    for lineIndex in setOfLineNumbers:
        pyramidSegment = ""

        if alignMode == _TRIANGLE_LEFT_ALIGN_MODE:
            pyramidSegment = triangleLines[lineIndex].ljust(maximumLineLength)
        elif alignMode == _TRIANGLE_RIGHT_ALIGN_MODE:
            pyramidSegment = triangleLines[lineIndex].rjust(maximumLineLength)
        else:
            pyramidSegment = triangleLines[lineIndex].center(maximumLineLength)

        print(pyramidSegment)

    print()


def printDesiredPyramid(printCommand, triangleLines, numberOfLines):
    """Calls a helper function to print the pyramid with the desired options."""
    if printCommand == _OPTION_TO_PRINT_UPSIDE_PYRAMID_ALIGNED_LEFT or printCommand == _OPTION_TO_PRINT_ALL_PYRAMID_TYPES:
        printPyramid(triangleLines, numberOfLines, _TRIANGLE_LEFT_ALIGN_MODE, False) # Prints a left pyramid

    if printCommand == _OPTION_TO_PRINT_UPSIDE_PYRAMID_ALIGNED_RIGHT or printCommand == _OPTION_TO_PRINT_ALL_PYRAMID_TYPES:
        printPyramid(triangleLines, numberOfLines, _TRIANGLE_RIGHT_ALIGN_MODE, False) # Prints a right pyramid

    if printCommand == _OPTION_TO_PRINT_FULL_UPSIDE_PYRAMID or printCommand == _OPTION_TO_PRINT_ALL_PYRAMID_TYPES:
        printPyramid(triangleLines, numberOfLines, _TRIANGLE_CENTER_ALIGN_MODE, False) # Prints a full pyramid

    if printCommand == _OPTION_TO_PRINT_UPSIDE_DOWN_PYRAMID_ALIGNED_LEFT or printCommand == _OPTION_TO_PRINT_ALL_PYRAMID_TYPES:
        printPyramid(triangleLines, numberOfLines, _TRIANGLE_LEFT_ALIGN_MODE, True) # Prints an upside-down left pyramid

    if printCommand == _OPTION_TO_PRINT_UPSIDE_DOWN_PYRAMID_ALIGNED_RIGHT or printCommand == _OPTION_TO_PRINT_ALL_PYRAMID_TYPES:
        printPyramid(triangleLines, numberOfLines, _TRIANGLE_RIGHT_ALIGN_MODE, True) # Prints an upside-down right pyramid

    if printCommand == _OPTION_TO_PRINT_FULL_UPSIDE_DOWN_PYRAMID or printCommand == _OPTION_TO_PRINT_ALL_PYRAMID_TYPES:
        printPyramid(triangleLines, numberOfLines, _TRIANGLE_CENTER_ALIGN_MODE, True) # Prints an upside-down full pyramid


def printNumberTrianglePyramids(numberTriangleName):
    """Loop for interacting with pyramids of famous number triangles"""
    triangle = generateNumberTriangle(numberTriangleName)
    triangleLines = generateNumberTriangleLines(triangle)

    while True:
        print("Pyramid: " + _FULL_NAMES_OF_NUMBER_TRIANGLES[numberTriangleName])
        printCommand = selectPrintPyramidCommand(8, True)

        if printCommand == _OPTION_TO_GO_BACK_TO_PREVIOUS_MENU:
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