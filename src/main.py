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

        if sequenceIndex == 1:
            printSimplePyramids()
        elif sequenceIndex >= 2 and sequenceIndex <= 4:
            _selectSequence(sequenceIndex)
        elif sequenceIndex >= 5 and sequenceIndex <= 7:
            _selectNumberTriangle(sequenceIndex)
        if sequenceIndex == 8:
            break

    print("See you!\n\nBy Gregory Desrosiers\nhttps://gregpdessch.github.io\nhttps://www.linkedin.com/in/gregorydesrosiers")

if __name__ == "__main__":
    main()
