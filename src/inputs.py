"""

    DespyNumPyramidGenerator - Inputs

    Holds common input functions.

    Start Date: March 10, 2021
    End Date:

    File Name: inputs.py

"""

from conditions import numberIsAWholeNumber

_goBackToPreviousMenuInputString = "--"
_goBackToPreviousMenuInputNum = -1

def inputIsGoBackCommand(userInput):
    return userInput == _goBackToPreviousMenuInputString or userInput == _goBackToPreviousMenuInputNum

def printMainMenu():
    print("Pick which sequence you would like to perform printing on.", "1 - Simple", "2 - Fibonacci", "3 - Triangle", 
        "4 - Alternating Bits", "5 - Pascal's Triangle", "6 - Euler's Triangle", "7 - Catalan's Triangle", "8 - Quit Program", sep="\n")

def selectSequence():
    rawPrintCommand = ""
    printCommand = 0
    while len(rawPrintCommand) == 0 or len(rawPrintCommand) > 1 or printCommand < 1 or printCommand > 8 \
        or not numberIsAWholeNumber(rawPrintCommand):
        printMainMenu()
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

def printPyramidCommandMenu(triangleIsANumberTriangle):
    print("Pick an option from one of the following:")

    if triangleIsANumberTriangle == True:
        print("1 - Left Pyramid", "2 - Right Pyramid", "3 - Center Pyramid",
            "4 - Upside Down Left Pyramid", "5 - Upside Down Right Pyramid", "6 - Upside Down Center Pyrmaid", 
            "7 - All Options", "8 - Back to Previous Menu", sep="\n")
    else:
        print("1 - Left Pyramid", "2 - Right Pyramid", "3 - Full Pyramid", "4 - Silhouette Pyramid", 
            "5 - Upside Down Left Pyramid", "6 - Upside Down Right Pyramid",  "7 - Upside Down Pyrmaid", 
            "8 - Silhouette Pyramid (Upside Down)", "9 - All Options", "10 - Back to Previous Menu", sep="\n")

    

def selectPrintPyramidCommand(lastCommandIndex = 10, triangleIsANumberTriangle = False):
    rawPrintCommand = ""
    printCommand = 0
    while len(rawPrintCommand) == 0 or len(rawPrintCommand) > 2 or printCommand < 1 or printCommand > lastCommandIndex \
        or not numberIsAWholeNumber(rawPrintCommand):
        printPyramidCommandMenu(triangleIsANumberTriangle)
        rawPrintCommand = input(f'Select option [1-{lastCommandIndex}]: ')
        if len(rawPrintCommand) == 0:
            print("ERROR - Input must not be empty.")
        elif not numberIsAWholeNumber(rawPrintCommand):
            print("ERROR - Input must be a whole positive number.")
        else:
            printCommand = int(rawPrintCommand)
            if printCommand < 1 or printCommand > lastCommandIndex:
                print(f"ERROR - Command must be in the range [1-{lastCommandIndex}].")
    
    return printCommand

def getNumberOfLinesFromUser(maxNumberOfLines = 80):
    rawNumberOfLines = ""
    numberOfLines = 0

    while len(rawNumberOfLines) == 0 or numberOfLines < 3 or numberOfLines > maxNumberOfLines \
        or not numberIsAWholeNumber(rawNumberOfLines):
        print("Enter number of lines to make the triangle, or type -- to go back to the previous menu.")
        rawNumberOfLines = input("Number of lines for triangle? ")
        if len(rawNumberOfLines) == 0:
            print("ERROR - Input must not be empty.")
        elif inputIsGoBackCommand(rawNumberOfLines):
            numberOfLines = -1
            break
        elif not numberIsAWholeNumber(rawNumberOfLines):
            print("ERROR - Input must be a whole positive number.")
        else:
            numberOfLines = int(rawNumberOfLines)
            if numberOfLines < 3 or numberOfLines > maxNumberOfLines:
                print(f"ERROR - Number of lines must be in the range [3-{maxNumberOfLines}].")
        
    return numberOfLines

def getStepWidth():
    rawStepWidth = ""
    stepWidth = 0

    while len(rawStepWidth) == 0 or stepWidth < 1 or stepWidth > 10 or not numberIsAWholeNumber(rawStepWidth):
        print("Enter the width of each triangle step, or type -- to go back to the previous menu.")
        rawStepWidth = input("Width of each step? ")
        if len(rawStepWidth) == 0:
            print("ERROR - Input must not be empty.")
        elif inputIsGoBackCommand(rawStepWidth):
            stepWidth = -1
            break
        elif not numberIsAWholeNumber(rawStepWidth):
            print("ERROR - Input must be a whole positive number.")
        else:
            stepWidth = int(rawStepWidth)
            if stepWidth < 1 or stepWidth > 10:
                print("ERROR - Step width must be in the range [1-10].")

    return stepWidth