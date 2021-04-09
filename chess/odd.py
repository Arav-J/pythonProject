def oddeven(i):
    if i % 2 == 0:
        return False
    return True


# print(oddeven(4177777777777))

def odd_list(numbers):
    for i in range(0, len(numbers)):
        if numbers[i] % 2 != 0:
            return True
    return False


print(odd_list([2, 2, 2, 2, 2, 5, 2, 2, 2, 2]), True)
print(odd_list([]), False)
print(odd_list([1]), True)
print(odd_list([2, 1]), True)
print(odd_list([1, 2]), True)
print(odd_list([2, 4, 6]), False)
print(odd_list([2]), False)

# check in a 2D array whether or not all rows and columns contain an odd number
