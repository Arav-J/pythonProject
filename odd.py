# check in a 2D array whether or not all rows and columns contain an odd number

def is_odd(number):
    if number % 2 == 0:
        return False
    return True


# print(oddeven(4177777777777))

def odd_lists(list_of_numbers):
    # for i in range(0, len(list_of_numbers)):
    #     number = list_of_numbers[i]
    #     if is_odd(number):
    #         return True
    # return False

    for number in list_of_numbers:
        if is_odd(number):
            return True
    return False


def odd_grid(list_of_list_of_numbers):
    for list_of_number in list_of_list_of_numbers:
        if odd_lists(list_of_number):
            ...
        else:
            return False
    return True

    # for i in range(0, range(list_of_list_of_numbers)):
    #     list_of_numbers = list_of_list_of_numbers[i]
    #     is_list_odd = odd_lists(list)


print(odd_grid([[2, 3], [4, 2, 2, 2, 2, 2], [4, 6, 8, 2]]), False)
print(odd_grid([[2, 2, 2, 2], [4, 2, 2, 2, 2, 2], [4, 6, 8, 2]]), False)
print(odd_grid([[2, 2, 2, 3], [3, 2, 2, 2, 2, 2], [4, 6, 8, 3]]), True)
print(odd_grid([[5, 2, 2, 3], [4, 7, 2, 2, 5, 2], [4, 6, 8, 2, 9, 3]]), True)
print(odd_grid([]), False)

test_cases = [odd_grid([])]

for __name__ in ...:
    print()
