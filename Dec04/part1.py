
with open("input.txt") as f:
    overlaps = 0
    for line in f:
        elves = line.rstrip().split(",")

        ranges = []
        for elf in elves:
            start, end = elf.split("-")
            ranges.append(range(int(start), int(end)+1))
        
        first = set(ranges[0])
        second = set(ranges[1])

        if first.issuperset(second) or second.issuperset(first):
            overlaps += 1

    print(overlaps)
        

        