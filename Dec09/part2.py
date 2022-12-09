from vector import Vector2

def sign(n):
    return int(n / abs(n))

def follow(head, tail):
    diff = head - tail

    if abs(diff.x) <= 1 and abs(diff.y) <= 1: # touching or covering
        pass

    elif diff.x == 0 or diff.y == 0: # away on same row / column
        tail = tail + (diff // 2)

    else: # away diagonally
        tail = tail + Vector2(sign(diff.x), sign(diff.y))

    return head, tail


knots = [Vector2(0, 0) for _ in range(10)]
tail_visits = set()

dir_char_to_vec = {
    "R": Vector2(1, 0), 
    "L": Vector2(-1, 0),
    "U": Vector2(0, 1),
    "D": Vector2(0, -1),
}

with open("input.txt") as f:
    for line in f:
        line = line.rstrip()
        
        direction, moves = line.split()
        moves = int(moves)

        for i in range(moves):
            knots[0] = knots[0] + dir_char_to_vec[direction]
            for knot in range(len(knots)-1):
                knots[knot], knots[knot+1] = follow(knots[knot], knots[knot+1])

            tail_visits.add(knots[-1])

print(len(tail_visits))
