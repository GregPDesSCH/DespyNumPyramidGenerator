"""

    DespyNumPyramidGenerator - Conditions

    Holds functions for common checks.

    Start Date: March 8, 2021
    End Date:

    File Name: conditions.py

"""

def numberIsAWholeNumber(rawNumber):
    try:
        int(rawNumber)
        return True
    except ValueError:
        return False