

# get input
items = list()
with open("input.txt", 'r') as f:
    items = f.readlines()
    
calories = list()
elf_cal = 0
for item in items:
    if item == '\n':
        calories.append(elf_cal)
        elf_cal = 0
    else:
        elf_cal += int(item)

# PART ONE
print(max(calories))


# PART TWO
most_calories = list()
for i in range(3):
    most_calories.append(max(calories))
    calories.remove(max(calories))

print(most_calories)
print(sum(most_calories))