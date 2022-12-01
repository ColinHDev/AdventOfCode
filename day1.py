calories = [0]

# reading the data from the file
file = open("input.txt", "r")
elf: int = 0
for line in file:
    if line == "\n":
        elf += 1
        calories.append(0)
    else:
        calories[elf] += int(line)

mostCaloriesElf: int = 0
mostCalories: int = 0
i: int = 0
while i < len(calories):
    if calories[i] > mostCalories:
        mostCalories = calories[i]
        mostCaloriesElf = i
    i += 1

print("The elf carrying the most calories is number " + str(mostCaloriesElf + 1) + ", carrying " + str(mostCalories) + " calories.")
