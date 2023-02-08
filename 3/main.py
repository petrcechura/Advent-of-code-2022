
# get input
with open("input.txt", 'r') as f:
    lines = f.readlines()

### PART ONE ###
# create rucksacks that contain tuple of first and second part
rucksacks = []    

for line in lines:
    half_size = len(line)/2 - 1
    part_one = line[0:int(half_size+1)]
    part_two = line[int((half_size+1)):int((len(line)-1))]
    rucksacks.append((part_one, part_two))

# get common characters from first and second part of each item from rucksack
contents = []

for item in rucksacks:
    for char in item[0]:
        if item[1].find(char) != -1:
            contents.append(char)
            break
        
# calculate score (priorities)
score = 0
lowercase_offset = 96
uppercase_offset = 38

for char in contents:
    points = ord(char)
    
    if char.isupper() == True:
        points -= uppercase_offset
    else:
        points -= lowercase_offset
    
    score += points
    
print("Score of part one: " + str(score))

### PART TWO ###

# get tuples of three-elf groups
groups = []

for i in range(len(lines)):
    if i % 3 == 0:
        groups.append((lines[i], lines[i+1], lines[i+2]))
        
# get common characters of tuple
common_chars = []

for group in groups:
    for char in group[0]:
        if group[1].find(char) != -1:
            if group[2].find(char) != -1:
                    common_chars.append(char)
                    break
# calculate score
score = 0

for char in common_chars:
    points = ord(char)
    
    if char.isupper() == True:
        points -= uppercase_offset
    else:
        points -= lowercase_offset
    
    score += points

print("Score of part two: " + str(score))