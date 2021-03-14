"""

    DespyNumPyramidGenerator - Sequences

    Script to generate different sequences

    Start Date: March 6, 2021
    End Date:

    File Name: sequences.py

"""

_maxNumberOfCharactersToPrint = 12880

#TODO: Move the generate sequence code to a new module called sequence generator.

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


def createLineSegment(sequence, maxLineSegmentLength, sequenceStringIndex):
    currentLineSegment = ""
    for _ in range(maxLineSegmentLength):
        currentLineSegment += sequence[0][0][sequenceStringIndex[0]]
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
            sequenceLines.append(createLineSegment(sequence, maxLineSegmentLength, sequenceStringIndex))
    else:
        for lineNumber in range(numberOfLines):
            currentLine = []
            
            if pyramidIsSilhouette == True and pyramidIsUpsideDown == False or pyramidIsSilhouette == False \
                    and pyramidIsUpsideDown == True:
                maxLineSegmentLength = numberOfLines - lineNumber * stepWidth
            else:
                maxLineSegmentLength = (lineNumber + 1) * stepWidth

            currentLine.append(createLineSegment(sequence, maxLineSegmentLength, sequenceStringIndex))
            currentLine.append(createLineSegment(sequence, maxLineSegmentLength, sequenceStringIndex))
            sequenceLines.append(currentLine)


    return sequenceLines

# For testing only
if __name__ == "__main__":
    print("Generating alternatingBits sequence")
    sequence = generateSequence("alternatingBits")
    print(generateSequenceLines(sequence, 10, 1, False, False, False))
    print(generateSequenceLines(sequence, 10, 1, False, True, False))
    print(generateSequenceLines(sequence, 10, 1, False, False, True))
    print(generateSequenceLines(sequence, 10, 1, True, False, False))
    print(generateSequenceLines(sequence, 10, 1, True, True, False))
    print(generateSequenceLines(sequence, 10, 1, True, False, True))
