TEMPLATE = """
┏━━━━━┳━━━━━┳━━━━━┳━━━━━┳━━━━━┳━━━━━┳━━━━━┳━━━━━┳━━━━━┓
┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃
┣━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━┣━━━━━╋━━━━━┫
┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃
┣━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━┣━━━━━╋━━━━━╋━━━━━┫
┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃
┣━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━┣━━━━━╋━━━━━╋━━━━━╋━━━━━┫
┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃
┣━━━━━╋━━━━━╋━━━━━╋━━━━━┣━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━┫
┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃
┣━━━━━╋━━━━━╋━━━━━┣━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━┫
┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃
┣━━━━━╋━━━━━┣━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━┫
┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃
┣━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━┫
┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃
┣━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━┫
┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃  {}  ┃
┗━━━━━┻━━━━━┻━━━━━┻━━━━━┻━━━━━┻━━━━━┻━━━━━┻━━━━━┻━━━━━┛
"""

STARTING_SUDOKU = [
    [4, 3, 5, 2, 6, 9, 7, 8, 1],
    [6, 8, 2, 5, 7, 1, 4, 9, 3],
    [1, 9, 7, 8, 3, 4, 5, 6, 2],
    [8, 2, 6, 1, 9, 5, 3, 4, 7],
    [3, 7, 4, 6, 8, 2, 9, 1, 5],
    [9, 5, 1, 7, 4, 3, 6, 2, 8],
    [5, 1, 9, 3, 2, 6, 8, 7, 4],
    [2, 4, 8, 9, 5, 7, 1, 3, 6],
    [7, 6, 3, 4, 1, 8, 2, 5, 9]
]

def sudoku_print(sudo):
    print(TEMPLATE.format(*[x for row in sudo for x in row]))

def the_box(su):
    # I want this code to find a 3 x 3 square inside the array
    for i in range(9):
        for j in range(9):
            i = 0
            j = 0
            box = [su[i][j], su[i+1][j], su[i+2][j],
                   su[i][j+1], su[i+1][j+1], su[i+2][j+1],
                   su[i][j+2], su[i+1][j+2], su[i+2][j+2]]
            # if (box[i][j])%3 == 0:
            # return box


def box_indices(box):

    for x in range(9):
        # We enumerate every box. The variable x takes 1 value for each box.
        # Using x, we can find the "number of boxes above" (helps finding the starting row)
        # and "number of boxes before" (helps finding the starting column)

        # 1. Find the coordinates of the top left cell for a given box
        # (where 'given box' means 'box of index x')
        print(f"x is {x}, x // 3 is {x // 3}, x % 3 is {x % 3}")
        print(f"  -> the top left cell is ({0}, {0})\n")

    # return sudok

if __name__ == '__main__':
    # sudoku = box_indices(STARTING_SUDOKU)
    # sudoku_print(sudoku)

    for box_i in range(3):
        for box_j in range(3):
            # top left cell of the box (box_i, box_j)
            for cell_i in range(box_i * 3, box_i * 3 + 3):
                for cell_j in range(box_j * 3, box_j * 3 + 3):
                    STARTING_SUDOKU[cell_i][cell_j] = box_i * 3 + box_j
    # for box_index in range(9):
    #     box_i = box_index // 3
    #     box_j = box_index % 3
    #     for cell_index in range(9):
    #         STARTING_SUDOKU[box_i * 3 + cell_index // 3][box_j * 3 + cell_index % 3] = cell_index

    sudoku_print(STARTING_SUDOKU)