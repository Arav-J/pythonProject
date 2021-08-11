n = 0
count = 0
numbers = 0
array = [0, 1, 1, 0]

for i in range(0, 3):
    array[i] = n
    if n == 1:
        count = count + 1
    array[i] = numbers
    if numbers == 0:
        count = count - 1

print(n)
print(numbers)

count = n - numbers

print(count)
