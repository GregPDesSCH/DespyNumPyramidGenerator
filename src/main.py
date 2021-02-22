"""

    DespyNumPyramidGenerator - Main Script

    Starting point for this program.

    Start Date: January 24, 2021
    End Date:

    File Name: main.py

"""

def printCommandMenu():
    print("Pick an option from one of the following:", "1 - Left Pyramid", "2 - Right Pyramid", "3 - Full Pyramid",
        "4 - Upside Down Left Pyramid", "5 - Upside Down Right Pyramid", "6 - Upside Down Pyrmaid (Mirrored)",
        "7 - All Options", "8 - Quit", sep="\n")

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


def selectPrintCommand():
    rawPrintCommand = ""
    printCommand = 0
    while len(rawPrintCommand) != 1 or printCommand < 1 or printCommand > 8 or not numberIsAWholeNumber(rawPrintCommand):
        printCommandMenu()
        rawPrintCommand = input('Select option [1-8]: ')
        if len(rawPrintCommand) == 0:
            print("ERROR - Input must not be empty.")
        elif not numberIsAWholeNumber(rawPrintCommand):
            print("ERROR - Input must be a whole positive number.")
        else:
            printCommand = int(rawPrintCommand)
            if printCommand < 1 or printCommand > 8:
                print("ERROR - Command must be in the range [1-8].")
    
    return printCommand

def main():
    while True:
        printCommand = selectPrintCommand()

        if printCommand == 8:
            break

        numberOfLines = getNumberOfLinesFromUser()
        characterToPrint = getCharacterToPrint()
        

        if printCommand == 1 or printCommand == 7:
            # Left Pyramid
            for lineIndex in range(numberOfLines):
                print("".ljust(lineIndex + 1, characterToPrint).ljust(numberOfLines))

        if printCommand == 2 or printCommand == 7:
            # Right Pyramid
            for lineIndex in range(numberOfLines):
                print("".ljust(lineIndex + 1, characterToPrint).rjust(numberOfLines))

        if printCommand == 3 or printCommand == 7:
            # Full Pyramid
            for lineIndex in range(numberOfLines):
                print("".ljust(lineIndex + 1, characterToPrint).rjust(numberOfLines) + \
                    "".rjust(lineIndex + 1, characterToPrint).ljust(numberOfLines))

        if printCommand == 4 or printCommand == 7:
            # Upside Down Left Pyramid
            for lineIndex in range(numberOfLines):
                print("".ljust(numberOfLines - (lineIndex), characterToPrint).ljust(numberOfLines))

        if printCommand == 5 or printCommand == 7:
            # Upside Down Right Pyramid
            for lineIndex in range(numberOfLines):
                print("".rjust(numberOfLines - (lineIndex), characterToPrint).rjust(numberOfLines))

        if printCommand == 6 or printCommand == 7:
            # Upside Down Pyramid (Mirrored)
            for lineIndex in range(numberOfLines):
                print("".ljust(numberOfLines - (lineIndex), characterToPrint).ljust(numberOfLines) + \
                    "".rjust(numberOfLines - (lineIndex), characterToPrint).rjust(numberOfLines))

if __name__ == "__main__":
    main()
