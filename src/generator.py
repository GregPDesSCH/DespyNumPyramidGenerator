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

def generateSequence(sequenceName):
    newSequence = []
    currentSequenceMember = ""
    if sequenceName == "fibonacci":
        a = 0
        b = 1
        currentValue = 1
        totalCharactersInNewSequence = 2
        newSequence = [[], ["0", "1"]]
        while totalCharactersInNewSequence <= _maxNumberOfCharactersToPrint:
            currentSequenceMember = str(currentValue)
            newSequence[1].append(currentSequenceMember)
            totalCharactersInNewSequence += len(currentSequenceMember)

            a = b
            b = currentValue
            currentValue = a + b

    elif sequenceName == "triangle":
        total = 1
        currentAddend = 2
        totalCharactersInNewSequence = 0
        newSequence = [[], []]

        while totalCharactersInNewSequence <= _maxNumberOfCharactersToPrint:
            currentSequenceMember = str(total)
            newSequence[1].append(currentSequenceMember)
            totalCharactersInNewSequence += len(currentSequenceMember)

            total += currentAddend
            currentAddend += 1

    elif sequenceName == "alternatingBits":
        currentValue = 0
        totalCharactersInNewSequence = 0
        newSequence = [[], []]

        while totalCharactersInNewSequence <= _maxNumberOfCharactersToPrint:
            currentSequenceMember = str(currentValue)
            newSequence[1].append(currentSequenceMember)
            totalCharactersInNewSequence += len(currentSequenceMember)

            currentValue = 1 if currentValue == 0 else 0

    newSequence[0].append("".join(newSequence[1]))

    return newSequence

def generateNumberTriangle(numberTriangleName):
    newNumberTriangle = []

    if numberTriangleName == "pascal":
        newNumberTriangle = [[1], [1, 1]]
        currentCharactersInNewRow = 0
        latestTriangleRowIndex = 1
        
        while True:
            newTriangleRow = [1]
            currentCharactersInNewRow = 2

            newTriangleRowIndex = 1

            while newTriangleRowIndex < len(newNumberTriangle[latestTriangleRowIndex]):
                newValue = newNumberTriangle[latestTriangleRowIndex][newTriangleRowIndex - 1] + \
                    newNumberTriangle[latestTriangleRowIndex][newTriangleRowIndex]

                currentCharactersInNewRow += int(math.log10(newValue)) + 2

                newTriangleRow.append(newValue)
                newTriangleRowIndex += 1

            latestTriangleRowIndex += 1
            newTriangleRow.append(1)
            currentCharactersInNewRow += 1

            if currentCharactersInNewRow > _maxNumberOfCharactersInOneLine:
                break

            newNumberTriangle.append(newTriangleRow)
        
    return newNumberTriangle

# For testing only
if __name__ == "__main__":
    print("Generating Pascal's Triangle")
    triangle = generateNumberTriangle("pascal")
    print("Generated Triangle:")
    print(triangle)
    for row in triangle:
        print(row)
    print("End")