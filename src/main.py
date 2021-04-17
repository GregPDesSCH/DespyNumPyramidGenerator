"""

    DespyNumPyramidGenerator - Main Script

    Starting point for this program.

    Start Date: January 24, 2021
    End Date:

    File Name: main.py

"""

from inputs import selectSequence
from number_triangles import printNumberTrianglePyramids
from sequences import printSequencePyramids
from simple import printSimplePyramids
from generator import getListOfSequenceNames, getListOfNumberTriangleNames

# Main menu selection constants
_OPTION_FOR_SIMPLE_PYRAMID = 1
_FIRST_OPTION_FOR_SEQUENCE_OPTION = 2
_LAST_OPTION_FOR_SEQUENCE_OPTION = 6
_FIRST_OPTION_FOR_NUMBER_TRIANGLE_OPTION = 7
_LAST_OPTION_FOR_NUMBER_TRIANGLE_OPTION = 11
_OPTION_TO_QUIT_PROGRAM = 12


def _selectSequence(sequenceIndex):
    """
    Selects a mathematical sequence to generate the numbers and print the 
    pyramid.

    Params:
    sequenceIndex - User's selection of what sequence to interact.
    """
    if sequenceIndex == 2:
        # Fibonacci sequence
        printSequencePyramids(getListOfSequenceNames()[0]) 
    elif sequenceIndex == 3:
        # Triangle numbers
        printSequencePyramids(getListOfSequenceNames()[1]) 
    elif sequenceIndex == 4:
        # Alternating bits
        printSequencePyramids(getListOfSequenceNames()[2]) 
    elif sequenceIndex == 5:
        # Sequence of squares
        printSequencePyramids(getListOfSequenceNames()[3]) 
    elif sequenceIndex == 6:
        # Sequence of powers of twos
        printSequencePyramids(getListOfSequenceNames()[4]) 

def _selectNumberTriangle(sequenceIndex):
    """
    Selects a famous mathematical triangle to print out.

    Params:
    sequenceIndex - User's selection of what sequence to interact.
    """
    if sequenceIndex == 7:
        # Pascal's Triangle
        printNumberTrianglePyramids(getListOfNumberTriangleNames()[0])
    elif sequenceIndex == 8:
        # Euler's Triangle
        printNumberTrianglePyramids(getListOfNumberTriangleNames()[1])
    elif sequenceIndex == 9:
        # Catalan's Triangle
        printNumberTrianglePyramids(getListOfNumberTriangleNames()[2])
    elif sequenceIndex == 10:
        # Bernoulli's Triangle
        printNumberTrianglePyramids(getListOfNumberTriangleNames()[3])
    elif sequenceIndex == 11:
        # Seidel-Entringer-Arnold Triangle
        printNumberTrianglePyramids(getListOfNumberTriangleNames()[4]) 

def main():
    """Main program loop"""
    print("DespyNumPyramidGenerator\nby Gregory Desrosiers\n")

    while True:
        # Select what sequence to interact with
        sequenceIndex = selectSequence()

        if sequenceIndex == _OPTION_FOR_SIMPLE_PYRAMID:
            printSimplePyramids() 
        elif sequenceIndex >= _FIRST_OPTION_FOR_SEQUENCE_OPTION \
                and sequenceIndex <= _LAST_OPTION_FOR_SEQUENCE_OPTION:
            _selectSequence(sequenceIndex) 
        elif sequenceIndex >= _FIRST_OPTION_FOR_NUMBER_TRIANGLE_OPTION \
                and sequenceIndex <= _LAST_OPTION_FOR_NUMBER_TRIANGLE_OPTION:
            _selectNumberTriangle(sequenceIndex) 
        if sequenceIndex == _OPTION_TO_QUIT_PROGRAM:
            break

    print("See you!\n\nBy Gregory Desrosiers\nhttps://gregpdessch.github.io")
    print("https://www.linkedin.com/in/gregorydesrosiers")

if __name__ == "__main__":
    main()
