# some_list = [3, 1, 4, 8]
# [1, 3, 4, 8]
"""
Taking a list of numbers and organising them in order of size.
First iteration took a list of 4 and and worked, but when the length of the list was increased
there was an issue with the logic statements.
The logic statements have now been adjusted.
"""
some_list = [3, 1, 4, 8, 2, 7, 5, 2, 3, 7, 8, 12]


def sort_list(something):
    i = 0
    for i in range(i, len(something)):
        for j in range(i + 1, len(something)):
            if something[i] > something[j]:
                new_number = something[i]
                something[i] = something[j]
                something[j] = new_number

    return print(something)


sort_list(some_list)
