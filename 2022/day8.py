trees = []
for line in open("input.txt", "r"):
    trees.append(line.replace("\n", ""))


def is_tree_visible(row: int, column: int):
    # edge tree
    if row == 0 or row == len(trees) - 1 or column == 0 or column == len(trees[row]) - 1:
        return True
    height = int(trees[row][column])
    # looking up
    for i in range(0, row):
        if int(trees[i][column]) >= height:
            break
    else:
        return True
    # looking down
    for i in range(row + 1, len(trees)):
        if int(trees[i][column]) >= height:
            break
    else:
        return True
    # looking left
    for i in range(0, column):
        if int(trees[row][i]) >= height:
            break
    else:
        return True
    # looking right
    for i in range(column + 1, len(trees[row])):
        if int(trees[row][i]) >= height:
            break
    else:
        return True
    return False


visible_tree_count = 0
for row_ in range(0, len(trees)):
    for column_ in range(0, len(trees[row_])):
        if is_tree_visible(row_, column_):
            visible_tree_count += 1
print(visible_tree_count)
