with open("input.txt") as f:
    line = f.readline().rstrip()

    for i in range(14, len(line)+1):
        chars = set(line[i-14:i])
        if len(chars) == 14:
            print(i)
            break