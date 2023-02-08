import numpy as np
import re
import copy

# get lines from input 
with open("input.txt", 'r') as f:
    lines = f.readlines()

# get lines that are about crates
crate_lines = []

for line in lines:
    if line.__contains__('['):
        crate_lines.append(line)


# derive stacks from crate_lines into list; each stack begins (index 0) with item that's on top; stacks are indexed from 0 too
stacks = []

for i in range(len(lines[0])):
    stack = []
    for line in crate_lines:
        if line[i].isupper():
            stack.append(line[i])
    if len(stack) > 0:
        stacks.append(stack)
        
# get moves

moves = []
# indexing
#   0 = amount of crates
#   1 = 'from' index
#   2 = 'to' index

for line in lines:
    if line.__contains__("move"):
        move = list(map(int, re.findall('\d+', line)))
        moves.append(move)


### PART ONE ###
stacks_part_one = copy.deepcopy(stacks)

# do the moves
for move in moves:    
    for i in range(move[0]):
        item = stacks_part_one[move[1]-1].pop(0)
        stacks_part_one[move[2]-1].insert(0, item)

result = ""
for stack in stacks_part_one:
    result += stack[0]

print("Part one result: " + str(result))

### PART TWO ###
stacks_part_two = copy.deepcopy(stacks)

# do the moves
for move in moves:
    op_list = []
    for i in range(move[0]):
        op_list.append(stacks_part_two[move[1]-1].pop(0))
    for i in range(move[0]):
        stacks_part_two[move[2]-1].insert(0, op_list[len(op_list)-1])
        op_list.pop(len(op_list)-1)

result = ""
for stack in stacks_part_two:
    result += stack[0]
    
print("Part two result: " + str(result))
        


                