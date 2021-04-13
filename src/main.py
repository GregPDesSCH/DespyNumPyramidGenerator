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

# Main menu selection constants
_OPTION_FOR_SIMPLE_PYRAMID = 1
_FIRST_OPTION_FOR_SEQUENCE_OPTION = 2
_LAST_OPTION_FOR_SEQUENCE_OPTION = 5
_FIRST_OPTION_FOR_NUMBER_TRIANGLE_OPTION = 6
_LAST_OPTION_FOR_NUMBER_TRIANGLE_OPTION = 9
_OPTION_TO_QUIT_PROGRAM = 10


def _selectSequence(sequenceIndex):
    """
    Selects a mathematical sequence to generate the numbers and print the 
    pyramid.

    Params:
    sequenceIndex - User's selection of what sequence to interact.
    """
    if sequenceIndex == 2:
        printSequencePyramids("fibonacci") # Fibonacci sequence
    elif sequenceIndex == 3:
        printSequencePyramids("triangle") # Triangle numbers
    elif sequenceIndex == 4:
        printSequencePyramids("alternatingBits") # Alternating bits
    elif sequenceIndex == 5:
        printSequencePyramids("squares")

def _selectNumberTriangle(sequenceIndex):
    """
    Selects a famous mathematical triangle to print out.

    Params:
    sequenceIndex - User's selection of what sequence to interact.
    """
    if sequenceIndex == 6:
        printNumberTrianglePyramids("pascal") # Pascal's Triangle
    elif sequenceIndex == 7:
        printNumberTrianglePyramids("euler") # Euler's Triangle
    elif sequenceIndex == 8:
        printNumberTrianglePyramids("catalan") # Catalan's Triangle
    elif sequenceIndex == 9:
        printNumberTrianglePyramids("bernoulli") # Bernoulli's Triangle

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
