
def score_part_one(oponent, you):
    if oponent == 'A': # rock
        if you == 'X': # rock
            return 1 + 3 # draw
        elif you == 'Y': # paper
            return 2 + 6 # win
        elif you == 'Z': # scissors
            return 3 + 0 # lose
    elif oponent == 'B': # paper
        if you == 'X': # rock
            return 1 + 0 # lose
        elif you == 'Y': # paper
            return 2 + 3 # draw
        elif you == 'Z': # scissors
            return 3 + 6 # win
    elif oponent == 'C': # scissors
        if you == 'X': # rock
            return 1 + 6 # win
        elif you == 'Y': # paper
            return 2 + 0 # lose
        elif you == 'Z': # scissors
            return 3 + 3 # draw
    raise Exception('Invalid input!')

def score_part_two(oponent, outcome):
    if oponent == 'A': # rock
        if outcome == 'X': # lose
            return 3 + 0
        elif outcome == 'Y': # draw
            return 1 + 3 
        elif outcome == 'Z': # win
            return 2 + 6 
    elif oponent == 'B': # paper
        if outcome == 'X': # lose
            return 1 + 0 
        elif outcome == 'Y': # draw
            return 2 + 3 
        elif outcome == 'Z': # win
            return 3 + 6 
    elif oponent == 'C': # scissors
        if outcome == 'X': # lose
            return 2 + 0 
        elif outcome == 'Y': # draw
            return 3 + 3 
        elif outcome == 'Z': # win
            return 1 + 6 
    raise Exception('Invalid input!')


# get input into list
with open("input.txt", 'r') as f:
    lines = f.readlines()

# score variables
score_p1 = 0
score_p2 = 0

# calculate scores from both parts
for id, line in enumerate(lines):
    score_p1 += score_part_one(line[0], line[2])
    score_p2 += score_part_two(line[0], line[2])

# print scores
print("Score of part I: " + str(score_p1))
print("Score of part II: " + str(score_p2))
    