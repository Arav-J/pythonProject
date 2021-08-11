"""
- Input a list of booleans - (0s and 1s).
- Identify positions of said booleans in a list, do so in the format of a 4 grid (creating 2D array).

	> i.e - : [[0, 1, 2, 3],
		  [4, 5, 6, 7],
		  [8, 9, 10, 11],
		  [12, 13, 14, 15],
		  [16, 17, 18, 19]]

	N.B-: The list won't contain these numbers they just refer to the position of the boolean characters.

- Identify whether there is a 2x2 square made up of all 1s.

	> i.e -: [0, 1, 4, 5] would be an example of the 2x2 square that would look like...
        	 -------
		    | 1 | 1 |
         	 -------
		    | 1 | 1 |
 	 	     -------
- Then output the result of whether the list contains the 2x2 square.
- The 2x2 square must be completely surround by 0s or not be touching a cell.
"""
from typing import List

Matrix = List[List[int]]

#                                    ~~EXAMPLES~~
#      0         1         2          3        4         5        6             7
#   1 1 0 1   1 1 0 1   0 0 0 0   0 0 0 0   0 0 0 0   0 0 0 0  0 0 1 1  0 0 0 0 0 1 1 0 0
#   0 0 1 0   1 0 0 1   0 1 1 0   0 0 0 0   0 0 1 0   0 1 1 0  1 0 1 1  0 0 0 0 0 1 1 0 0
#   1 0 0 0   1 0 0 0   0 1 1     0 0 1 0   0 1 1 0   0 1 1 0
#   0 1 0 0   0 1 1 0   0 0 0     0 1 1 0   0 1 1 1   0 0 0 0
#                                 0 1 1 0   0 0 0 0

examples: List[Matrix] = [
    [[1, 1, 0, 1], [0, 0, 1, 0], [1, 0, 0, 0], [0, 1, 0, 0]],                # 0

    [[1, 1, 0, 1], [1, 0, 0, 1], [1, 0, 0, 0], [0, 1, 1, 0]],                # 1

    [[0, 0, 0, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0]],                   # 2

    [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0], [0, 1, 1, 0], [0, 1, 1, 0]],  # 3

    [[0, 0, 0, 0], [0, 0, 1, 0], [0, 1, 1, 0], [0, 1, 1, 1], [0, 0, 0, 0]],  # 4

    [[0, 0, 0, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]],                # 5

    [[0, 0, 1, 1], [1, 0, 1, 1]],                                            # 6

    [[0, 0, 0, 0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 0, 1, 1, 0, 0]]               # 7

]

# sum(m[i]) == 2 -> Gives a false 'True'
# m[i][3] and m[i][0] == 0 or m[i][0] and m[i][1] or m[i][2] and m[i][2] == 0 -> gives multiple incorrect 'False' returns

"""
For the 4 length column the maximum possible value has to be 2, 
because there are only 3 possible working iterations and they all add to 2:
 - 1 + 1 + 0 + 0 = 2
 - 0 + 1 + 1 + 0 = 2
 - 0 + 0 + 1 + 1 = 2

Never mind there are exception where you can get the square:
 - 1 + 0 + 1 + 1 = 3
 - 1 + 1 + 0 + 1 = 3

"""


def has_square(m: Matrix) -> bool:
    for i in range(0, len(m) - 1):  # rows
        for j in range(0, len(m[i]) - 1):  # columns
            # 0. 0 <= j < len(m[i]) - 1
            # 1. 0 <= j + 1 < len(m[i])
            # 2. len(m[i + 1]) >= len(m[i])
            # 3. 0 <= j < j + 1 < len(m[i]) <= len(m[i + 1])
            # find a black 2x2 square
            if len(m[i + 1]) >= len(m[i]) and m[i][j] == m[i][j + 1] == m[i + 1][j] == m[i + 1][j + 1] == 1:
                if is_square_isolated(m, i) and surroundings(m ,i, j, k) == True:
                    return True

    return False


def is_square_isolated(m: Matrix, i: int) -> bool:
#    if can_access and test_on_value:
    if ((sum(m[i]) == sum(m[i - 1]) == sum(m[i + 1]) == 2) and (m[i][0] + m[i][1] + m[i][2] != 3 or 0)
            or (m[i][1] + m[i][2] + m[i][3] != 3 or 0)):

        return True
    return False

def surroundings(m, i, j, k):
    if (m[i][j][k]) == 1:
        if (m[i][j][k + 2]) and (m[i][j][k - 1]) and (m[i][j - 1][k - 1]) \
                and (m[i][j + 1][k - 1]) and (m[i][j + 1][k + 2]) \
                and (m[i][j - 1][k]) and (m[i][j - 1][k + 1]) and (m[i][j - 1][k + 2]) \
                and (m[i][j + 2][k]) and (m[i][j + 2][k + 1]) and (m[i][j + 2][k + 2]) == 0 or IndexError:
            return True


def is_black(m, i, j, k):
    if 0 <= i < len(m):
        row = m[i]
        if 0 <= j < len(row):
            cell = row[j][k]
            print(cell)
            if cell == 1:
                print(cell)
                return True
    return False


# Evaluates whether this example has a square.
print(has_square(examples[0]), False, "-> 0")
print(has_square(examples[1]), False, "-> 1")
print(has_square(examples[2]), True, "-> 2")
print(has_square(examples[3]), False, "-> 3")
print(has_square(examples[4]), False, "-> 4")
print(has_square(examples[5]), True, "-> 5")
print(has_square(examples[6]), True, "-> 6")
print(has_square(examples[7]), True, "-> 7")
print(surroundings(examples, 5, 1, 1))
# print(is_black(examples, 0, 0, 0))
# Shows what type of data structure it is.
# print([type(x) for x in examples[0]]
