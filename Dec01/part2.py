import bisect

top3 = [0, 0, 0]

current_sum = 0
with open("input.txt") as f:
    for line in f:
        line = line.rstrip()

        if line == "":
            if current_sum > top3[0]:
                top3.pop(0)
                bisect.insort(top3, current_sum)
            current_sum = 0

        else:
            current_sum += int(line)

print(f"{top3} => {sum(top3)}")