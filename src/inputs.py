"""

    DespyNumPyramidGenerator - Inputs

    Holds common input functions.

    Start Date: March 10, 2021
    End Date:

    File Name: inputs.py

"""

from conditions import numberIsAWholeNumber

# Constants for going back to previous menu
_GO_BACK_TO_PREVIOUS_MENU_INPUT_STRING = "--"
_GO_BACK_TO_PREVIOUS_MENU_INPUT_NUM = -1

# Error message constants
_ERROR_MESSAGE_PREFIX = "ERROR - "
_INPUT_EMPTY_ERROR_MESSAGE = _ERROR_MESSAGE_PREFIX + "Input must not be empty."
_INPUT_NOT_POSITIVE_NUMBER_ERROR_MESSAGE = _ERROR_MESSAGE_PREFIX \
        + "Input must be a whole positive number."

# Constants for lines
_PRINT_LINE_SEPARATOR = "\n"
_MINIMUM_NUMBER_OF_LINES = 3
_DEFAULT_MAXIMUM_NUMBER_OF_LINES = 80

# Step width constants
_MINIMUM_STEP_WIDTH = 1
_MAXIMUM_STEP_WIDTH = 10

# Program menu constants
_FIRST_OPTION_FOR_PROGRAM = 1
_LAST_OPTION_FOR_PROGRAM = 10

# Orientation option constant
_FIRST_OPTION_FOR_PRINTING = 1

# Checks if input is empty
def _inputIsEmpty(rawInput):
    return len(rawInput) == 0


def inputIsGoBackCommand(userInput):
    """
    Checks if the input is the command to go back to the previous menu.

    Params:
    userInput - User's raw input

    Returns:
    Flag saying whether or not the user's input is to go back to the previous
    menu.

    """
    return userInput == _GO_BACK_TO_PREVIOUS_MENU_INPUT_STRING \
            or userInput == _GO_BACK_TO_PREVIOUS_MENU_INPUT_NUM


def getErrorMessagePrefix():
    """
    Gets the prefix for printing out error messages.

    Returns:
    _ERROR_MESSAGE_PREFIX - Prefix for error messages.
    """
    return _ERROR_MESSAGE_PREFIX

def getInputEmptyErrorMessage():
    """
    Gets the error message for inputs that are empty.

    Returns:
    _ERROR_MESSAGE_PREFIX - Prefix for error messages.
    """
    return _INPUT_EMPTY_ERROR_MESSAGE



def printMainMenu():
    """Prints out the main menu of the program"""
    print("Pick which type of pyramid you would like to perform printing on.",
          "1 - Simple", "2 - Fibonacci", "3 - Triangular Number",
          "4 - Alternating Bits", "5 - Square Numbers", 
          "6 - Pascal's Triangle", "7 - Euler's Triangle", 
          "8 - Catalan's Triangle", "9 - Bernoulli's Triangle",
          "10 - Quit Program",
          sep=_PRINT_LINE_SEPARATOR)


def selectSequence():
    """
    Reads in user input for selecting the sequence to interact.

    Returns:
    printCommand - User's selection of sequence to interact.
    """
    rawPrintCommand = ""
    printCommand = 0

    while _inputIsEmpty(rawPrintCommand) or printCommand \
            < _FIRST_OPTION_FOR_PROGRAM or printCommand \
            > _LAST_OPTION_FOR_PROGRAM \
            or not numberIsAWholeNumber(rawPrintCommand):
        printMainMenu()

        rawPrintCommand = input(
                f"Select option [{_FIRST_OPTION_FOR_PROGRAM}-"
                f"{_LAST_OPTION_FOR_PROGRAM}]: ")
        if _inputIsEmpty(rawPrintCommand):
            print(_INPUT_EMPTY_ERROR_MESSAGE)
        elif not numberIsAWholeNumber(rawPrintCommand):
            print(_INPUT_NOT_POSITIVE_NUMBER_ERROR_MESSAGE)
        else:
            printCommand = int(rawPrintCommand)
            if printCommand < _FIRST_OPTION_FOR_PROGRAM or printCommand \
                    > _LAST_OPTION_FOR_PROGRAM:
                print(_ERROR_MESSAGE_PREFIX + "Command must be in the range "
                      f"[{_FIRST_OPTION_FOR_PROGRAM}-"
                      f"{_LAST_OPTION_FOR_PROGRAM}].")

        print()

    return printCommand


def printPyramidCommandMenu(triangleIsANumberTriangle):
    """
    Prints out a menu of possible orientations to print the pyramid of the 
    selected sequence.

    Params:
    triangleIsANumberTriangle - Flag denoting whether the pyramid chosen is a
    famous number triangle.
    """
    print("Pick an option from one of the following:")

    if triangleIsANumberTriangle:
        print("1 - Left Pyramid", "2 - Right Pyramid", "3 - Center Pyramid", 
              "4 - Upside Down Left Pyramid", "5 - Upside Down Right Pyramid", 
              "6 - Upside Down Center Pyrmaid", "7 - All Options", 
              "8 - Back to Previous Menu", sep=_PRINT_LINE_SEPARATOR)
    else:
        print("1 - Left Pyramid", "2 - Right Pyramid", "3 - Full Pyramid", 
              "4 - Silhouette Pyramid", "5 - Upside Down Left Pyramid", 
              "6 - Upside Down Right Pyramid",  "7 - Upside Down Pyrmaid", 
              "8 - Silhouette Pyramid (Upside Down)", "9 - All Options", 
              "10 - Back to Previous Menu", sep=_PRINT_LINE_SEPARATOR)

    
def selectPrintPyramidCommand(
        lastCommandIndex = 10, 
        triangleIsANumberTriangle = False):
    """
    Reads in user input for selecting which orientation to print the pyramid
    of the selected sequence out of.

    Params:
    lastCommandIndex - Number representing the last option the user can enter.
    triangleIsANumberTriangle - Flag denoting whether the pyramid chosen is a
    famous number triangle.

    Returns:
    printCommand - User's selection of orientation for the pyramid to be
    printed out.
    """
    rawPrintCommand = ""
    printCommand = 0

    while _inputIsEmpty(rawPrintCommand) or printCommand \
            < _FIRST_OPTION_FOR_PRINTING or printCommand > lastCommandIndex \
            or not numberIsAWholeNumber(rawPrintCommand):
        printPyramidCommandMenu(triangleIsANumberTriangle)

        rawPrintCommand = input(f"Select option [{_FIRST_OPTION_FOR_PRINTING}"
                                f"-{lastCommandIndex}]: ")
        if _inputIsEmpty(rawPrintCommand):
            print(_INPUT_EMPTY_ERROR_MESSAGE)
        elif not numberIsAWholeNumber(rawPrintCommand):
            print(_INPUT_NOT_POSITIVE_NUMBER_ERROR_MESSAGE)
        else:
            printCommand = int(rawPrintCommand)
            if printCommand < _FIRST_OPTION_FOR_PRINTING or printCommand \
            > lastCommandIndex:
                print(_ERROR_MESSAGE_PREFIX + "Command must be in the range ["
                      f"{_FIRST_OPTION_FOR_PRINTING}-{lastCommandIndex}].")

        print()
    
    return printCommand


def getNumberOfLinesFromUser(
        maxNumberOfLines = _DEFAULT_MAXIMUM_NUMBER_OF_LINES):
    """
    Reads in user input for the number of lines the pyramid to be printed will
    be made up of.

    Params:
    maxNumberOfLines - Maximum number of lines the user can print out.

    Returns:
    numberOfLines - User's selection of the number of lines to be printed.
    """
    rawNumberOfLines = ""
    numberOfLines = 0

    while _inputIsEmpty(rawNumberOfLines) or numberOfLines \
            < _MINIMUM_NUMBER_OF_LINES or numberOfLines > maxNumberOfLines \
            or not numberIsAWholeNumber(rawNumberOfLines):
        print("Enter number of lines to make the triangle, or type -- to go "
              "back to the previous menu.")

        rawNumberOfLines = input("Number of lines for triangle? ")
        if _inputIsEmpty(rawNumberOfLines):
            print(_INPUT_EMPTY_ERROR_MESSAGE)
        elif inputIsGoBackCommand(rawNumberOfLines):
            numberOfLines = -1
            print()
            break
        elif not numberIsAWholeNumber(rawNumberOfLines):
            print(_INPUT_NOT_POSITIVE_NUMBER_ERROR_MESSAGE)
        else:
            numberOfLines = int(rawNumberOfLines)
            if numberOfLines < _MINIMUM_NUMBER_OF_LINES or numberOfLines \
                    > maxNumberOfLines:
                print(_ERROR_MESSAGE_PREFIX + f"Number of lines must be in the"
                      f" range [{_MINIMUM_NUMBER_OF_LINES}-{maxNumberOfLines}]"
                      ".")

        print()
        
    return numberOfLines


def getStepWidth():
    """
    Reads in user input for the step width of the pyramid to print.

    Returns:
    stepWidth - User's selection of the pyramid's step width.
    """
    rawStepWidth = ""
    stepWidth = 0

    while _inputIsEmpty(rawStepWidth) or stepWidth < _MINIMUM_STEP_WIDTH \
            or stepWidth > _MAXIMUM_STEP_WIDTH \
            or not numberIsAWholeNumber(rawStepWidth):
        print("Enter the width of each triangle step, or type -- to go back to"
              " the previous menu.")

        rawStepWidth = input("Width of each step? ")
        if _inputIsEmpty(rawStepWidth):
            print(_INPUT_EMPTY_ERROR_MESSAGE)
        elif inputIsGoBackCommand(rawStepWidth):
            stepWidth = -1
            print()
            break
        elif not numberIsAWholeNumber(rawStepWidth):
            print(_INPUT_NOT_POSITIVE_NUMBER_ERROR_MESSAGE)
        else:
            stepWidth = int(rawStepWidth)
            if stepWidth < _MINIMUM_STEP_WIDTH or stepWidth \
                    > _MAXIMUM_STEP_WIDTH:
                print(_ERROR_MESSAGE_PREFIX + "Step width must be in the range"
                      f" [{_MINIMUM_STEP_WIDTH}-{_MAXIMUM_STEP_WIDTH}].")

        print()

    return stepWidth