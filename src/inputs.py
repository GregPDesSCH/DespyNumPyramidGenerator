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

_errorMessagePrefix = "ERROR - "
_inputEmptyErrorMessage = _errorMessagePrefix + "Input must not be empty."
_inputNotPositiveNumberErrorMessage = _errorMessagePrefix + "Input must be a whole positive number."

_printLineSeparator = "\n"
_minimumNumberOfLines = 3
_defaultMaximumNumberOfLines = 80

_firstOptionForProgram = 1
_lastOptionForProgram = 8
_firstOptionForPrinting = 1
_minimumStepWidth = 1
_maximumStepWidth = 10

def _inputIsEmpty(rawInput):
    return len(rawInput) == 0

def getErrorMessagePrefix():
    return _errorMessagePrefix

def getInputEmptyErrorMessage():
    return _inputEmptyErrorMessage

def inputIsGoBackCommand(userInput):
    return userInput == _goBackToPreviousMenuInputString or userInput == _goBackToPreviousMenuInputNum

def printMainMenu():
    print("Pick which type of pyramid you would like to perform printing on.", "1 - Simple", "2 - Fibonacci", "3 - Triangular Number", 
        "4 - Alternating Bits", "5 - Pascal's Triangle", "6 - Euler's Triangle", "7 - Catalan's Triangle", "8 - Quit Program", sep=_printLineSeparator)

def selectSequence():
    rawPrintCommand = ""
    printCommand = 0
    while _inputIsEmpty(rawPrintCommand) or printCommand < _firstOptionForProgram or printCommand > _lastOptionForProgram \
        or not numberIsAWholeNumber(rawPrintCommand):
        printMainMenu()
        rawPrintCommand = input(f'Select option [{_firstOptionForProgram}-{_lastOptionForProgram}]: ')
        if _inputIsEmpty(rawPrintCommand):
            print(_inputEmptyErrorMessage)
        elif not numberIsAWholeNumber(rawPrintCommand):
            print(_inputNotPositiveNumberErrorMessage)
        else:
            printCommand = int(rawPrintCommand)
            if printCommand < _firstOptionForProgram or printCommand > _lastOptionForProgram:
                print(_errorMessagePrefix + f"Command must be in the range [{_firstOptionForProgram}-{_lastOptionForProgram}].")

        print()
    return printCommand

def printPyramidCommandMenu(triangleIsANumberTriangle):
    print("Pick an option from one of the following:")

    if triangleIsANumberTriangle == True:
        print("1 - Left Pyramid", "2 - Right Pyramid", "3 - Center Pyramid",
            "4 - Upside Down Left Pyramid", "5 - Upside Down Right Pyramid", "6 - Upside Down Center Pyrmaid", 
            "7 - All Options", "8 - Back to Previous Menu", sep=_printLineSeparator)
    else:
        print("1 - Left Pyramid", "2 - Right Pyramid", "3 - Full Pyramid", "4 - Silhouette Pyramid", 
            "5 - Upside Down Left Pyramid", "6 - Upside Down Right Pyramid",  "7 - Upside Down Pyrmaid", 
            "8 - Silhouette Pyramid (Upside Down)", "9 - All Options", "10 - Back to Previous Menu", sep=_printLineSeparator)

    

def selectPrintPyramidCommand(lastCommandIndex = 10, triangleIsANumberTriangle = False):
    rawPrintCommand = ""
    printCommand = 0
    while _inputIsEmpty(rawPrintCommand) or printCommand < _firstOptionForPrinting or printCommand > lastCommandIndex or not \
        numberIsAWholeNumber(rawPrintCommand):
        printPyramidCommandMenu(triangleIsANumberTriangle)
        rawPrintCommand = input(f'Select option [{_firstOptionForPrinting}-{lastCommandIndex}]: ')
        if _inputIsEmpty(rawPrintCommand):
            print(_inputEmptyErrorMessage)
        elif not numberIsAWholeNumber(rawPrintCommand):
            print(_inputNotPositiveNumberErrorMessage)
        else:
            printCommand = int(rawPrintCommand)
            if printCommand < _firstOptionForPrinting or printCommand > lastCommandIndex:
                print(_errorMessagePrefix + f"Command must be in the range [{_firstOptionForPrinting}-{lastCommandIndex}].")

        print()
    
    return printCommand

def getNumberOfLinesFromUser(maxNumberOfLines = _defaultMaximumNumberOfLines):
    rawNumberOfLines = ""
    numberOfLines = 0

    while _inputIsEmpty(rawNumberOfLines) or numberOfLines < _minimumNumberOfLines or numberOfLines > maxNumberOfLines \
        or not numberIsAWholeNumber(rawNumberOfLines):
        print("Enter number of lines to make the triangle, or type -- to go back to the previous menu.")
        rawNumberOfLines = input("Number of lines for triangle? ")
        if _inputIsEmpty(rawNumberOfLines):
            print(_inputEmptyErrorMessage)
        elif inputIsGoBackCommand(rawNumberOfLines):
            numberOfLines = -1
            print()
            break
        elif not numberIsAWholeNumber(rawNumberOfLines):
            print(_inputNotPositiveNumberErrorMessage)
        else:
            numberOfLines = int(rawNumberOfLines)
            if numberOfLines < _minimumNumberOfLines or numberOfLines > maxNumberOfLines:
                print(_errorMessagePrefix + f"Number of lines must be in the range [{_minimumNumberOfLines}-{maxNumberOfLines}].")

        print()
        
    return numberOfLines

def getStepWidth():
    rawStepWidth = ""
    stepWidth = 0

    while _inputIsEmpty(rawStepWidth) or stepWidth < _minimumStepWidth or stepWidth > _maximumStepWidth or not numberIsAWholeNumber(rawStepWidth):
        print("Enter the width of each triangle step, or type -- to go back to the previous menu.")
        rawStepWidth = input("Width of each step? ")
        if _inputIsEmpty(rawStepWidth):
            print(_inputEmptyErrorMessage)
        elif inputIsGoBackCommand(rawStepWidth):
            stepWidth = -1
            print()
            break
        elif not numberIsAWholeNumber(rawStepWidth):
            print(_inputNotPositiveNumberErrorMessage)
        else:
            stepWidth = int(rawStepWidth)
            if stepWidth < _minimumStepWidth or stepWidth > _maximumStepWidth:
                print(_errorMessagePrefix + f"Step width must be in the range [{_minimumStepWidth}-{_maximumStepWidth}].")

        print()

    return stepWidth