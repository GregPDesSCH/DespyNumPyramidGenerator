"""

    DespyNumPyramidGenerator - Main Script

    Starting point for this program.

    Start Date: January 24, 2021
    End Date:

    File Name: main.py

"""

def numberIsAWholeNumber(rawNumber):
    try:
        int(rawNumber)
        return True
    except ValueError:
        return False

def getNumberOfLinesFromUser():
    rawNumberOfLines = ""
    numberOfLines = 0

    while len(rawNumberOfLines) == 0 or numberOfLines < 3 or numberOfLines > 80 or not numberIsAWholeNumber(rawNumberOfLines):
        rawNumberOfLines = input("Number of lines to print out for pyramids? ")
        if len(rawNumberOfLines) == 0:
            print("ERROR - Input must not be empty.")
        elif not numberIsAWholeNumber(rawNumberOfLines):
            print("ERROR - Input must be a whole positive number.")
        else:
            numberOfLines = int(rawNumberOfLines)
            if numberOfLines < 3 or numberOfLines > 80:
                print("ERROR - Number of lines must be in the range [3-80].")
        
    return numberOfLines

def getCharacterToPrint():
    characterToPrint = ""
    while len(characterToPrint) != 1:
        characterToPrint = input('Character to print pyramids? ')
        if len(characterToPrint) == 0:
            print("ERROR - Input must not be empty.")
        elif len(characterToPrint) > 1:
            print("ERROR - Input must be exactly one character long.")

    return characterToPrint

def main():
    numberOfLines = getNumberOfLinesFromUser()
    characterToPrint = getCharacterToPrint()

    # Left Pyramid
    for lineIndex in range(numberOfLines):
        print("".ljust(lineIndex + 1, characterToPrint).ljust(numberOfLines))

    # Right Pyramid
    for lineIndex in range(numberOfLines):
        print("".ljust(lineIndex + 1, characterToPrint).rjust(numberOfLines))

    # Full Pyramid
    for lineIndex in range(numberOfLines):
        print("".ljust(lineIndex + 1, characterToPrint).rjust(numberOfLines) + "".rjust(lineIndex + 1, characterToPrint).ljust(numberOfLines))

    # Upside Down Left Pyramid
    for lineIndex in range(numberOfLines):
        print("".ljust(numberOfLines - (lineIndex), characterToPrint).ljust(numberOfLines))

    # Upside Down Right Pyramid
    for lineIndex in range(numberOfLines):
        print("".rjust(numberOfLines - (lineIndex), characterToPrint).rjust(numberOfLines))

    # Upside Down Pyramid
    for lineIndex in range(numberOfLines):
        print("".ljust(numberOfLines - (lineIndex), characterToPrint).ljust(numberOfLines) + \
            "".rjust(numberOfLines - (lineIndex), characterToPrint).rjust(numberOfLines))

if __name__ == "__main__":
    main()
