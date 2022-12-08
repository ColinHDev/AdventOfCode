trees = []
for line in open("input.txt", "r"):
    trees.append(line.replace("\n", ""))


def calculate_scenic_score(row: int, column: int):
    # edge tree
    if row == 0 or row == len(trees) - 1 or column == 0 or column == len(trees[row]) - 1:
        return 0
    height = int(trees[row][column])
    # looking up
    up_count = 0
    for i in range(row - 1, -1, -1):
        up_count += 1
        if int(trees[i][column]) >= height:
            break
    # looking down
    down_count = 0
    for i in range(row + 1, len(trees)):
        down_count += 1
        if int(trees[i][column]) >= height:
            break
    # looking left
    left_count = 0
    for i in range(column - 1, -1, -1):
        left_count += 1
        if int(trees[row][i]) >= height:
            break
    # looking right
    right_count = 0
    for i in range(column + 1, len(trees[row])):
        right_count += 1
        if int(trees[row][i]) >= height:
            break
    return up_count * down_count * left_count * right_count


highest_scenic_score = 0
for row_ in range(1, len(trees) - 1):
    for column_ in range(1, len(trees[row_]) - 1):
        score = calculate_scenic_score(row_, column_)
        highest_scenic_score = max(score, highest_scenic_score)
print(highest_scenic_score)
