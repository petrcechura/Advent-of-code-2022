
# get input
with open("input.txt", 'r') as f:
    line = f.read() 

sequence = list()
last_index = 0
part_one_costant = 4
part_two_costant = 14

# function that gets sequence and decides whether it's free of duplicates
def check_repet(seq):
    s = set(seq)
    if len(s) == len(seq):
        return True

# through the array and find index that mathes criteria
for id, char in enumerate(line):
    if len(sequence) < part_one_costant: # change it to "part_two_costant" to have second result
        sequence.append(char)
    else:
        sequence.pop(0)
        sequence.append(char)
    
        if check_repet(sequence):
            last_index = id+1
            break


print("Result: " + str(last_index))
    
    
