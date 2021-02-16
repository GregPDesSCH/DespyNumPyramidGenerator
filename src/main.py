"""

    DespyNumPyramidGenerator - Main Script

    Starting point for this program.

    Start Date: January 24, 2021
    End Date:

    File Name: main.py

"""

def main():
    numberOfLines = 10
    characterToPrint = '8'

    # Left Pyramid
    for lineIndex in range(numberOfLines):
        print("".ljust(lineIndex + 1, characterToPrint).ljust(numberOfLines))

    # Right Pyramid
    for lineIndex in range(numberOfLines):
        print("".ljust(lineIndex + 1, characterToPrint).rjust(numberOfLines))

    # Full Pyramid
    for lineIndex in range(numberOfLines):
        print("".ljust(lineIndex + 1, characterToPrint).rjust(numberOfLines) + "".rjust(lineIndex + 1, characterToPrint).ljust(numberOfLines))

    # Upside Down Left Pyramid
    for lineIndex in range(numberOfLines):
        print("".ljust(numberOfLines - (lineIndex), characterToPrint).ljust(numberOfLines))

    # Upside Down Right Pyramid
    for lineIndex in range(numberOfLines):
        print("".rjust(numberOfLines - (lineIndex), characterToPrint).rjust(numberOfLines))

    # Upside Down Pyramid
    for lineIndex in range(numberOfLines):
        print("".ljust(numberOfLines - (lineIndex), characterToPrint).ljust(numberOfLines) + \
            "".rjust(numberOfLines - (lineIndex), characterToPrint).rjust(numberOfLines))

if __name__ == "__main__":
    main()
