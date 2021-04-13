"""

    DespyNumPyramidGenerator - Generator

    Script to generate sequences and famous triangles

    Start Date: March 17, 2021
    End Date:

    File Name: sequences.py

"""

import math

# Max number of characters a sequence can have
# (based on a full pyramid with 80 lines and step width of 1)
_MAX_NUMBER_OF_CHARACTERS_TO_PRINT = 12880

# Max characters to print in one line
_MAX_NUMBER_OF_CHARACTERS_IN_ONE_LINE = 160


def _generateFibonacciSequence():
    """
    Generates a list of elements following the Fibonacci sequence.

    Returns:
    sequenceElements - List of elements following the sequence.
    """
    sequenceElements = ["0", "1"]
    totalCharactersInNewSequence = 2

    secondPreviousValue = 0
    firstPreviousValue = 1
    currentValue = 1

    while totalCharactersInNewSequence <= _MAX_NUMBER_OF_CHARACTERS_TO_PRINT:
        currentSequenceMember = str(currentValue)
        sequenceElements.append(currentSequenceMember)

        totalCharactersInNewSequence += len(currentSequenceMember)

        secondPreviousValue = firstPreviousValue
        firstPreviousValue = currentValue
        currentValue = secondPreviousValue + firstPreviousValue

    return sequenceElements

def _generateTriangleSequence():
    """
    Generates list of elements following sequence of triangle numbers.

    Returns:
    sequenceElements - List of elements following the sequence.
    """
    sequenceElements = []
    totalCharactersInNewSequence = 0

    total = 1
    currentAddend = 2

    while totalCharactersInNewSequence <= _MAX_NUMBER_OF_CHARACTERS_TO_PRINT:
        currentSequenceMember = str(total)
        sequenceElements.append(currentSequenceMember)

        totalCharactersInNewSequence += len(currentSequenceMember)

        total += currentAddend
        currentAddend += 1

    return sequenceElements

def _generateAlternatingBitsSequence():
    """
    Generates list of elements following sequence of alternating binary 
    numbers.

    Returns:
    sequenceElements - List of elements following the sequence.
    """
    sequenceElements = []
    totalCharactersInNewSequence = 0
    
    currentValue = 0

    while totalCharactersInNewSequence <= _MAX_NUMBER_OF_CHARACTERS_TO_PRINT:
        currentSequenceMember = str(currentValue)
        sequenceElements.append(currentSequenceMember)

        totalCharactersInNewSequence += len(currentSequenceMember)

        currentValue = 1 if currentValue == 0 else 0

    return sequenceElements

def _generateSequenceOfSquares():
    """
    Generates list of elements following sequence of squares.

    Returns:
    sequenceElements - List of elements following the sequence.
    """
    sequenceElements = []
    totalCharactersInNewSequence = 0
    
    currentValue = 0
    currentBase = 1

    while totalCharactersInNewSequence <= _MAX_NUMBER_OF_CHARACTERS_TO_PRINT:
        currentValue = currentBase * currentBase
        currentSequenceMember = str(currentValue)
        sequenceElements.append(currentSequenceMember)

        totalCharactersInNewSequence += len(currentSequenceMember)

        currentBase += 1

    return sequenceElements
    

def generateSequence(sequenceName):
    """
    Delegates the sequence generation to the appropriate function.
    
    Params:
    sequenceName - Name of sequence to build the list of elements out of.

    Returns:
    newSequence - Full string representing the sequence.
    """
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
    """
    Generates a 2D list representing Pascal's Triangle.

    Returns:
    newNumberTriangle - 2D list with elements representing the number triangle.
    """
    newNumberTriangle = [[1], [1, 1]]
    latestTriangleRowIndex = 1
    
    while True:
        newTriangleRow = [1]
        currentCharactersInNewRow = 2
        newTriangleColIndex = 1

        while newTriangleColIndex < len(
                newNumberTriangle[latestTriangleRowIndex]):
            newBinomialCoefficient = \
                    newNumberTriangle[latestTriangleRowIndex][newTriangleColIndex - 1] \
                    + newNumberTriangle[latestTriangleRowIndex][newTriangleColIndex]

            currentCharactersInNewRow += \
                    int(math.log10(newBinomialCoefficient)) + 2

            newTriangleRow.append(newBinomialCoefficient)
            newTriangleColIndex += 1

        latestTriangleRowIndex += 1
        newTriangleRow.append(1)
        currentCharactersInNewRow += 1

        if currentCharactersInNewRow > _MAX_NUMBER_OF_CHARACTERS_IN_ONE_LINE:
            break

        newNumberTriangle.append(newTriangleRow)
    
    return newNumberTriangle

def _generateEulerTriangle():
    """
    Generates a 2D list representing Euler's Triangle.

    Returns:
    newNumberTriangle - 2D list with elements representing the number triangle.
    """
    newNumberTriangle = [[1], [1, 1]]
    triangleRowIndex = 2

    while True:
        newTriangleRow = [1]
        currentCharactersInNewRow = 2
        newTriangleColIndex = 2

        while newTriangleColIndex < len(
                    newNumberTriangle[triangleRowIndex - 1]) + 1:
            firstShiftedEulerianNumber = newTriangleColIndex \
                    * newNumberTriangle[triangleRowIndex - 1][
                    newTriangleColIndex - 1]
            secondShiftedEulerianNumber = (triangleRowIndex + 2 - 
                    newTriangleColIndex) \
                    * newNumberTriangle[triangleRowIndex - 1][
                    newTriangleColIndex - 2]

            newEulerianNumber = firstShiftedEulerianNumber \
                + secondShiftedEulerianNumber

            currentCharactersInNewRow += \
                int(math.log10(newEulerianNumber)) + 2

            newTriangleRow.append(newEulerianNumber)
            newTriangleColIndex += 1

        triangleRowIndex += 1
        newTriangleRow.append(1)
        currentCharactersInNewRow += 1

        if currentCharactersInNewRow > _MAX_NUMBER_OF_CHARACTERS_IN_ONE_LINE:
            break

        newNumberTriangle.append(newTriangleRow)

    return newNumberTriangle

def _generateCatalanTriangle():
    """
    Generates a 2D list representing Catalan's Triangle.

    Returns:
    newNumberTriangle - 2D list with elements representing the number triangle.
    """
    newNumberTriangle = []
    triangleRowIndex = 0
    triangleColIndex = 0

    while True:
        newTriangleRow = []
        currentCharactersInNewRow = 0
        triangleColIndex = 0

        while triangleColIndex <= triangleRowIndex:
            newCoefficientNumerator = math.factorial(triangleRowIndex \
                    + triangleColIndex) * (triangleRowIndex - triangleColIndex \
                    + 1)
            newCoefficientDenominator = math.factorial(triangleColIndex) \
                    * math.factorial(triangleRowIndex + 1)

            newCoefficient = int(newCoefficientNumerator / \
                    newCoefficientDenominator)

            currentCharactersInNewRow += int(math.log10(newCoefficient)) + 2

            newTriangleRow.append(newCoefficient)
            triangleColIndex += 1

        triangleRowIndex += 1

        if currentCharactersInNewRow > _MAX_NUMBER_OF_CHARACTERS_IN_ONE_LINE:
            break
        newNumberTriangle.append(newTriangleRow)

    return newNumberTriangle


def generateNumberTriangle(numberTriangleName):
    """
    Delegates the number triangle generation to the appropriate function.
    
    Params:
    numberTriangleName - Name of the number triangle to build the 2D list
    of elements out of.

    Returns:
    newNumberTriangle - 2D list with elements representing the desired number
    triangle.
    """
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