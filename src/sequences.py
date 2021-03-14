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


def printPyramid(printCommand, sequence, numberOfLines, stepWidth):
    if numberOfLines * stepWidth > 160:
        print("ERROR - Maximum number of characters to be printed on the screen is 160. Please enter again.")
    else:
        if printCommand == 1 or printCommand == 9:
            pyramidLines = generateSequenceLines(sequence, 10, 1, False, False, False)
            # Left Pyramid
            for lineIndex in range(numberOfLines):
                print(pyramidLines[lineIndex].ljust(stepWidth * (lineIndex + 1)).ljust(stepWidth * numberOfLines))

        if printCommand == 2 or printCommand == 9:
            pyramidLines = generateSequenceLines(sequence, 10, 1, False, False, False)
            # Right Pyramid
            for lineIndex in range(numberOfLines):
                print(pyramidLines[lineIndex].ljust(stepWidth * (lineIndex + 1)).rjust(stepWidth * numberOfLines))

        if printCommand == 3 or printCommand == 9:
            pyramidLines = generateSequenceLines(sequence, 10, 1, False, True, False)
            # Full Pyramid
            for lineIndex in range(numberOfLines):
                print(pyramidLines[lineIndex][0].rjust(stepWidth * numberOfLines) + \
                    pyramidLines[lineIndex][1].ljust(stepWidth * numberOfLines))

        if printCommand == 4 or printCommand == 9:
            pyramidLines = generateSequenceLines(sequence, 10, 1, False, False, True)
            # Silhouette Pyramid
            for lineIndex in range(numberOfLines):
                print(pyramidLines[lineIndex][0].ljust(stepWidth * numberOfLines) + \
                    pyramidLines[lineIndex][1].rjust(stepWidth * numberOfLines))

        if printCommand == 5 or printCommand == 9:
            pyramidLines = generateSequenceLines(sequence, 10, 1, True, False, False)
            # Upside Down Left Pyramid
            for lineIndex in range(numberOfLines):
                print(pyramidLines[lineIndex].ljust(stepWidth * numberOfLines))

        if printCommand == 6 or printCommand == 9:
            pyramidLines = generateSequenceLines(sequence, 10, 1, True, False, False)
            # Upside Down Right Pyramid
            for lineIndex in range(numberOfLines):
                print(pyramidLines[lineIndex].rjust(stepWidth * numberOfLines))

        if printCommand == 7 or printCommand == 9:
            pyramidLines = generateSequenceLines(sequence, 10, 1, True, True, False)
            # Upside Down Pyramid
            for lineIndex in range(numberOfLines):
                print(pyramidLines[lineIndex][0].rjust(stepWidth * numberOfLines) + \
                    pyramidLines[lineIndex][1].ljust(stepWidth * numberOfLines))

        if printCommand == 8 or printCommand == 9:
            pyramidLines = generateSequenceLines(sequence, 10, 1, True, False, True)
            # Silhouette Pyramid (Upside Down)
            for lineIndex in range(numberOfLines):
                print(pyramidLines[lineIndex][0].ljust(stepWidth * numberOfLines) + \
                    pyramidLines[lineIndex][1].rjust(stepWidth * numberOfLines))

# For testing only
if __name__ == "__main__":
    print("Generating alternatingBits sequence")
    sequence = generateSequence("alternatingBits")
    printPyramid(9, sequence, 10, 1)
