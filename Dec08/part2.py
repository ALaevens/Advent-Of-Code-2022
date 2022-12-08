def check_around(data, x, y):
    width = len(forest[0])
    height = len(forest)

    offsets = [(1, 0), (0, 1), (-1, 0), (0, -1)] # right, down, left, up

    score = 1
    
    for offset in offsets:
        
        check_x = x + offset[0]
        check_y = y + offset[1]
        distance = 1
        while 0 <= check_x < width and 0 <= check_y < height:
            if data[check_y][check_x] >= data[y][x]:
                score *= distance
                break

            check_x += offset[0]
            check_y += offset[1]
            distance += 1
        
        else:
            score *= (distance-1)

    return score

forest = []
score = 0

with open("input.txt") as f:
    for line in f:
        trees = []
        for tree in line.rstrip():
            trees.append(int(tree))
        forest.append(trees)

for y in range(0, len(forest)):
    for x in range(0, len(forest[0])):
        score = max(score, check_around(forest, x, y))

print(score)