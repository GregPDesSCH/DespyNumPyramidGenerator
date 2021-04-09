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


_OPTION_FOR_SIMPLE_PYRAMID = 1
_FIRST_OPTION_FOR_SEQUENCE_OPTION = 2
_LAST_OPTION_FOR_SEQUENCE_OPTION = 4
_FIRST_OPTION_FOR_NUMBER_TRIANGLE_OPTION = 5
_LAST_OPTION_FOR_NUMBER_TRIANGLE_OPTION = 7
_OPTION_TO_QUIT_PROGRAM = 8


# Selects a sequence to generate the numbers and print the pyramid.
def _selectSequence(sequenceIndex):
    if sequenceIndex == 2:
        printSequencePyramids("fibonacci")
    elif sequenceIndex == 3:
        printSequencePyramids("triangle")
    elif sequenceIndex == 4:
        printSequencePyramids("alternatingBits")

# Selects a famous mathematical triangle to print out.
def _selectNumberTriangle(sequenceIndex):
    if sequenceIndex == 5:
        printNumberTrianglePyramids("pascal")
    elif sequenceIndex == 6:
        printNumberTrianglePyramids("euler")
    elif sequenceIndex == 7:
        printNumberTrianglePyramids("catalan")

def main():
    """Main program loop"""
    print("DespyNumPyramidGenerator\nby Gregory Desrosiers\n")

    while True:
        sequenceIndex = selectSequence() # Select what sequence to interact with

        if sequenceIndex == _OPTION_FOR_SIMPLE_PYRAMID:
            printSimplePyramids()
        elif sequenceIndex >= _FIRST_OPTION_FOR_SEQUENCE_OPTION and sequenceIndex <= _LAST_OPTION_FOR_SEQUENCE_OPTION:
            _selectSequence(sequenceIndex)
        elif sequenceIndex >= _FIRST_OPTION_FOR_NUMBER_TRIANGLE_OPTION and sequenceIndex <= _LAST_OPTION_FOR_NUMBER_TRIANGLE_OPTION:
            _selectNumberTriangle(sequenceIndex)
        if sequenceIndex == _OPTION_TO_QUIT_PROGRAM:
            break

    print("See you!\n\nBy Gregory Desrosiers\nhttps://gregpdessch.github.io\nhttps://www.linkedin.com/in/gregorydesrosiers")

if __name__ == "__main__":
    main()
