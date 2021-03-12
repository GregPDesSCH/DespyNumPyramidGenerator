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
    if sequenceName == "fibonacci":
        a = 0
        b = 1
        currentValue = 1
        totalCharactersInNewSequence = 2
        currentSequenceMember = ""
        newSequence = [[], ["0", "1"]]
        while totalCharactersInNewSequence <= _maxNumberOfCharactersToPrint:
            currentSequenceMember = str(currentValue)
            newSequence[1].append(currentSequenceMember)
            totalCharactersInNewSequence += len(currentSequenceMember)

            a = b
            b = currentValue
            currentValue = a + b

        newSequence[0].append("".join(newSequence[1]))

    return newSequence

# For testing only
if __name__ == "__main__":
    print("Generating Fibonacci sequence")
    sequence = generateSequence("fibonacci")
    print(sequence)
