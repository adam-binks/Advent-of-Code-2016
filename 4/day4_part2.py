import string


class Room:
    def __init__(self, name, sectorID, checkSum, dashedName):
        self.name = name
        self.sectorID = sectorID
        self.checksum = checkSum
        self.dashedName = dashedName



def parse(roomStr):
    nameAndID, checksum = roomStr.split("[")
    checksum = checksum.strip("]")
    l = nameAndID.split("-")
    ID = int(l.pop(len(l) - 1))
    name = "".join(l)
    dashedName = "-".join(l)
    return Room(name, ID, checksum, dashedName)


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


def getRealRooms(rooms):
    realRooms = []
    for room in rooms:
        lc = getLetterCounts(room.name)
        topFive = getTopFiveLetters(lc)
        if topFive == room.checksum:
            realRooms.append(room)
    return realRooms


def decrypt(n, num):
    decrypted = ""
    for i in range(len(n)):
        decrypted += shiftChar(n[i], num)
    return decrypted


def shiftChar(char, num):
    if char == "-":
        return " "

    i = string.ascii_lowercase.index(char)
    i += num
    i = i % len(string.ascii_lowercase)
    return string.ascii_lowercase[i]



def main():
    inputFile = open("input.txt", "r")
    ins = inputFile.read().split("\n")

    allRooms = []
    for roomStr in ins:
        allRooms.append(parse(roomStr))

    rooms = getRealRooms(allRooms)
    northPoleRoom = None
    for room in rooms:
        d = decrypt(room.dashedName, room.sectorID)
        # print(d)
        if "northpole" in d.lower():
            northPoleRoom = room
            northPoleRoom.decrypted = d

    if northPoleRoom is not None:
        print("Decrypted: " + northPoleRoom.decrypted +
              ", ID: " + str(northPoleRoom.sectorID))



main()