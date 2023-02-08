
# get input into lines
with open("input.txt", 'r') as f:
    lines = f.readlines()

# assign pairs into lists 
first_elves = []
second_elves = []

for line in lines:
    pair = line.rsplit(sep=',')
    first_elves.append([int(pair[0].rsplit(sep='-')[0]), int(pair[0].rsplit(sep='-')[1])])
    second_elves.append([int(pair[1].rsplit(sep='-')[0]), int(pair[1].rsplit(sep='-')[1])])

# calculate amount of full overlaps
amount_of_full_overlaps = 0
amount_of_no_overlaps = 0

for i in range(len(first_elves)):
    
    # if first border of 1st elf is lower than first border of 2nd elf
    # and second border of 1st is higher than second border of 2nd elf, the 1st elf overlaps job of second one
    if first_elves[i][0] <= second_elves[i][0] and first_elves[i][1] >= second_elves[i][1]: 
        amount_of_full_overlaps += 1                     
    # if first border of 2nd elf is lower than first border of 1st elf 
    # and second border of 2nd is higher than second border of 1nd elf, the 2nd elf overlaps job of first one                                                    
    elif first_elves[i][0] >= second_elves[i][0] and first_elves[i][1] <= second_elves[i][1]:
        amount_of_full_overlaps += 1
    # if second border of 1st elf is lower than first border of 2nd elf (..1st...2nd..) or viceversa (..2nd...1st..), there is no overlap
    elif first_elves[i][1] < second_elves[i][0] or second_elves[i][1] < first_elves[i][0]:
        amount_of_no_overlaps += 1
        
print("Amount of full overlaps: " + str(amount_of_full_overlaps))
print("Amount of overlaps at all: "  + str(len(first_elves) - amount_of_no_overlaps))




    
