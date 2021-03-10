"""

    DespyNumPyramidGenerator - Inputs

    Holds common input functions.

    Start Date: March 10, 2021
    End Date:

    File Name: inputs.py

"""

from conditions import numberIsAWholeNumber

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