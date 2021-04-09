"""

    DespyNumPyramidGenerator - Conditions

    Holds functions for common checks.

    Start Date: March 8, 2021
    End Date:

    File Name: conditions.py

"""

_MAXIMUM_CHARACTERS_IN_ONE_LINE = 160


def numberIsAWholeNumber(rawNumber):
    """Checks if the input is a whole number or not by parsing."""
    try:
        int(rawNumber)
        return True
    except ValueError:
        return False


def numberOfCharactersToPrintIsTooHigh(printCommand, numberOfLines, stepWidth):
    """Checks if the required number of characters to print out at most is over the console width limit."""
    return numberOfLines * stepWidth > _MAXIMUM_CHARACTERS_IN_ONE_LINE or (printCommand == 3 or printCommand == 4 or printCommand == 7
            or printCommand == 8 or printCommand == 9) and 2 * numberOfLines * stepWidth > _MAXIMUM_CHARACTERS_IN_ONE_LINE