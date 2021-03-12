"""

    DespyNumPyramidGenerator - Sequences

    Script to generate different sequences

    Start Date: March 6, 2021
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

    newSequence[0].append("".join(newSequence[1]))

    return newSequence

# For testing only
if __name__ == "__main__":
    print("Generating triangle sequence")
    sequence = generateSequence("triangle")
    print(sequence)
