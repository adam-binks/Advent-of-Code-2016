# keypad = [["", "", "1", "", ""],
#           ["", "2", "3", "4", ""],
#           ["5", "6", "7", "8", "9"],
#           ["", "A", "B", "C", ""],
#           ["", "", "D", "", ""], ]

# I use [x, y] for position
keypad = [["", "", "5", "", ""],
          ["", "2", "6", "A", ""],
          ["1", "3", "7", "B", "D"],
          ["", "4", "8", "C", ""],
          ["", "", "9", "", ""]]

def isValid(pos):
    # check if outside bounds of keypad
    for axis in (0, 1):
        if pos[axis] < 0 or pos[axis] > 4: # 5x5 keypad
            return False
    # check if the key exists on the keypad
    return keypad[pos[0]][pos[1]] != ""


def coordsToKeypadNum(coords):
    return keypad[coords[0]][coords[1]]


def main():
    file = open("input.txt", "r")
    ins = file.read()
    commands = ins.split()

    directions = {"U": [0, -1], "D": [0, 1], "R": [1, 0], "L": [-1, 0]}

    sequence = ""
    pos = [0, 2]  # 5 on the keypad

    for command in commands:
        for char in command:
            newPos = [pos[0] + directions[char][0], pos[1] + directions[char][1]]
            if isValid(newPos):
                pos = newPos
        sequence += coordsToKeypadNum(pos)

    print("Sequence: " + sequence)


main()