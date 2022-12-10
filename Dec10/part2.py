def do_add(x, instruction, to_wait):
    if to_wait > 1:
        return x, to_wait-1
    else:
        return x + int(instruction[1]), 0

def crt(x, cycle):
    pixel = (cycle-1)%40

    if abs(pixel - x) <= 1:
        print("█", end="")
    else:
        print(" ", end="")

    if pixel == 39:
        print("")

with open("input.txt") as f:
    x = 1
    cycle = 1
    
    decoded_val = 0

    for line in f:
        parts = line.rstrip().split()

        if parts[0] == "addx":
            wait = 2
            while wait > 0:
                crt(x, cycle)
                x, wait = do_add(x, parts, wait)

                cycle += 1
        else:
            crt(x, cycle)
            cycle += 1


