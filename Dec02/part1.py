
# A=X=Rock, B=Y=Paper, C=Z=Scissors
outcome_score = {
    ("A", "Y"): 6,
    ("A", "Z"): 0,
    ("B", "X"): 0,
    ("B", "Z"): 6,
    ("C", "X"): 6,
    ("C", "Y"): 0
}

move_score = {"X": 1, "Y": 2, "Z": 3}

total_score = 0
with open("input.txt") as f:
    for line in f:
        line = line.rstrip()
        opponent_move, my_move = line.split()

        total_score += move_score[my_move]
        total_score += outcome_score.get((opponent_move, my_move), 3)
            
print(total_score)

