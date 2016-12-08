# sadly day 3 part 1 was lost to the sands of time and the idiocy of this developer
# it was mostly just the latter half of this file's main() function though
# I did do it, honest!


def flattenListOfLists(l):
    return [item for sublist in l for item in sublist]


def main():
    inputFile = open("input.txt", "r")
    ins = inputFile.read()

    rows = ins.split("\n")
    cols = [[], [], []]
    for row in rows:
        rowSides = row.split()
        for i in range(len(rowSides)):
            cols[i].append(rowSides[i])

    allSides = flattenListOfLists(cols)
    assert(len(allSides) % 3 == 0)

    triangles = []
    for tri in range(0, len(allSides), 3):
        triangles.append([])
        for side in range(3):
            triangles[-1].append(allSides[tri + side])

    validCount = 0

    for triangle in triangles:
        assert(len(triangle) == 3)
        sides = []
        for sideStr in triangle:
            sides.append(int(sideStr))

        sides = sorted(sides) # sort ascending order

        sumSmallerSides = 0
        for smallerSide in sides[0:-1]:
            sumSmallerSides += smallerSide

        if sumSmallerSides > sides[-1]:
            validCount += 1

    print("Valid triangles: " + str(validCount))

main()