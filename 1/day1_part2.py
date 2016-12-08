def parse(c):
    return [c[:1], int(c[1:])]

def checkDone(pos, visited):
    if pos in visited:
        print("Location is " + str(pos))
        print("Blocks away " + str(abs(pos[0]) + abs(pos[1])))
        return True
    else:
        visited.append([pos[0], pos[1]])
        return False

def main():
    inputFile = open("input.txt", "r")
    ins = inputFile.read()
    commands = ins.split(", ")

    facing = 0  # number between 0 and 4. Increased by turning right, decreased by turning left
    pos = [0, 0]
    visited = [[0, 0]]

    for command in commands:
        dir, dist = parse(command)
        if dir == "R":
            facing += 1
            if facing > 3:
                facing = 0
        elif dir == "L":
            facing -= 1
            if facing < 0:
                facing = 3
        else:
            print("invalid direction: " + dir)

        if facing in [0, 1]:
            for i in range(dist):
                pos[facing] += 1
                if checkDone(pos, visited): return
        else:
            for i in range(dist):
                pos[(facing - 2)] -= 1
                if checkDone(pos, visited): return



main()