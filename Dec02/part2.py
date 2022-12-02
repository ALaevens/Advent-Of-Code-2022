
# A=Rock, B=Paper, C=Scissors
# X=Lose, Z=Win
outcome_to_move = {
    ("A", "X"): "C",
    ("A", "Z"): "B",
    ("B", "X"): "A",
    ("B", "Z"): "C",
    ("C", "X"): "B",
    ("C", "Z"): "A",
}

move_score = {"A": 1, "B": 2, "C": 3}
outcome_score = {"X": 0, "Y": 3, "Z": 6}

total_score = 0
with open("input.txt") as f:
    for line in f:
        line = line.rstrip()
        opponent_move, desired_outcome = line.split()

        my_move = outcome_to_move.get((opponent_move, desired_outcome), opponent_move)
        total_score += move_score[my_move]
        total_score += outcome_score[desired_outcome]
            
print(total_score)

