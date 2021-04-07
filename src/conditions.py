"""

    DespyNumPyramidGenerator - Conditions

    Holds functions for common checks.

    Start Date: March 8, 2021
    End Date:

    File Name: conditions.py

"""

_maximumCharactersInOneLine = 160

def numberIsAWholeNumber(rawNumber):
    try:
        int(rawNumber)
        return True
    except ValueError:
        return False

def numberOfCharactersToPrintIsTooHigh(printCommand, numberOfLines, stepWidth):
    return numberOfLines * stepWidth > _maximumCharactersInOneLine or (printCommand == 3 or printCommand == 4 or printCommand == 7 
            or printCommand == 8 or printCommand == 9) and 2 * numberOfLines * stepWidth > _maximumCharactersInOneLine