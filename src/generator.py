"""

    DespyNumPyramidGenerator - Generator

    Script to generate sequences and famous triangles

    Start Date: March 17, 2021
    End Date:

    File Name: sequences.py

"""

_maxNumberOfCharactersToPrint = 12880

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