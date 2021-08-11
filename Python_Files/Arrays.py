# numbers = [4, 2, 4, 4], [3, 2, 2, 4]
#
# for row in numbers:
#     print([str(elem) for elem in row])
#
# for i in range(0, len(numbers)):
#     if int(numbers[i]) % 2 != 0:
#         print("True")
#     print("False")
#
# a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
# for row in a:
#     for elem in row:
#         print(elem, end=' ')
#
# a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
# s = 0
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         s += a[i][j]
# print(s)
#
# n = 4
# a = [0] * n
# for i in range(n):
#     a[i: int] = [2] * i + [1] + [0] * (n - i - 1)

# for i in range(0, len(l) - 1):
#     # we stop at the penultimate index to make sure m[i + 1] is valid
#     # checks if number to the right is identical
#     if l[i] == l[i + 1]:
#         # stores identical numbers position in array
#         print("There are identical numbers next to each the other.")
#         print(f"index {i}: {l[i]} & index {i + 1}: {l[i + 1]}")
