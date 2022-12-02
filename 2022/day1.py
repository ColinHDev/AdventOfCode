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

def insertIntoList(list: list, calories: int):
    if list[2] < calories:
        list = [list[1], list[2], calories]
    elif list[1] < calories:
        list[0] = list[1]
        list[1] = calories
    elif list[0] < calories:
        list[0] = calories
    return list

mostCalories = [0, 0, 0]
i: int = 0
while i < len(calories):
    mostCalories = insertIntoList(mostCalories, calories[i])
    i += 1

print("The top three elves carry " + str(mostCalories[0] + mostCalories[1] + mostCalories[2]) + " calories together.")
