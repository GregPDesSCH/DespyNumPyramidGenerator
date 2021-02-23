"""

    DespyNumPyramidGenerator - Main Script

    Starting point for this program.

    Start Date: January 24, 2021
    End Date:

    File Name: main.py

"""

def printCommandMenu():
    print("Pick an option from one of the following:", "1 - Left Pyramid", "2 - Right Pyramid", "3 - Full Pyramid",
        "4 - Silhouette Pyramid", "5 - Upside Down Left Pyramid", "6 - Upside Down Right Pyramid", 
        "7 - Upside Down Pyrmaid", "8 - Silhouette Pyramid (Upside Down)", "9 - All Options", "10 - Quit", sep="\n")

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

def getStepWidth():
    rawStepWidth = ""
    stepWidth = 0

    while len(rawStepWidth) == 0 or stepWidth < 1 or stepWidth > 10 or not numberIsAWholeNumber(rawStepWidth):
        rawStepWidth = input("Width of each step? ")
        if len(rawStepWidth) == 0:
            print("ERROR - Input must not be empty.")
        elif not numberIsAWholeNumber(rawStepWidth):
            print("ERROR - Input must be a whole positive number.")
        else:
            stepWidth = int(rawStepWidth)
            if stepWidth < 1 or stepWidth > 10:
                print("ERROR - Step width must be in the range [1-10].")

    return stepWidth

def selectPrintCommand():
    rawPrintCommand = ""
    printCommand = 0
    while len(rawPrintCommand) < 0 or len(rawPrintCommand) > 2 or printCommand < 1 or printCommand > 10 \
        or not numberIsAWholeNumber(rawPrintCommand):
        printCommandMenu()
        rawPrintCommand = input('Select option [1-10]: ')
        if len(rawPrintCommand) == 0:
            print("ERROR - Input must not be empty.")
        elif not numberIsAWholeNumber(rawPrintCommand):
            print("ERROR - Input must be a whole positive number.")
        else:
            printCommand = int(rawPrintCommand)
            if printCommand < 1 or printCommand > 10:
                print("ERROR - Command must be in the range [1-8].")
    
    return printCommand

def main():

    while True:
        printCommand = selectPrintCommand()

        if printCommand == 10:
            break

        numberOfLines = getNumberOfLinesFromUser()
        characterToPrint = getCharacterToPrint()
        stepWidth = getStepWidth()

        if numberOfLines * stepWidth > 160:
            print("ERROR - Maximum number of characters to be printed on the screen is 160. Please enter again.")
        else:
            if printCommand == 1 or printCommand == 9:
                # Left Pyramid
                for lineIndex in range(numberOfLines):
                    print("".ljust(stepWidth * (lineIndex + 1), characterToPrint).ljust(stepWidth * numberOfLines))

            if printCommand == 2 or printCommand == 9:
                # Right Pyramid
                for lineIndex in range(numberOfLines):
                    print("".ljust(stepWidth * (lineIndex + 1), characterToPrint).rjust(stepWidth * numberOfLines))

            if printCommand == 3 or printCommand == 9:
                # Full Pyramid
                for lineIndex in range(numberOfLines):
                    print("".ljust(stepWidth * (lineIndex + 1), characterToPrint).rjust(stepWidth * numberOfLines) + \
                        "".rjust(stepWidth * (lineIndex + 1), characterToPrint).ljust(stepWidth * numberOfLines))

            if printCommand == 4 or printCommand == 9:
                # Silhouette Pyramid
                for lineIndex in range(numberOfLines):
                    print("".ljust(stepWidth * (numberOfLines - (lineIndex)), characterToPrint).ljust(stepWidth * numberOfLines) + \
                        "".rjust(stepWidth * (numberOfLines - (lineIndex)), characterToPrint).rjust(stepWidth * numberOfLines))

            if printCommand == 5 or printCommand == 9:
                # Upside Down Left Pyramid
                for lineIndex in range(numberOfLines):
                    print("".ljust(stepWidth * (numberOfLines - (lineIndex)), characterToPrint).ljust(stepWidth * numberOfLines))

            if printCommand == 6 or printCommand == 9:
                # Upside Down Right Pyramid
                for lineIndex in range(numberOfLines):
                    print("".rjust(stepWidth * (numberOfLines - (lineIndex)), characterToPrint).rjust(stepWidth * numberOfLines))

            if printCommand == 7 or printCommand == 9:
                # Upside Down Pyramid
                for lineIndex in range(numberOfLines):
                    print("".ljust(stepWidth * (numberOfLines - (lineIndex)), characterToPrint).rjust(stepWidth * numberOfLines) + \
                        "".rjust(stepWidth * (numberOfLines - (lineIndex)), characterToPrint).ljust(stepWidth * numberOfLines))

            if printCommand == 8 or printCommand == 9:
                # Silhouette Pyramid (Upside Down)
                for lineIndex in range(numberOfLines):
                    print("".ljust(stepWidth * (lineIndex + 1), characterToPrint).ljust(stepWidth * numberOfLines) + \
                        "".rjust(stepWidth * (lineIndex + 1), characterToPrint).rjust(stepWidth * numberOfLines))
            

if __name__ == "__main__":
    main()
