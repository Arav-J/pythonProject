from typing import List

# solved array
sudoku = [[4, 3, 5, 2, 6, 9, 7, 8, 1],
          [6, 8, 2, 5, 7, 1, 4, 9, 3],
          [1, 9, 7, 8, 3, 4, 5, 6, 2],
          [8, 2, 6, 1, 9, 5, 3, 4, 7],
          [3, 7, 4, 6, 8, 2, 9, 1, 5],
          [9, 5, 1, 7, 4, 3, 6, 2, 8],
          [5, 1, 9, 3, 2, 6, 8, 7, 4],
          [2, 4, 8, 9, 5, 7, 1, 3, 6],
          [7, 6, 3, 4, 1, 8, 2, 5, 9]]

# Function to detect repeated values horizontally
def horizontally_valid(l: List[List[int]]) -> bool:
# Looks at each row
    for row in range(0, len(l)):
# Looks at full range
        for i in range(0, len(l[row])):
# Goes through each value moving to the right
            for j in range(i+1, len(l[row])):
# Looks at index and then each value specifically and acknowledges overlapping value
                if l[row][i] == l[row][j]:
                    return False
    return True


# Function to detect repeated values vertically
def vertically_valid(grid: List[List[int]]) -> bool:
# Looks at each column
    for column in range(9):
# Chicken will contain the elements of column j
        chicken = []
# Looks at the rows via the selected column
        for row in range(9):
# Adding values to the list 'chicken'
            chicken.append(grid[row][column])
# we test chicken (the column) for duplicates
        for m in range(0, len(chicken)):
            for l in range(m + 1, len(chicken)):
                if chicken[m] == chicken[l]:
                    return False
    return True


def box_validation(tango: List[List[int]])-> None:
# for this one call i and j - x and y.
# give the 9 key boxes co-ordinates, from 0 to 2 in x and y directions
# integer division(//) for the x movement and modulus for the y movement(%)
        for x in range(len(tango)):
            for y in range(len(tango)):
# Create the 9 3x3 boxes
                ...


def validation(sud):
    if horizontally_valid(sud) and vertically_valid(sud) == True:
        print("-> The sudoku board is correct.")
    else:
        print("-> The sudoku board is not correct.")


sudoku_template = """
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

# dark magic [2D list comprehension]
print(sudoku_template.format(*[cell for row in sudoku for cell in row]))

validation(sudoku)

box_validation(sudoku)

