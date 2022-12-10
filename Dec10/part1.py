def do_add(x, instruction, to_wait):
    if to_wait > 1:
        return x, to_wait-1
    else:
        return x + int(instruction[1]), 0

def decode(ongoing_sum, x, cycle):
    if (cycle-20)%40 == 0:
        print(x*cycle)
        new_val = ongoing_sum + (x*cycle)
        return new_val
    else:
        return ongoing_sum

with open("input.txt") as f:
    x = 1
    cycle = 1
    
    decoded_val = 0

    for line in f:
        parts = line.rstrip().split()

        if parts[0] == "addx":
            wait = 2
            while wait > 0:
                decoded_val = decode(decoded_val, x, cycle)
                x, wait = do_add(x, parts, wait)

                cycle += 1
        else:
            decoded_val = decode(decoded_val, x, cycle)
            cycle += 1

    print(decoded_val)

