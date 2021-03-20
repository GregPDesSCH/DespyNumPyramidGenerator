"""

    DespyNumPyramidGenerator - Sequences

    Script responsible for printing number triangles

    Start Date: March 18, 2021
    End Date:

    File Name: number_triangles.py

"""

from generator import generateNumberTriangle
from inputs import selectPrintPyramidCommand, getNumberOfLinesFromUser

def generateNumberTriangleLines(numberTriangle, numberOfLines, pyramidIsUpsideDown):
    numberTriangleLines = []

    startingIndex = 0 if pyramidIsUpsideDown == False else numberOfLines - 1
    endingIndex = numberOfLines if pyramidIsUpsideDown == False else - 1
    loopStep = -1 if pyramidIsUpsideDown == True else 1
    
    for lineIndex in range(startingIndex, endingIndex, loopStep):
        currentLine = ""
        for index, elem in enumerate(numberTriangle[lineIndex]):
            currentLine += str(elem)
            if index < len(numberTriangle[lineIndex]) - 1:
                currentLine += " "
        numberTriangleLines.append(currentLine)

    return numberTriangleLines

def printPyramid(printCommand, numberTriangle, numberOfLines):
    if numberOfLines > len(numberTriangle):
        print(f"This number triangle only has {len(numberTriangle)} lines. Please use a smaller number of lines.")
    else:
        maximumLineLength = 0
        if printCommand < 4 or printCommand == 7:
            triangleLines = generateNumberTriangleLines(numberTriangle, numberOfLines, False)
            maximumLineLength = len(triangleLines[len(triangleLines) - 1])

        if printCommand == 1 or printCommand == 7:
            # Left Pyramid
            for lineIndex in range(numberOfLines):
                print(triangleLines[lineIndex].ljust(maximumLineLength))

        if printCommand == 2 or printCommand == 7:
            # Right Pyramid
            for lineIndex in range(numberOfLines):
                print(triangleLines[lineIndex].rjust(maximumLineLength))

        if printCommand == 3 or printCommand == 7:
            # Full Pyramid
            for lineIndex in range(numberOfLines):
                print(triangleLines[lineIndex].center(maximumLineLength))

        if printCommand > 3 or printCommand == 7:
            triangleLines = generateNumberTriangleLines(numberTriangle, numberOfLines, True)
            maximumLineLength = len(triangleLines[0])

        if printCommand == 4 or printCommand == 7:
            # Upside Down Left Pyramid
            for lineIndex in range(numberOfLines):
                print(triangleLines[lineIndex].ljust(maximumLineLength))

        if printCommand == 5 or printCommand == 7:
            # Upside Down Right Pyramid
            for lineIndex in range(numberOfLines):
                print(triangleLines[lineIndex].rjust(maximumLineLength))

        if printCommand == 6 or printCommand == 7:
            # Upside Down Full Pyramid
            for lineIndex in range(numberOfLines):
                print(triangleLines[lineIndex].center(maximumLineLength))

def printNumberTrianglePyramids(numberTriangleName):
    triangle = generateNumberTriangle(numberTriangleName)

    while True:
        printCommand = selectPrintPyramidCommand(8, True)

        if printCommand == 8:
            break

        numberOfLines = getNumberOfLinesFromUser(len(triangle))

        printPyramid(printCommand, triangle, numberOfLines)

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

    printPyramid(printCommand, triangle, numberOfLines)