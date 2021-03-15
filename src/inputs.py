"""

    DespyNumPyramidGenerator - Inputs

    Holds common input functions.

    Start Date: March 10, 2021
    End Date:

    File Name: inputs.py

"""

from conditions import numberIsAWholeNumber

def printCommandMenu():
    print("Pick an option from one of the following:", "1 - Left Pyramid", "2 - Right Pyramid", "3 - Full Pyramid",
        "4 - Silhouette Pyramid", "5 - Upside Down Left Pyramid", "6 - Upside Down Right Pyramid", 
        "7 - Upside Down Pyrmaid", "8 - Silhouette Pyramid (Upside Down)", "9 - All Options", "10 - Quit", sep="\n")

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