import string


class Room:
    def __init__(self, name, sectorID, checkSum):
        self.name = name
        self.sectorID = sectorID
        self.checksum = checkSum



def parse(roomStr):
    nameAndID, checksum = roomStr.split("[")
    checksum = checksum.strip("]")
    l = nameAndID.split("-")
    ID = int(l.pop(len(l) - 1))
    name = "".join(l)
    return Room(name, ID, checksum)


def getLetterCounts(n):
    letterCounts = dict.fromkeys(string.ascii_lowercase, 0)
    for char in n:
        letterCounts[char] += 1
    return letterCounts


def getTopFiveLetters(letterCounts):
    topFive = ""
    for i in range(1000, 0, -1):
        for char in string.ascii_lowercase:
            if letterCounts[char] == i:
                topFive += char
                if len(topFive) == 5:
                    return topFive
    print("Error: couldn't find five different letters " + letterCounts)


def main():
    inputFile = open("input.txt", "r")
    ins = inputFile.read().split("\n")

    rooms = []
    for roomStr in ins:
        rooms.append(parse(roomStr))

    sumSectorIDs = 0
    for room in rooms:
        lc = getLetterCounts(room.name)
        topFive = getTopFiveLetters(lc)
        if topFive == room.checksum:
            sumSectorIDs += room.sectorID

    print("Sum of sector IDs: " + str(sumSectorIDs))


main()