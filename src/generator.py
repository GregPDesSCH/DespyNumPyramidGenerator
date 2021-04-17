"""

    DespyNumPyramidGenerator - Generator

    Script to generate sequences and number triangles.

    Initial Version
    Start Date: March 17, 2021
    End Date: April 17, 2021

    File Name: generator.py

"""

import math

# Max number of characters a sequence can have
# (based on a full pyramid with 80 lines and step width of 1)
_MAX_NUMBER_OF_CHARACTERS_TO_PRINT = 12880

# Max characters to print in one line
_MAX_NUMBER_OF_CHARACTERS_IN_ONE_LINE = 160

# Sequence name list
_LIST_OF_SEQUENCE_NAMES = [
    "fibonacci", "triangle", "alternatingBits", "squares", "powersOfTwos"
]

# Number triangle name list
_LIST_OF_NUMBER_TRIANGLE_NAMES = [
    "pascal", "euler", "catalan", "bernoulli", "seidelEntringerArnold"
]


def getListOfSequenceNames():
    """
    Gets a list of names for all the sequences to be used as arguments.

    Returns:
    _LIST_OF_SEQUENCE_NAMES - Sequence name list.
    """
    return _LIST_OF_SEQUENCE_NAMES

def getListOfNumberTriangleNames():
    """
    Gets a list of names for all the number triangles to be used as arguments.

    Returns:
    _LIST_OF_NUMBER_TRIANGLE_NAMES - Number triangle name list.
    """
    return _LIST_OF_NUMBER_TRIANGLE_NAMES

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

def _generateSequenceOfPowersOfTwos():
    """
    Generates list of elements following sequence of powers of twos.

    Returns:
    sequenceElements - List of elements following the sequence.
    """
    sequenceElements = []
    totalCharactersInNewSequence = 0

    currentValue = 1

    while totalCharactersInNewSequence <= _MAX_NUMBER_OF_CHARACTERS_TO_PRINT:
        currentSequenceMember = str(currentValue)
        sequenceElements.append(currentSequenceMember)

        totalCharactersInNewSequence += len(currentSequenceMember)
        
        currentValue *= 2

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
    elif sequenceName == "squares":
        sequenceElements = _generateSequenceOfSquares()
    elif sequenceName == "powersOfTwos":
        sequenceElements = _generateSequenceOfPowersOfTwos()

    newSequence = "".join(sequenceElements)

    return newSequence


def _generateBinomialTriangle(generateBernoulliTriangle = False):
    """
    Generates a 2D list representing a binomial triangle. Depending on the
    parameters, it either generates Pascal's Triangle, or the Bernoulli
    triangle.

    Params:
    generateBernoulliTriangle - Flag denoting whether to generate the Bernoulli
    triangle or not.

    Returns:
    newNumberTriangle - 2D list with elements representing the number triangle.
    """
    newNumberTriangle = [[1], [1, 1]]

    if generateBernoulliTriangle:
        newNumberTriangle[1][1] = 2

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

        if generateBernoulliTriangle:
            newTriangleRow.append(1 + newTriangleRow[newTriangleColIndex - 1])
        else:
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

def _generateSeidelEntringerArnoldTriangle():
    """
    Generates a 2D list representing the Seidel-Entringer-Arnold Triangle.

    Returns:
    newNumberTriangle - 2D list with elements representing the number triangle.
    """
    newNumberTriangle = [[0], [0, 1]]
    triangleRowIndex = 2
    triangleColIndex = 0

    while True:
        newTriangleRow = [0]
        currentCharactersInNewRow = 0
        triangleColIndex = 1

        while triangleColIndex <= triangleRowIndex:
            newValue = newTriangleRow[triangleColIndex - 1] \
                    + newNumberTriangle[triangleRowIndex \
                    - 1][triangleRowIndex - triangleColIndex]
            
            currentCharactersInNewRow += int(math.log10(newValue)) + 2
            newTriangleRow.append(newValue)
            triangleColIndex += 1

        triangleRowIndex += 1

        if currentCharactersInNewRow > _MAX_NUMBER_OF_CHARACTERS_IN_ONE_LINE:
            break
        newNumberTriangle.append(newTriangleRow)

    triangleRowIndex = 2
    while triangleRowIndex < len(newNumberTriangle):
        newNumberTriangle[triangleRowIndex] = \
                list(reversed(newNumberTriangle[triangleRowIndex]))
        triangleRowIndex += 2

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
        newNumberTriangle = _generateBinomialTriangle()
    elif numberTriangleName == "euler":
        newNumberTriangle = _generateEulerTriangle()
    elif numberTriangleName == "catalan":
        newNumberTriangle = _generateCatalanTriangle()
    elif numberTriangleName == "bernoulli":
        newNumberTriangle = _generateBinomialTriangle( 
                generateBernoulliTriangle = True)
    elif numberTriangleName == "seidelEntringerArnold":
        newNumberTriangle = _generateSeidelEntringerArnoldTriangle()
            
    return newNumberTriangle


# For testing only
if __name__ == "__main__":
    # print("Generating Pascal's Triangle")
    # triangle = generateNumberTriangle("pascal")
    # print("Generating Euler's Triangle")
    # triangle = generateNumberTriangle("euler")
    
    # print("Generating Catalan's Triangle")
    # triangle = generateNumberTriangle("bernoulli")
    # print("Generated Triangle:")
    # print(triangle)
    # for row in triangle:
    #     print(row)
    # print("End")

    # print("Generating sequence of powers of twos")
    # fullSequence = generateSequence("powersOfTwos")
    # print(fullSequence)

    # sequence = _generateSequenceOfPowersOfTwos()
    # print(sequence)

    sequence = _generateSeidelEntringerArnoldTriangle()
    print(sequence)