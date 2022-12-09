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


head_pos = Vector2(0, 0)
tail_pos = Vector2(0, 0)
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
            head_pos, tail_pos = follow(head_pos + dir_char_to_vec[direction], tail_pos)
            tail_visits.add(tail_pos)

print(len(tail_visits))
