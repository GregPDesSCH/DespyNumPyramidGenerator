"""

    DespyNumPyramidGenerator - Sequences

    Script to generate different sequences

    Start Date: March 6, 2021
    End Date:

    File Name: main.py

"""

_maxNumberOfCharactersToPrint = 12880

def generateSequence(sequenceName):
    newSequence = []
    if sequenceName == "fibonacci":
        a = 1
        b = 1
        currentValue = 2
        totalCharactersInNewSequence = 2
        currentSequenceMember = ""
        newSequence = ["1", "1"]
        while totalCharactersInNewSequence <= _maxNumberOfCharactersToPrint:
            currentSequenceMember = str(currentValue)
            newSequence.append(currentSequenceMember)
            totalCharactersInNewSequence += len(currentSequenceMember)

            a = b
            b = currentValue
            currentValue = a + b

    return newSequence

# For testing only
if __name__ == "__main__":
    print("Generating Fibonacci sequence")
    sequence = generateSequence("fibonacci")
    print(sequence)
