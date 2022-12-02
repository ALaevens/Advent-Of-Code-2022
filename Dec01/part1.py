
max_calories = 0

current_sum = 0
with open("input.txt") as f:
    for line in f:
        line = line.rstrip()

        if line == "":
            max_calories = max(max_calories, current_sum)
            current_sum = 0

        else:
            current_sum += int(line)

print(max_calories)
