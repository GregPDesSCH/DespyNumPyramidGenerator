"""

    DespyNumPyramidGenerator - Sequences

    Script responsible for printing number triangles

    Start Date: March 18, 2021
    End Date:

    File Name: number_triangles.py

"""

from generator import generateNumberTriangle


def generateNumberTriangleLines(numberTriangle, numberOfLines, pyramidIsUpsideDown):
    if numberOfLines > len(numberTriangle):
        print(f"This number triangle only has {len(numberTriangle)} lines. Please use a smaller number of lines.")
        return None

    numberTriangleLines = []

    startingIndex = 0 if pyramidIsUpsideDown == False else numberOfLines - 1
    endingIndex = numberOfLines if pyramidIsUpsideDown == False else - 1
    loopStep = -1 if pyramidIsUpsideDown == True else 1
    
    for lineIndex in range(startingIndex, endingIndex, loopStep):
        currentLine = ""
        for index, elem in enumerate(numberTriangle[lineIndex]):
            currentLine += str(elem)
            if index < len(numberTriangle[lineIndex]) - 1:
                currentLine += " "
        numberTriangleLines.append(currentLine)

    return numberTriangleLines

# For testing only
if __name__ == "__main__":
    print("Generating Pascal's Triangle")
    triangle = generateNumberTriangle("pascal")
    print("Creating lines of triangle")
    triangleLines = generateNumberTriangleLines(triangle, 10, False)
    print("Printing triangle")
    for line in triangleLines:
        print(line)
    print("End")