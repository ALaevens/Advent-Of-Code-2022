import string

with open("input.txt") as f:
    priority_sum = 0
    for line in f:
        rucksack = line.rstrip()

        first = set(rucksack[0:len(rucksack)//2])
        second = set(rucksack[len(rucksack)//2:])

        both = first.intersection(second)

        common = both.pop()
        priority = string.ascii_lowercase.find(common.lower()) + 1
        
        
        if common.isupper():
            priority += 26

        priority_sum += priority

    print(priority_sum)

        
