"""

    DespyNumPyramidGenerator - Conditions

    Holds functions for common checks.

    Start Date: March 8, 2021
    End Date:

    File Name: conditions.py

"""

# Max characters to print in one line
_MAXIMUM_CHARACTERS_IN_ONE_LINE = 160


def numberIsAWholeNumber(rawNumber):
    """
    Checks if the input is a whole number or not by parsing.

    Params:
    rawNumber - A string holding the user's raw input (which may be a number)

    Returns:
    Flag representing whether the input is a whole number or not.
    """
    try:
        int(rawNumber)
        return True
    except ValueError:
        return False


def numberOfCharactersToPrintIsTooHigh(printCommand, numberOfLines, stepWidth):
    """
    Checks if the required number of characters to print out at most is over 
    the console width limit.
    (only for simple pyramids and pyramids involving sequences)

    Params:
    printCommand - User's selection of orientation for the pyramid to be
    printed out.
    numberOfLines - User's selection of the number of lines to be printed.
    stepWidth - User's selection of the pyramid's step width.

    Returns:
    Flag representing whether there's at most more than 160 characters to print
    in a single line or not.
    """
    return numberOfLines * stepWidth > _MAXIMUM_CHARACTERS_IN_ONE_LINE \
            or (printCommand == 3 or printCommand == 4 or printCommand == 7 \
            or printCommand == 8 or printCommand == 9) and 2 * numberOfLines \
            * stepWidth > _MAXIMUM_CHARACTERS_IN_ONE_LINE