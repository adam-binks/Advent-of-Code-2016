def isValid(pos):
    for axis in (0, 1):
        if pos[axis] < 0 or pos[axis] > 2: # 3x3 keypad
            return False
    return True


def coordsToKeypadNum(coords):
    return (coords[0] + 1) + coords[1]*3


def main():
    file = open("input.txt", "r")
    ins = file.read()
    commands = ins.split()

    directions = {"U": [0, -1], "D": [0, 1], "R": [1, 0], "L": [-1, 0]}

    sequence = ""
    pos = [1, 1]  # 5 on the keypad
                  # [0, 0] is 1, [2, 2] is 9

    for command in commands:
        for char in command:
            newPos = [pos[0] + directions[char][0], pos[1] + directions[char][1]]
            if isValid(newPos):
                pos = newPos
        sequence += str(coordsToKeypadNum(pos))

    print("Sequence: " + sequence)

main()