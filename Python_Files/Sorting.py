# some_list = [3, 1, 4, 8]
# [1, 3, 4, 8]
"""
Taking a list of numbers and organising them in order of size.
First iteration took a list of 4 and and worked, but when the length of the list was increased
there was an issue with the logic statements.
The logic statements have now been adjusted.
"""
some_list = [5, 6, 7, 8, 8, 9, 0, 4, 3, 3, 3, 4, 5, 6]


def sort_list(something):
    for i in range(len(something)):
        print(f"i {i}")
        for j in range(i + 1, len(something)):
            if something[i] > something[j]:
                new_number = something[i]
                something[i] = something[j]
                something[j] = new_number

    return print(something)


sort_list(some_list)
