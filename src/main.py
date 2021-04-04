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

_optionForSimplePyramid = 1
_firstOptionForSequenceOption = 2
_lastOptionForSequenceOption = 4
_firstOptionForNumberTriangleOption = 5
_lastOptionForNumberTriangleOption = 7
_optionToQuitProgram = 8

def _selectSequence(sequenceIndex):
    if sequenceIndex == 2:
        printSequencePyramids("fibonacci")
    elif sequenceIndex == 3:
        printSequencePyramids("triangle")
    elif sequenceIndex == 4:
        printSequencePyramids("alternatingBits")

def _selectNumberTriangle(sequenceIndex):
    if sequenceIndex == 5:
        printNumberTrianglePyramids("pascal")
    elif sequenceIndex == 6:
        printNumberTrianglePyramids("euler")
    elif sequenceIndex == 7:
        printNumberTrianglePyramids("catalan")

def main():
    print("DespyNumPyramidGenerator\nby Gregory Desrosiers\n")

    while True:
        sequenceIndex = selectSequence()

        if sequenceIndex == _optionForSimplePyramid:
            printSimplePyramids()
        elif sequenceIndex >= _firstOptionForSequenceOption and sequenceIndex <= _lastOptionForSequenceOption:
            _selectSequence(sequenceIndex)
        elif sequenceIndex >= _firstOptionForNumberTriangleOption and sequenceIndex <= _lastOptionForNumberTriangleOption:
            _selectNumberTriangle(sequenceIndex)
        if sequenceIndex == _optionToQuitProgram:
            break

    print("See you!\n\nBy Gregory Desrosiers\nhttps://gregpdessch.github.io\nhttps://www.linkedin.com/in/gregorydesrosiers")

if __name__ == "__main__":
    main()
