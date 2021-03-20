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

def main():
    while True:
        sequenceIndex = selectSequence()

        if sequenceIndex == 1:
            printSimplePyramids()
        elif sequenceIndex == 2:
            printSequencePyramids("fibonacci")
        elif sequenceIndex == 3:
            printSequencePyramids("triangle")
        elif sequenceIndex == 4:
            printSequencePyramids("alternatingBits")
        elif sequenceIndex == 5:
            printNumberTrianglePyramids("pascal")
        elif sequenceIndex == 6:
            printNumberTrianglePyramids("euler")
        if sequenceIndex == 7:
            break

if __name__ == "__main__":
    main()
