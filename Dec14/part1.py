from vector import Vector2

def sign(n):
    if n == 0:
        return 0

    return int(n / abs(n))

def add_line(world, start, end):
    diff = end-start
    step = Vector2(sign(diff.x), sign(diff.y))

    pos = start
    while pos != end:
        world[pos] = "#"
        
        pos += step
    else:
        world[pos] = "#"

def drop(world: dict, bottom):
    pos = Vector2(500, 0)

    drop_dirs = [Vector2(0, 1), Vector2(-1, 1), Vector2(1, 1)]

    while pos.y < bottom:
        cant_move = True
        for drop_dir in drop_dirs:
            if world.get(pos + drop_dir, None) is None:
                pos += drop_dir
                cant_move = False
                break
        
        if cant_move:
            world[pos] = "o"
            return True
    
    return False

world = {}
bottom = 0
with open("input.txt") as f:
    for line in f:
        pairs = line.strip().split(" -> ")
        coords = [Vector2(*[int(coord) for coord in pair.split(",")]) for pair in pairs]

        for i in range(len(coords)-1):
            add_line(world, coords[i], coords[i+1])

            bottom = max(bottom, coords[i].y, coords[i+1].y)

drops = 0
while drop(world, bottom):
    drops += 1

print(drops)
