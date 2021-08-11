# sudoku = [[4, 3, 5, 2, 6, 9, 7, 8, 1],
#           [6, 8, 2, 5, 7, 1, 4, 9, 3],
#           [1, 9, 7, 8, 3, 4, 5, 6, 2],
#           [8, 2, 6, 1, 9, 5, 3, 4, 7],
#           [3, 7, 4, 6, 8, 2, 9, 1, 5],
#           [9, 5, 1, 7, 4, 3, 6, 2, 8],
#           [5, 1, 9, 3, 2, 6, 8, 7, 4],
#           [2, 4, 8, 9, 5, 7, 1, 3, 6],
#           [7, 6, 3, 4, 1, 8, 2, 5, 9]]


# sudoku_template =  """
# ┏━━━━━┳━━━━━┳━━━━━┳━━━━━┳━━━━━┳━━━━━┳━━━━━┳━━━━━┳━━━━━┓
# ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃
# ┣━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━┣━━━━━╋━━━━━┫
# ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃
# ┣━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━┣━━━━━╋━━━━━╋━━━━━┫
# ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃
# ┣━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━┣━━━━━╋━━━━━╋━━━━━╋━━━━━┫
# ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃
# ┣━━━━━╋━━━━━╋━━━━━╋━━━━━┣━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━┫
# ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃
# ┣━━━━━╋━━━━━╋━━━━━┣━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━┫
# ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃
# ┣━━━━━╋━━━━━┣━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━┫
# ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃
# ┣━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━┫
# ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃
# ┣━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━┫
# ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃
# ┗━━━━━┻━━━━━┻━━━━━┻━━━━━┻━━━━━┻━━━━━┻━━━━━┻━━━━━┻━━━━━┛
# """


# dark magic [2D list comprehension]
# print(sudoku_template.format(*[cell for row in sudoku for cell in row]))
# for j in range(9):
#     chicken = []
    # chicken will contain the elements of column j
    # for i in range(9):
    #     chicken.append(sudoku[i][j])
    # we test chicken (the column) for duplicates
    # for m in range(0, len(chicken)):
    #     for l in range(m + 1, len(chicken)):
    #         if chicken[m] == chicken[l]:
    #            ...
    # duplicate!


# first loop defines what we're looking at (columns here)
# for j in col_indices:
#     # before a column
#     ...
#     # to look at column j, we need each rows i of that column
#     for i in rows_indices:
#         ...
#     # after a column
#     ...
# use other function - horizontal


    # if sum(set(sudoku)) == sum(sudoku[i][j]):
    #     before = sudoku[i][j]
    #     sudoku[i][j] = " "
    #     print(sudoku_template.format(*[x for rows in sudoku for x in rows]))
    #     sudoku[i][j] = before
    # print("+ " + f" after col {j} ".center(60, '-') + " +")


# print("\n" * 20)
# for i in range(9):
#     print("+ " + f" before row {i} ".center(60, '-') + " +")
#     for j in range(9):
#         before = sudoku[i][j]
#         sudoku[i][j] = " "
#         print(sudoku_template.format(*[x for rows in sudoku for x in rows]))
#         sudoku[i][j] = before
#     print("+ " + f" after row {i} ".center(60, '-') + " +")


# print("\n" * 20)
# for j in range(9):
#     print("+ " + f" before col {j} ".center(60, '-') + " +")
#     for i in range(9):
#         before = sudoku[i][j]
#         sudoku[i][j] = " "
#         print(sudoku_template.format(*[x for rows in sudoku for x in rows]))
#         sudoku[i][j] = before
#     print("+ " + f" after col {j} ".center(60, '-') + " +")


# print(f" Horizontally is {horizontally_valid(sudoku)}")
# print(f" Vertically is {vertically_valid(sudoku)}")


# print(f"-> There is an error with one of the boxes{box_validation(sudoku)}")


# def index_training(tango):
#     for x in range(9):
#         ...
#     print(sudoku_template.format(*[x for rows in tango for x in rows]))

# index_training(sudoku)


# the 'not so dark' way
# print(sudoku_template.format(
#   *sudoku[0],
#   *sudoku[1],
#   *sudoku[2],
#   *sudoku[3],
#   *sudoku[4],
#   *sudoku[5],
#   *sudoku[6],
#   *sudoku[7],
#   *sudoku[8]
# ))

# boxes = [tango[0][0], tango[0][1], tango[0][2],
#                          tango[1][0], tango[1][1], tango[1][2],
#                          tango[2][0], tango[2][1], tango[2][2]], \
#                         [tango[0][3], tango[0][4], tango[0][5],
#                          tango[1][3], tango[1][4], tango[1][5],
#                          tango[2][3], tango[2][4], tango[2][5]], \
#                         [tango[0][6], tango[0][7], tango[0][8],
#                          tango[1][6], tango[1][7], tango[1][8],
#                          tango[2][6], tango[2][7], tango[2][8]], \
#                         [tango[3][0], tango[3][1], tango[3][2],
#                          tango[4][0], tango[4][1], tango[4][2],
#                          tango[5][0], tango[5][1], tango[5][2]], \
#                         [tango[3][3], tango[3][4], tango[3][5],
#                          tango[4][3], tango[4][4], tango[4][5],
#                          tango[5][3], tango[5][4], tango[5][5]], \
#                         [tango[3][6], tango[3][7], tango[3][8],
#                          tango[4][6], tango[4][7], tango[4][8],
#                          tango[5][6], tango[5][7], tango[5][8]], \
#                         [tango[6][0], tango[6][1], tango[6][2],
#                          tango[7][0], tango[7][1], tango[7][2],
#                          tango[8][0], tango[8][1], tango[8][2]], \
#                         [tango[6][3], tango[6][4], tango[6][5],
#                          tango[7][3], tango[7][4], tango[7][5],
#                          tango[8][3], tango[8][4], tango[8][5]], \
#                         [tango[6][6], tango[6][7], tango[6][8],
#                          tango[7][6], tango[7][7], tango[7][8],
#                          tango[8][6], tango[8][7], tango[8][8]]

        # print(f"{boxes[0]}, {boxes[1]}, {boxes[2]}, "
        #       f"\n{boxes[3]}, {boxes[4]}, {boxes[5]}, "
        #       f"\n{boxes[6]}, {boxes[7]}, {boxes[8]}")