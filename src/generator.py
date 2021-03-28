"""

    DespyNumPyramidGenerator - Generator

    Script to generate sequences and famous triangles

    Start Date: March 17, 2021
    End Date:

    File Name: sequences.py

"""

import math

_maxNumberOfCharactersToPrint = 12880
_maxNumberOfCharactersInOneLine = 160

def _generateFibonacciSequence():
    a = 0
    b = 1
    currentValue = 1
    totalCharactersInNewSequence = 2
    sequenceElements = ["0", "1"]

    while totalCharactersInNewSequence <= _maxNumberOfCharactersToPrint:
        currentSequenceMember = str(currentValue)
        sequenceElements.append(currentSequenceMember)
        totalCharactersInNewSequence += len(currentSequenceMember)

        a = b
        b = currentValue
        currentValue = a + b

    return sequenceElements

def _generateTriangleSequence():
    sequenceElements = []
    total = 1
    currentAddend = 2
    totalCharactersInNewSequence = 0

    while totalCharactersInNewSequence <= _maxNumberOfCharactersToPrint:
        currentSequenceMember = str(total)
        sequenceElements.append(currentSequenceMember)
        totalCharactersInNewSequence += len(currentSequenceMember)

        total += currentAddend
        currentAddend += 1

    return sequenceElements

def _generateAlternatingBitsSequence():
    sequenceElements = []
    currentValue = 0
    totalCharactersInNewSequence = 0

    while totalCharactersInNewSequence <= _maxNumberOfCharactersToPrint:
        currentSequenceMember = str(currentValue)
        sequenceElements.append(currentSequenceMember)
        totalCharactersInNewSequence += len(currentSequenceMember)

        currentValue = 1 if currentValue == 0 else 0

    return sequenceElements
    

def generateSequence(sequenceName):
    sequenceElements = []

    if sequenceName == "fibonacci":
        sequenceElements = _generateFibonacciSequence()
    elif sequenceName == "triangle":
        sequenceElements = _generateTriangleSequence()
    elif sequenceName == "alternatingBits":
        sequenceElements = _generateAlternatingBitsSequence()

    newSequence = "".join(sequenceElements)

    return newSequence

def _generatePascalTriangle():
    newNumberTriangle = [[1], [1, 1]]
    latestTriangleRowIndex = 1
    
    while True:
        newTriangleRow = [1]
        currentCharactersInNewRow = 2
        newTriangleColIndex = 1

        while newTriangleColIndex < len(newNumberTriangle[latestTriangleRowIndex]):
            newValue = newNumberTriangle[latestTriangleRowIndex][newTriangleColIndex - 1] + \
                newNumberTriangle[latestTriangleRowIndex][newTriangleColIndex]

            currentCharactersInNewRow += int(math.log10(newValue)) + 2

            newTriangleRow.append(newValue)
            newTriangleColIndex += 1

        latestTriangleRowIndex += 1
        newTriangleRow.append(1)
        currentCharactersInNewRow += 1

        if currentCharactersInNewRow > _maxNumberOfCharactersInOneLine:
            break

        newNumberTriangle.append(newTriangleRow)
    
    return newNumberTriangle

def _generateEulerTriangle():
    newNumberTriangle = [[1], [1, 1]]
    triangleRowIndex = 2

    while True:
        newTriangleRow = [1]
        currentCharactersInNewRow = 2
        newTriangleColIndex = 2

        while newTriangleColIndex < len(newNumberTriangle[triangleRowIndex - 1]) + 1:
            newValue = newTriangleColIndex * newNumberTriangle[triangleRowIndex - 1][newTriangleColIndex - 1] + \
                (triangleRowIndex + 2 - newTriangleColIndex) * \
                newNumberTriangle[triangleRowIndex - 1][newTriangleColIndex - 2]

            currentCharactersInNewRow += int(math.log10(newValue)) + 2

            newTriangleRow.append(newValue)
            newTriangleColIndex += 1

        triangleRowIndex += 1
        newTriangleRow.append(1)
        currentCharactersInNewRow += 1

        if currentCharactersInNewRow > _maxNumberOfCharactersInOneLine:
            break

        newNumberTriangle.append(newTriangleRow)

    return newNumberTriangle

def _generateCatalanTriangle():
    newNumberTriangle = []
    triangleRowIndex = 0
    triangleColIndex = 0

    while True:
        newTriangleRow = []
        currentCharactersInNewRow = 0
        triangleColIndex = 0

        while triangleColIndex <= triangleRowIndex:
            newValue = int(math.factorial(triangleRowIndex + triangleColIndex) * (triangleRowIndex - triangleColIndex + 1) / \
                (math.factorial(triangleColIndex) * math.factorial(triangleRowIndex + 1)))

            currentCharactersInNewRow += int(math.log10(newValue)) + 2

            newTriangleRow.append(newValue)
            triangleColIndex += 1

        triangleRowIndex += 1

        if currentCharactersInNewRow > _maxNumberOfCharactersInOneLine:
            break
        newNumberTriangle.append(newTriangleRow)

    return newNumberTriangle


def generateNumberTriangle(numberTriangleName):
    newNumberTriangle = []

    if numberTriangleName == "pascal":
        newNumberTriangle = _generatePascalTriangle()
    elif numberTriangleName == "euler":
        newNumberTriangle = _generateEulerTriangle()
    elif numberTriangleName == "catalan":
        newNumberTriangle = _generateCatalanTriangle()
            
    return newNumberTriangle

# For testing only
if __name__ == "__main__":
    # print("Generating Pascal's Triangle")
    # triangle = generateNumberTriangle("pascal")
    # print("Generating Euler's Triangle")
    # triangle = generateNumberTriangle("euler")
    print("Generating Catalan's Triangle")
    triangle = generateNumberTriangle("catalan")
    print("Generated Triangle:")
    print(triangle)
    for row in triangle:
        print(row)
    print("End")