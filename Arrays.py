numbers = [4, 2, 4, 4], [3, 2, 2, 4]

for row in numbers:
    print([str(elem) for elem in row])

for i in range(0, len(numbers)):
    if numbers[i] % 2 != 0:
        print("True")
    print("False")

a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
for row in a:
    for elem in row:
        print(elem, end=' ')

a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
s = 0
for i in range(len(a)):
    for j in range(len(a[i])):
        s += a[i][j]
print(s)
print(s)

n = 4
a = [0] * n
for i in range(n):
    a[i] = [2] * i + [1] + [0] * (n - i - 1)

