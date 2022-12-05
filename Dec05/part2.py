def read_stacks(f):
    rows = []

    for line in f:
        if line[1] == "1":
            break

        rows.append(line[1::4])

    stacks = []
    for stack_pos in range(len(rows[0])):
        stack = []
        for i in range(len(rows)-1, -1, -1):
            crate = rows[i][stack_pos]
            if crate == " ":
                break

            stack.append(rows[i][stack_pos])
        stacks.append(stack)

    return stacks

with open("input.txt") as f:
    stacks = read_stacks(f)

    for line in f:
        if line[0] != "m":
            continue

        parts = line.rstrip().split()
        quantity = int(parts[1])
        src = int(parts[3]) - 1
        dest = int(parts[5]) - 1

        stacks[dest].extend(stacks[src][-quantity:len(stacks[src])])
        stacks[src] = stacks[src][:len(stacks[src]) - quantity]

    for stack in stacks:
        print(stack[-1], end="")
    print()