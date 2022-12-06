with open("input.txt") as f:
    line = f.readline().rstrip()

    for i in range(4, len(line)+1):
        chars = set(line[i-4:i])
        if len(chars) == 4:
            print(i)
            break