import bisect

def height_at(point, height_map):
    return height_map[point[0]][point[1]]

def heuristic(point, height_map):
    height = height_at(point, height_map)
    return 25 - height

def path_cost(path, height_map):
    cost = len(path) + heuristic(path[-1], height_map)

    return cost

def get_neighbours(point, height_map):
    height = height_at(point, height_map)

    offsets = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    neighbours = []
    for offset in offsets:
        neighbour_pos = (point[0] + offset[0], point[1] + offset[1])

        if 0 <= neighbour_pos[0] < len(height_map) and \
           0 <= neighbour_pos[1] < len(height_map[0]) and \
           height-1 <= height_at(neighbour_pos, height_map) <= 25:
           neighbours.append(neighbour_pos)

    return neighbours

 
def a_star(start_point, height_map):
    frontier = [[start_point]]
    explored = [start_point]

    while len(frontier) > 0:
        path = frontier.pop(0)

        if height_at(path[-1], height_map) == 0:
            return path

        for neighbour in get_neighbours(path[-1], height_map):
            if neighbour not in explored:
                bisect.insort(frontier, path + [neighbour], key=lambda p: path_cost(p, height_map))
                explored.append(neighbour)

    return frontier

height_map = []
start_point = None
with open("input.txt") as f:
    row = 0
    for line in f:
        line = line.strip()

        if "S" in line:
            line = line.replace("S", "a")

        if "E" in line:
            col = line.index("E")
            start_point = (row, col)
            line = line.replace("E", "z")
        
        height_map.append([ord(x) - ord("a") for x in line])
        row += 1

path = a_star(start_point, height_map)
print(len(path)-1)

