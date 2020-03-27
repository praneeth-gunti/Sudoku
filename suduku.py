grid = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


def valid(b, val, pos):
    # row
    for i in range(len(b[0])):
        if b[pos[0]][i] == val and i != pos[1]:
            return False
    # col
    for j in range(len(b)):
        if b[j][pos[1]] == val and j != pos[0]:
            return False
    # 3*3 grid
    grid_x = pos[0] // 3
    grid_y = pos[1] // 3

    for i in range(grid_x*3, grid_x*3 + 3):
        for j in range(grid_y*3, grid_y*3 + 3):
            if b[i][j] == val and (i, j) != pos:
                return False
    return True


def print_board(b):
    for i in range(len(b)):
        if i % 3 == 0:
            print("----------------------------------------")
        for j in range(len(b[0])):
            if j % 3 == 0:
                print(" | ", end=" ")
            if j < 8:
                print(str(b[i][j]) + " ", end=" ")
            else:
                print(str(b[i][j]) + " | ")
    print("----------------------------------------")


def empty_space(b):
    for i in range(len(b)):
        for j in range(len(b[0])):
            if b[i][j] == 0:
                return i, j   # row, col
    return False


def solve(b):
    zero = empty_space(b)
    if not zero:
        return True
    else:
        row, col = zero
    for i in range(1, 10):
        if valid(b, i, (row, col)):
            b[row][col] = i
            if solve(b):
                return True
            else:
                b[row][col] = 0
    return False


print_board(grid)
print("-------------SOLUTION-------------------")
solve(grid)
print_board(grid)
