def parse(c):
    return [c[:1], int(c[1:])]

def main():
    inputFile = open("input.txt", "r")
    ins = inputFile.read()
    commands = ins.split(", ")

    facing = 0  # number between 0 and 4. Increased by turning right, decreased by turning left
    moves = [0, 0, 0, 0]

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
        moves[facing] += dist

    total = abs(moves[0] - moves[2]) + abs(moves[1] - moves[3])
    print ("Total moves: " + str(total))



main()