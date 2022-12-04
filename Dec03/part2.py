import string

def get_common(rucksacks):
    common = None
    for sack in rucksacks:
        if common is None:
            common = set(sack)
        else:
            common = common.intersection(sack)
    return common.pop()

with open("input.txt") as f:
    priority_sum = 0

    rucksacks = []
    for line in f:
        rucksack = line.rstrip()
        rucksacks.append(rucksack)

        if len(rucksacks) == 3:
            common = get_common(rucksacks)
            rucksacks = []

            priority = string.ascii_lowercase.find(common.lower()) + 1
        
        
            if common.isupper():
                priority += 26

            priority_sum += priority

    print(priority_sum)
